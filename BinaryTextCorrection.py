# program: A1functions
# author:  Fatih Emre Başer
# date:    february 20, 2024
# purpose: python main( ) program for PRG550 Winter 2024 Assignment #1
# version: 1.00


def load_dictionary(file_name) :
   try:
        with open (file_name) as file:
            lines = [line.strip() for line in file]
            return lines
   except FileNotFoundError :                             
        print(f"File '{file_name}' not found.")
        return


def clean_up_words(dictionary, text):
    lines = text.split('\n')  # Split the text by new lines to preserve them in the corrected version
    corrected_lines = []
    for line in lines:
        words = line.split()  # Split line into words
        corrected_line = ""
        for word in words:
            punctuation = ""                # Separate punctuation from the end if it exists
            if not word[-1].isalpha():
                punctuation = word[-1]
                word = word[:-1]

            if word.isalpha():  # Check if the word is alphabetic
                is_capitalized = word[0].isupper()  # Check if the word is capitalized
                word_lower = word.lower()
                if word_lower not in dictionary:  # Attempt to find the most similar word in the dictionary
                    similar_words = [
                        obj for obj in dictionary 
                        if len(obj) == len(word) and obj[0].lower() == word_lower[0] and obj[-1].lower() == word_lower[-1]
                    ]
                    if similar_words:                           # Find the word with the most matching characters
                        best_match = None
                        max_match = -1
                        for obj in similar_words:
                            match_count = sum(1 for ch in obj if ch in word_lower)
                            if match_count > max_match:
                                max_match = match_count
                                best_match = obj
                        
                        best_match_corrected = best_match.capitalize() if is_capitalized else best_match                         # Capitalize the matched word if the original word was capitalized
                        corrected_line += best_match_corrected
                    else:
                        corrected_line += word
                else:
                    corrected_line += word
            else:
                corrected_line += word  # Add punctuation marks
                
            corrected_line += " "  # Add a space after each word
        corrected_lines.append(corrected_line.strip())
    return text, '\n'.join(corrected_lines).strip()

