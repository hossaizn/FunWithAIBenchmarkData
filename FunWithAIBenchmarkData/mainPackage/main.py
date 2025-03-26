# File Name : main.py
# Student Name: Zulqarnayan Hossain, Vishwaja Painjane, Leah Radcliffe
# email:  hossaizn@mail.uc.edu, painjavv@mail.uc.edu, radclilr@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   March 27, 2025
# Course #/Section:   IS 4010 Section 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  We produce visualization using the data in this project as well as produce the team logo as an output.

# Brief Description of what this module does. We work with python packages and environments to create visualizations.
# Citations: We used ChatGPT 40 model for this assignment.

# Anything else that's relevant: N/A

# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import random
import pandas as pd
import matplotlib.pyplot as plt

from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *

from visualization.graphicfunction import plot_word_length_distribution
from logo.image import display_logo


def find_longest_word(text):
    """Finds the longest word in a given string."""
    words = text.split()
    return max(words, key=len)

def find_shortest_word(text):
    """Finds the shortest word in a given string (excluding 1-letter noise)."""
    words = [word for word in text.split() if len(word) > 1]
    return min(words, key=len)

def compute_word_lengths(text):
    """Returns a list of lengths of all words in the text."""
    words = text.split()
    return [len(word) for word in words if word.isalpha()]


if __name__ == "__main__":
    # Step 1: Read CSV files
    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv", "college_medicine_test.csv"])
    questions = CSV_Processor.read_data()

    # Step 2: Convert all prompts and answers to one big string
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])

    # Step 3: Extract and print longest and shortest words
    longest = find_longest_word(text)
    shortest = find_shortest_word(text)

    #print("Longest word:", longest, "| Length:", len(longest))
    #print("Shortest word:", shortest, "| Length:", len(shortest))

    # Step 4: Calculate word lengths and visualize
    word_lengths = compute_word_lengths(text)
    display_logo()
    plot_word_length_distribution(word_lengths)

    """
    # Optional: Write questions to files (still works)
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
    """