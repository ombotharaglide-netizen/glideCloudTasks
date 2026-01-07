import numpy as np
from unittest.mock import Mock

import pytest

import search


def test_cosine_similarity_identical():
    a = np.array([1.0, 0.0])
    b = np.array([1.0, 0.0])
    assert pytest.approx(search.cosine_similarity(a, b)) == 1.0


def test_cosine_similarity_orthogonal():
    a = np.array([1.0, 0.0])
    b = np.array([0.0, 1.0])
    assert pytest.approx(search.cosine_similarity(a, b)) == 0.0


def test_search_prefers_best_match(monkeypatch):
    # Mock get_embedding to return a query vector
    monkeypatch.setattr(search, "get_embedding", lambda q: np.array([1.0, 0.0]))

    # Create fake documents with embeddings
    docs = [
        {"text": "doc1", "embedding": np.array([0.0, 1.0])},
        {"text": "doc2", "embedding": np.array([1.0, 0.0])},
    ]

    fake_collection = Mock()
    fake_collection.find.return_value = docs

    monkeypatch.setattr(search, "collection", fake_collection)

    result = search.search("query")

    assert result == "doc2"
