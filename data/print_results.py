#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints comprehensive classification results and optional error analysis.
    
    This function displays:
    1. Summary statistics for the CNN model's performance
    2. Counts of images processed (total, dogs, non-dogs)
    3. Accuracy percentages for various classification tasks
    4. Optional: Incorrectly classified dogs (dog vs non-dog errors)
    5. Optional: Incorrectly classified breeds (breed identification errors)
    
    The summary helps determine which CNN model performs best for:
    - Overall accuracy (pct_match)
    - Dog detection (pct_correct_dogs)
    - Breed identification (pct_correct_breed)
    - Non-dog classification (pct_correct_notdogs)
    
    Parameters:
      results_dic (dict) - Results dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = label match (int: 1=match, 0=no match)
                            index 3 = pet is-a-dog (int: 1=dog, 0=not dog)
                            index 4 = classifier is-a-dog (int: 1=dog, 0=not dog)
      results_stats_dic (dict) - Statistics dictionary containing counts (n_*) 
                                and percentages (pct_*) of classification results
      model (str) - CNN model architecture used ('resnet', 'alexnet', or 'vgg')
      print_incorrect_dogs (bool) - If True, prints images where dog/non-dog 
                                   classification was incorrect (default: False)
      print_incorrect_breed (bool) - If True, prints dog images where breed 
                                    was incorrectly identified (default: False)
    
    Returns:
      None - Prints results to console
      
    Example Output:
      *** Results Summary for VGG CNN Model ***
      Number of Images:              40
      Number of Dog Images:          30
      Number of Not-Dog Images:      10
      
      Percentage of Correct Dogs:    100.0%
      Percentage of Correct Breed:    93.3%
      ...
    """    
    # Print header with model name
    print("\n" + "="*70)
    print(f"*** Results Summary for {model.upper()} CNN Model ***")
    print("="*70)
    
    # Print image counts
    print("\n--- Image Counts ---")
    print(f"{'Total Images Processed:':<35} {results_stats_dic['n_images']:>5}")
    print(f"{'Dog Images:':<35} {results_stats_dic['n_dogs_img']:>5}")
    print(f"{'Non-Dog Images:':<35} {results_stats_dic['n_notdogs_img']:>5}")
    
    # Print accuracy percentages
    print("\n--- Classification Accuracy ---")
    print(f"{'Overall Match Accuracy:':<35} {results_stats_dic['pct_match']:>6.1f}%")
    print(f"{'Dog Detection Accuracy:':<35} {results_stats_dic['pct_correct_dogs']:>6.1f}%")
    print(f"{'Breed Identification Accuracy:':<35} {results_stats_dic['pct_correct_breed']:>6.1f}%")
    print(f"{'Non-Dog Classification Accuracy:':<35} {results_stats_dic['pct_correct_notdogs']:>6.1f}%")
    print("="*70)
    
    # Print incorrectly classified dogs if requested
    if print_incorrect_dogs:
        print("\n" + "="*70)
        print("*** INCORRECTLY CLASSIFIED DOGS (Dog vs Non-Dog Errors) ***")
        print("="*70)
        incorrect_dog_count = 0
        
        for filename, values in results_dic.items():
            pet_is_dog = values[3]
            classifier_is_dog = values[4]
            
            # Check for dog/non-dog classification errors
            if (pet_is_dog == 1 and classifier_is_dog == 0) or \
               (pet_is_dog == 0 and classifier_is_dog == 1):
                incorrect_dog_count += 1
                pet_label = values[0]
                classifier_label = values[1]
                
                # Determine error type
                error_type = "FALSE NEGATIVE" if pet_is_dog == 1 else "FALSE POSITIVE"
                
                print(f"\n{incorrect_dog_count}. {filename}")
                print(f"   Error Type:       {error_type}")
                print(f"   True Label:       {pet_label}")
                print(f"   Classifier Label: {classifier_label}")
        
        if incorrect_dog_count == 0:
            print("\n✓ No dog/non-dog classification errors found!")
        else:
            print(f"\nTotal Errors: {incorrect_dog_count}")
        print("="*70)
    
    # Print incorrectly classified breeds if requested
    if print_incorrect_breed:
        print("\n" + "="*70)
        print("*** INCORRECTLY CLASSIFIED BREEDS (Breed Identification Errors) ***")
        print("="*70)
        incorrect_breed_count = 0
        
        for filename, values in results_dic.items():
            pet_is_dog = values[3]
            classifier_is_dog = values[4]
            labels_match = values[2]
            
            # Check for breed misidentification (both are dogs but breed is wrong)
            if pet_is_dog == 1 and classifier_is_dog == 1 and labels_match == 0:
                incorrect_breed_count += 1
                pet_label = values[0]
                classifier_label = values[1]
                
                print(f"\n{incorrect_breed_count}. {filename}")
                print(f"   True Breed:       {pet_label}")
                print(f"   Predicted Breed:  {classifier_label}")
        
        if incorrect_breed_count == 0:
            print("\n✓ No breed identification errors found!")
        else:
            print(f"\nTotal Breed Errors: {incorrect_breed_count}")
        print("="*70)
                
