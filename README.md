# BinaryTextCorrection

ScrambleSolver is a Python project developed as part of the PRG550 Winter 2024 assignment, authored by Fatih Emre Başer. It decodes scrambled text while preserving readability by using a binary search on an English dictionary to match words based on given rules. This program efficiently handles word unscrambling by identifying and correcting scrambled words.

## Project Description
This program follows a principle of human reading comprehension that allows people to read scrambled text if the first and last letters of each word remain in place. ScrambleSolver corrects scrambled text based on this principle, identifying correct dictionary words and reconstructing the text with proper spelling.

Key features:
- Binary search-based dictionary lookup
- Retains original punctuation and capitalization
- Uses string manipulation and list operations for efficient text reconstruction

## Installation
1. Clone this repository.
2. Ensure `dictionary.txt` (containing 370,032 lowercase English words) is present in the project directory. The dictionary is essential for accurate word corrections.

## Usage
To use ScrambleSolver:
1. Load the dictionary using the `load_dictionary()` function.
2. Call `clean_up_words()` to correct scrambled text. The program will output both the original and corrected text, demonstrating the unscrambled version.

