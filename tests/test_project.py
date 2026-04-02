from src.project import (
    load_text,
    normalize_text,
    tokenize,
    count_words,
    top_n_words,
    extra_insight,
)


def test_load_text():
    text = load_text("data/sample.txt")
    assert isinstance(text, str)
    assert len(text) > 0


def test_normalize_text():
    assert normalize_text("Hello!") == "hello"


def test_tokenize():
    assert tokenize("hello world") == ["hello", "world"]


def test_count_words():
    result = count_words(["a", "b", "a"])
    assert result == {"a": 2, "b": 1}


def test_top_n_words():
    counts = {"a": 3, "b": 1, "c": 2}
    result = top_n_words(counts, 2)
    assert result == [("a", 3), ("c", 2)]


def test_top_n_words_edge():
    counts = {"a": 1}
    assert top_n_words(counts, 0) == []


def test_extra_insight():
    words = ["a", "b", "a", "c"]
    counts = {"a": 2, "b": 1, "c": 1}
    result = extra_insight(words, counts)
    assert sorted(result) == ["b", "c"]