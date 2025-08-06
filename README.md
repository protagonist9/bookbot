# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# Bookbot

Bookbot is a command-line tool written in Python for analyzing the content of books in plain text format. It can count words, tally character frequencies, and give you a quick textual overview of any `.txt` book file.

## Features

- Counts total words in a book
- Calculates the count of each character (letters only)
- Displays results in a user-friendly format

## Usage

1. Place your book `.txt` files in a directory, such as `books`.
2. Run Bookbot from the command line with:
    ```
    python3 main.py <path_to_book>
    ```
    Example:
    ```
    python3 main.py books/frankenstein.txt
    ```

## Requirements

- Python 3.x
