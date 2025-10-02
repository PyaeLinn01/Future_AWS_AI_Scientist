#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25                                
# REVISED DATE: 
# PURPOSE: Adjusts results_dic to indicate whether labels are of-a-dog or not.
##

def adjust_results4_isadog(results_dic, dogfile):
    """
    Determines whether images are correctly classified as dogs or not dogs.
    
    This function extends the results dictionary by adding flags that indicate:
    1. Whether the true pet label represents a dog breed
    2. Whether the classifier label represents a dog breed
    
    These flags enable evaluation of the classifier's ability to distinguish
    dogs from non-dogs, independent of breed identification accuracy.
    
    Process:
      1. Load valid dog breed names from the dogfile into a dictionary
      2. For each image result:
         - Check if pet label is in the dog names dictionary
         - Check if any term in classifier label is in the dog names dictionary
         - Extend results with is-a-dog flags
    
    Parameters:
      results_dic (dict) - Results dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = label match indicator (int: 1/0)
                          EXTENDED BY THIS FUNCTION:
                            index 3 = pet is-a-dog flag (int: 1=dog, 0=not dog)
                            index 4 = classifier is-a-dog flag (int: 1=dog, 0=not dog)
      dogfile (str) - Path to text file containing valid dog breed names
                     (one breed name per line, lowercase format)
    
    Returns:
      None - Modifies results_dic in place (mutable data type)
      
    Example:
      If pet_label='beagle' and dogfile contains 'beagle', then pet_is_dog=1
      If classifier_label='cat, feline' and neither is in dogfile, then classifier_is_dog=0
    """
    # Step 1: Load valid dog breed names from file into dictionary
    dognames_dic = {}
    with open(dogfile, "r") as infile:
        for line in infile:
            breed_name = line.strip()
            # Add non-empty breed names to dictionary
            if breed_name and breed_name not in dognames_dic:
                dognames_dic[breed_name] = 1

    # Step 2: Process each image result and add is-a-dog flags
    for filename, result_list in results_dic.items():
        # Extract labels from results list
        pet_label = result_list[0]
        classifier_label = result_list[1]

        # Step 3: Check if pet label is a dog breed
        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # Step 4: Check if classifier label contains any dog breed
        # Classifier may return multiple terms separated by commas
        classifier_is_dog = 0
        classifier_terms = classifier_label.split(",")
        for term in classifier_terms:
            if term.strip() in dognames_dic:
                classifier_is_dog = 1
                break  # Found a dog breed, no need to check further

        # Step 5: Extend results list with is-a-dog flags
        results_dic[filename].extend([pet_is_dog, classifier_is_dog])
