from __future__ import annotations

import string


def load_text(path: str) -> str:
    """Load text from a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def normalize_text(text: str) -> str:
    """Convert text to lowercase and remove punctuation."""
    text = text.lower()
    return text.translate(str.maketrans("", "", string.punctuation))


def tokenize(text: str) -> list[str]:
    """Split text into words."""
    return text.split()


def count_words(words: list[str]) -> dict[str, int]:
    """Count frequency of each word."""
    counts: dict[str, int] = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_n_words(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return top N most common words."""
    if n <= 0:
        return []

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]


def extra_insight(words: list[str], counts: dict[str, int]) -> list[str]:
    """Return words that appear only once."""
    return [word for word, count in counts.items() if count == 1]


# Optional: run the program
if __name__ == "__main__":
    text = load_text("data/sample.txt")
    text = normalize_text(text)
    words = tokenize(text)
    counts = count_words(words)

    print("Total words:", len(words))
    print("Unique words:", len(counts))
    print("Top 3 words:", top_n_words(counts, 3))
    print("Words that appear once:", extra_insight(words, counts))