# File Name : graphicfunction.py
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



import matplotlib.pyplot as plt
import seaborn as sns

def plot_word_length_distribution(word_lengths):
    """Creates a histogram of word lengths."""
    plt.figure(figsize=(10, 6))
    sns.histplot(word_lengths, bins=range(1, max(word_lengths)+1), kde=False, color='skyblue')
    plt.title("Distribution of Word Lengths in Text")
    plt.xlabel("Word Length")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
