from unittest.mock import Mock

import builtins
import io

import ingest


def test_ingest_reads_and_inserts(monkeypatch):
    # Prepare fake file content
    fake_file = io.StringIO("first line\nsecond line\n\nthird line\n")

    # Mock open to return our fake file
    monkeypatch.setattr(builtins, "open", lambda *args, **kwargs: fake_file)

    # Mock get_embedding to return a predictable vector
    monkeypatch.setattr(ingest, "get_embedding", lambda t: [0.1, 0.2])

    # Mock collection methods
    fake_collection = Mock()
    fake_collection.delete_many = Mock()
    fake_collection.insert_one = Mock()

    monkeypatch.setattr(ingest, "collection", fake_collection)

    # Run ingest
    ingest.ingest()

    # delete_many should be called once
    fake_collection.delete_many.assert_called_once()

    # insert_one should be called for 3 non-empty lines
    assert fake_collection.insert_one.call_count == 3
