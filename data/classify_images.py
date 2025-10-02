#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images using CNN model and compares results with true labels.
    
    This function processes each image in the results dictionary by:
    1. Running the image through the specified CNN classifier
    2. Normalizing the classifier output to match pet label format
    3. Comparing classifier label with the true pet label
    4. Extending the results dictionary with classification results
    
    Label Matching:
      - Classifier may return multiple breed names separated by commas
      - Example: 'Maltese dog, Maltese terrier, Maltese'
      - A match occurs if the pet label appears in any of the classifier terms
      - Example: pet label 'dalmatian' matches classifier 'dalmatian, coach dog, carriage dog'
    
    Parameters:
      images_dir (str) - Full path to folder containing images to classify
                        (must include trailing slash)
      results_dic (dict) - Results dictionary with structure:
                          Key: image filename (str)
                          Value: list where:
                            index 0 = pet image label (str)
                          EXTENDED BY THIS FUNCTION:
                            index 1 = classifier label (str)
                            index 2 = match indicator (int: 1=match, 0=no match)
      model (str) - CNN model architecture to use for classification
                   Valid values: 'resnet', 'alexnet', 'vgg'
    
    Returns:
      None - Modifies results_dic in place (mutable data type)
      
    Note:
      This function uses the classifier() function from classifier.py.
      See test_classifier.py for proper usage examples.
    """
    # Process each image in the results dictionary
    for filename in results_dic:
        # Step 1: Run CNN classifier on image
        # Construct full image path and get classifier prediction
        full_image_path = images_dir + filename
        classifier_label = classifier(full_image_path, model)

        # Step 2: Normalize classifier label (lowercase and strip whitespace)
        classifier_label = classifier_label.lower().strip()

        # Step 3: Get the true pet label from results dictionary
        pet_label = results_dic[filename][0]

        # Step 4: Parse classifier label into individual terms
        # Classifier may return multiple breed names separated by commas
        classifier_terms = [term.strip() for term in classifier_label.split(",")]

        # Step 5: Compare pet label with classifier terms
        # Match = 1 if pet label found in any classifier term, otherwise 0
        is_match = 1 if pet_label in classifier_terms else 0

        # Step 6: Extend results dictionary with classifier results
        # Adds [classifier_label, is_match] to the existing list
        results_dic[filename].extend([classifier_label, is_match]) 