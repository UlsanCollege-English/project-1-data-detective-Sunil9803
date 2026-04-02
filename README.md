[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cDnlIYNC)

# P1: Data Detective

## Summary
This project analyzes a text file, counts word frequencies, shows the top N words, and reports one extra insight. It focuses on text processing using Python functions and standard data structures.

## Dataset
- File: `data/sample.txt`
- Why I chose it: I used *The Memoirs of Sherlock Holmes* by Arthur Conan Doyle because it is a public-domain book with rich vocabulary and repeated words, which is useful for testing word frequency analysis.

## How to run
```bash
pytest -q
python -m src.project
```

## Approach
- Load text from a file
- Normalize the text (convert to lowercase and remove punctuation)
- Tokenize into words
- Count word frequencies using a dictionary
- Show the top N most frequent words
- Report one extra insight (words that appear only once)

## Complexity
### `count_words`
- Time: O(n)
- Space: O(n)
- Why: Each word is processed once and stored in a dictionary.

### `top_n_words`
- Time: O(n log n)
- Space: O(n)
- Why: Sorting the word-frequency pairs takes O(n log n) time.

## Edge-case checklist
- [x] empty file → returns empty results safely
- [x] punctuation-heavy input → punctuation removed during normalization
- [x] repeated words → counted correctly
- [x] uppercase/lowercase differences → normalized to lowercase
- [x] `n <= 0` → returns an empty list

## Assistance & sources
- AI used? Yes
- What it helped with: Understanding the structure, debugging code, writing tests, and improving README clarity
- Other sources: Python documentation

## Design note (150–250 words)
For this project, I used *The Memoirs of Sherlock Holmes* as my dataset because it provides a large and meaningful collection of text for analysis. The repeated use of certain words and varied vocabulary make it suitable for testing word frequency functions.

I designed the program using small and modular functions, where each function performs one specific task such as loading text, normalizing it, tokenizing, or counting words. This approach improves readability and makes testing easier. One important design decision was to normalize the text before tokenization so that words like "The" and "the" are treated the same. Removing punctuation also helps avoid incorrect word splitting.

The easiest part of the project was implementing the word counting using a dictionary. The most challenging part was handling edge cases, especially ensuring the program behaves correctly with empty input or unusual text formats.

If I were to improve this project, I would optimize the top-N function using a more efficient method like a heap for large datasets. I would also add more advanced insights, such as analyzing word lengths or visualizing the results.
