import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def ensure_nltk_resources() -> None:
    resources = [
        ('tokenizers/punkt', 'punkt'),
        ('corpora/stopwords', 'stopwords'),
    ]
    for resource_path, package in resources:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(package)


def remove_special_characters(text: str) -> str:
    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]', '', text)


def tokenize(text: str, language: str = 'spanish', remove_stopwords: bool = True) -> list[str]:
    language = language.lower()
    if language not in {'spanish', 'english'}:
        raise ValueError("Language must be 'spanish' or 'english'")

    tokens = word_tokenize(text, language=language)
    tokens = [token.lower() for token in tokens if token.isalpha()]

    if remove_stopwords:
        stop_words = set(stopwords.words(language))
        tokens = [token for token in tokens if token not in stop_words]

    return tokens


def stemming_tokens(tokens: list[str], language: str = 'spanish') -> list[str]:
    language = language.lower()
    if language not in {'spanish', 'english'}:
        raise ValueError("Language must be 'spanish' or 'english'")

    stemmer = SnowballStemmer(language)
    return [stemmer.stem(token) for token in tokens]


def build_tfidf_matrix(documents: list[str]) -> tuple[TfidfVectorizer, 'scipy.sparse.csr_matrix']:
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    return vectorizer, tfidf_matrix


def score_queries_tfidf(vectorizer: TfidfVectorizer, tfidf_matrix, queries: list[str]) -> list[list[float]]:
    query_matrix = vectorizer.transform(queries)
    return cosine_similarity(tfidf_matrix, query_matrix).tolist()
