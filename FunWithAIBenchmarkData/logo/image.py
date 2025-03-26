# File Name : image.py
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



import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_logo():
    """Displays the logo image."""
    img_path = os.path.join("logoImage", "logoImage.jpg")
    if os.path.exists(img_path):
        img = mpimg.imread(img_path)
        plt.figure(figsize=(4, 4))
        plt.imshow(img)
        plt.axis('off')
        plt.title("Project Logo", fontsize=14)
        plt.show()
    else:
        print("Logo image not found.")




