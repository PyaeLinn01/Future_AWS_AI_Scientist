#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25                             
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels extracted from image filenames.
    
    This function parses image filenames to extract the true pet breed labels,
    which serve as ground truth for evaluating classifier performance. The function
    handles various filename formats and normalizes labels to lowercase.
    
    Filename Format:
      Expected format: 'breed_name_number.extension'
      Example: 'Boston_terrier_02259.jpg' -> 'boston terrier'
      
    Processing Steps:
      1. List all files in the specified directory
      2. Skip hidden files (starting with '.')
      3. Remove file extensions
      4. Extract alphabetic words (breed names) from filename
      5. Convert to lowercase and normalize spacing
      6. Store in dictionary with filename as key
    
    Parameters:
      image_dir (str) - Full or relative path to folder containing pet images
    
    Returns:
      dict - Dictionary with structure:
             Key: image filename (str)
             Value: list containing [pet_label (str)] at index 0
             
    Example:
      >>> get_pet_labels('pet_images/')
      {'Boston_terrier_02259.jpg': ['boston terrier'],
       'Collie_03797.jpg': ['collie']}
    """
    # Get list of files in directory
    in_files = listdir(image_dir)
    
    # Create empty dictionary for results
    results_dic = {}
   
    # Process each file in the directory
    for filename in in_files:
        # Skip hidden files (starting with '.')
        if filename[0] != ".":
            # Remove file extension (e.g., .jpg, .png)
            name_without_ext = filename.rsplit('.', 1)[0]
            
            # Split by underscores and filter only alphabetic words (breed names)
            name_parts = name_without_ext.split('_')
            alphabetic_words = [word for word in name_parts if word.isalpha()]
            
            # Join words with spaces, convert to lowercase, and strip whitespace
            pet_label = " ".join(alphabetic_words).lower().strip()
            
            # Add to dictionary if not already present
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                # Warn about duplicate filenames
                print(f"** Warning: Duplicate file detected: {filename}")
                
    # Return the results dictionary
    return results_dic

