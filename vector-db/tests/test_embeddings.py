import types
from unittest.mock import Mock

import pytest

from embeddings import get_embedding


class DummyResponse:
    def __init__(self, data):
        self._data = data

    def json(self):
        return self._data


def test_get_embedding_monkeypatch(monkeypatch):
    dummy = DummyResponse({"embedding": [0.1, 0.2, 0.3]})

    mock_post = Mock(return_value=dummy)
    monkeypatch.setattr("requests.post", mock_post)

    emb = get_embedding("hello world")

    assert isinstance(emb, list)
    assert emb == [0.1, 0.2, 0.3]
    mock_post.assert_called_once()
