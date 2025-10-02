#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates comprehensive statistics for image classification results.
    
    This function analyzes the classification results to compute counts and percentages
    that help evaluate CNN model performance. Statistics include overall accuracy,
    dog detection accuracy, breed identification accuracy, and non-dog classification accuracy.
    
    Calculated Statistics:
      Counts (prefix 'n_'):
        - n_images: Total number of images processed
        - n_dogs_img: Number of images that are actually dogs
        - n_notdogs_img: Number of images that are not dogs
        - n_match: Number of exact label matches (pet label == classifier label)
        - n_correct_dogs: Number of correctly identified dogs (regardless of breed)
        - n_correct_notdogs: Number of correctly identified non-dogs
        - n_correct_breed: Number of correctly identified dog breeds
      
      Percentages (prefix 'pct_'):
        - pct_match: Percentage of exact label matches
        - pct_correct_dogs: Percentage of correctly classified dogs
        - pct_correct_breed: Percentage of correctly classified breeds (among dogs)
        - pct_correct_notdogs: Percentage of correctly classified non-dogs
    
    Parameters:
      results_dic (dict) - Results dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = label match (int: 1=match, 0=no match)
                            index 3 = pet is-a-dog (int: 1=dog, 0=not dog)
                            index 4 = classifier is-a-dog (int: 1=dog, 0=not dog)
    
    Returns:
      dict - Statistics dictionary with keys as statistic names and values as
             counts (int) or percentages (float). All percentages are in range [0, 100].
             
    Example:
      >>> stats = calculates_results_stats(results)
      >>> print(f"Dog detection accuracy: {stats['pct_correct_dogs']:.1f}%")
      Dog detection accuracy: 95.5%
    """    
    # Initialize the results statistics dictionary with counters
    results_stats_dic = {
        'n_dogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }
    
    # Process each image result and accumulate counts
    for filename, result_list in results_dic.items():
        # Extract values from result list for readability
        pet_label = result_list[0]
        classifier_label = result_list[1]
        labels_match = result_list[2]
        pet_is_dog = result_list[3]
        classifier_is_dog = result_list[4]
        
        # Count exact label matches
        if labels_match == 1:
            results_stats_dic['n_match'] += 1
        
        # Process dog images
        if pet_is_dog == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # Count correct breed identification (both are dogs AND labels match)
            if labels_match == 1:
                results_stats_dic['n_correct_breed'] += 1
            
            # Count correct dog detection (classifier also says it's a dog)
            if classifier_is_dog == 1:
                results_stats_dic['n_correct_dogs'] += 1
        
        # Process non-dog images
        else:
            # Count correct non-dog classification (classifier also says not a dog)
            if classifier_is_dog == 0:
                results_stats_dic['n_correct_notdogs'] += 1
    
    # Calculate derived counts
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (
        results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    )
    
    # Calculate percentages with division by zero protection
    
    # Overall match percentage
    results_stats_dic['pct_match'] = (
        (results_stats_dic['n_match'] / results_stats_dic['n_images'] * 100.0)
        if results_stats_dic['n_images'] > 0 else 0.0
    )
    
    # Dog detection accuracy percentage
    results_stats_dic['pct_correct_dogs'] = (
        (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'] * 100.0)
        if results_stats_dic['n_dogs_img'] > 0 else 0.0
    )
    
    # Breed identification accuracy percentage (among dog images)
    results_stats_dic['pct_correct_breed'] = (
        (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img'] * 100.0)
        if results_stats_dic['n_dogs_img'] > 0 else 0.0
    )
    
    # Non-dog classification accuracy percentage
    results_stats_dic['pct_correct_notdogs'] = (
        (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'] * 100.0)
        if results_stats_dic['n_notdogs_img'] > 0 else 0.0
    )
    
    # Return the completed statistics dictionary
    return results_stats_dic    
    