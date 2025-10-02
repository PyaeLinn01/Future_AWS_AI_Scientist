#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Pyae Linn                                                    
# DATE CREATED: 30/09/25                                  
# REVISED DATE:                         
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"
#
def check_command_line_arguments(in_arg):
    """
    Validates and displays command line arguments for the image classification program.
    
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each command line argument to verify they were parsed correctly.
    Assumes all three required arguments (dir, arch, dogfile) are defined.
    
    Parameters:
      in_arg (argparse.Namespace) - Object containing command line arguments with
                                   attributes: .dir, .arch, .dogfile
    Returns:
      None - Prints to console
    """
    if in_arg is None:
        print("* Cannot check Command Line Arguments - 'get_input_args' not defined.")
    else:
        # Print command line arguments with improved formatting
        print("\n" + "="*50)
        print("Command Line Arguments:")
        print("="*50)
        print(f"  Image Directory:  {in_arg.dir}")
        print(f"  CNN Architecture: {in_arg.arch}")
        print(f"  Dog Names File:   {in_arg.dogfile}")
        print("="*50)

def check_creating_pet_image_labels(results_dic):
    """
    Validates pet image label extraction from filenames.
    
    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Displays the first 10 key-value pairs from the results dictionary and
    verifies the total count matches expected number of images.
    
    Parameters:
      results_dic (dict) - Dictionary with structure:
                          Key: image filename (str)
                          Value: list containing [pet_label (str)] at index 0
    Returns:
      None - Prints to console
    """
    if results_dic is None:
        print("* Cannot check Results Dictionary - 'get_pet_labels' not defined.")
    else:
        # Determine how many entries to display (max 10)
        total_images = len(results_dic)
        display_count = min(total_images, 10)
        
        print("\n" + "="*70)
        print(f"Pet Image Label Dictionary: {total_images} key-value pairs")
        print(f"Displaying first {display_count} entries:")
        print("="*70)
    
        # Display first N entries
        for idx, (filename, label_list) in enumerate(results_dic.items(), 1):
            if idx <= display_count:
                print(f"{idx:2d}. {filename:>35} -> {label_list[0]:>26}")
            else:
                break
        print("="*70)


def check_classifying_images(results_dic):
    """
    Validates image classification results by comparing pet labels with classifier labels.
    
    For Lab: Classifying Images - 11/12. Classifying Images
    Displays all matching and non-matching classifications, then shows summary counts
    to verify all images were processed correctly.
    
    Parameters:
      results_dic (dict) - Dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = match indicator (int: 1=match, 0=no match)
    Returns:
      None - Prints to console
    """
    if results_dic is None:
        print("* Cannot check Results Dictionary - 'classify_images' not defined.")
    elif len(results_dic[next(iter(results_dic))]) < 2:
        print("* Cannot check Results Dictionary - 'classify_images' not defined.")
    else:
        # Initialize counters
        n_match = 0
        n_notmatch = 0
    
        # Display all matches
        print("\n" + "="*70)
        print("MATCHES (Pet Label == Classifier Label):")
        print("="*70)
        for filename, values in results_dic.items():
            if values[2] == 1:
                n_match += 1
                print(f"\n{filename:>35}:")
                print(f"  Pet Label:        {values[0]:>26}")
                print(f"  Classifier Label: {values[1]:>26}")

        # Display all non-matches
        print("\n" + "="*70)
        print("NOT MATCHES (Pet Label != Classifier Label):")
        print("="*70)
        for filename, values in results_dic.items():
            if values[2] == 0:
                n_notmatch += 1
                print(f"\n{filename:>35}:")
                print(f"  Pet Label:        {values[0]:>26}")
                print(f"  Classifier Label: {values[1]:>26}")

        # Display summary
        print("\n" + "="*70)
        print(f"Total Images: {n_match + n_notmatch} | Matches: {n_match} | Not Matches: {n_notmatch}")
        print("="*70)

 
def check_classifying_labels_as_dogs(results_dic):
    """
    Validates dog classification results showing whether labels are correctly identified as dogs.
    
    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Displays pet label, classifier label, and dog classification flags (is-a-dog indicators)
    for all matches and non-matches to verify dog detection accuracy.
    
    Parameters:
      results_dic (dict) - Dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = match indicator (int: 1=match, 0=no match)
                            index 3 = pet is-a-dog (int: 1=dog, 0=not dog)
                            index 4 = classifier is-a-dog (int: 1=dog, 0=not dog)
    Returns:
      None - Prints to console
    """
    if results_dic is None:
        print("* Cannot check Results Dictionary - 'adjust_results4_isadog' not defined.")
    elif len(results_dic[next(iter(results_dic))]) < 4:
        print("* Cannot check Results Dictionary - 'adjust_results4_isadog' not defined.")
    else:
        # Initialize counters
        n_match = 0
        n_notmatch = 0
    
        # Display all matches with dog classification flags
        print("\n" + "="*70)
        print("MATCHES (Pet Label == Classifier Label):")
        print("="*70)
        for filename, values in results_dic.items():
            if values[2] == 1:
                n_match += 1
                print(f"\n{filename:>35}:")
                print(f"  Pet Label:        {values[0]:>26}")
                print(f"  Classifier Label: {values[1]:>26}")
                print(f"  Pet is Dog: {values[3]}  |  Classifier is Dog: {values[4]}")

        # Display all non-matches with dog classification flags
        print("\n" + "="*70)
        print("NOT MATCHES (Pet Label != Classifier Label):")
        print("="*70)
        for filename, values in results_dic.items():
            if values[2] == 0:
                n_notmatch += 1
                print(f"\n{filename:>35}:")
                print(f"  Pet Label:        {values[0]:>26}")
                print(f"  Classifier Label: {values[1]:>26}")
                print(f"  Pet is Dog: {values[3]}  |  Classifier is Dog: {values[4]}")

        # Display summary
        print("\n" + "="*70)
        print(f"Total Images: {n_match + n_notmatch} | Matches: {n_match} | Not Matches: {n_notmatch}")
        print("="*70)



def check_calculating_results(results_dic, results_stats_dic):
    """
    Validates statistics calculations by comparing function output with manual calculations.
    
    For Lab: Classifying Images - 14. Calculating Results
    Displays statistics from the calculates_results_stats() function and compares
    them with independently calculated values to verify correctness.
    
    Parameters:
      results_dic (dict) - Dictionary with structure:
                          Key: image filename (str)
                          Value: list containing:
                            index 0 = pet image label (str)
                            index 1 = classifier label (str)
                            index 2 = match indicator (int: 1=match, 0=no match)
                            index 3 = pet is-a-dog (int: 1=dog, 0=not dog)
                            index 4 = classifier is-a-dog (int: 1=dog, 0=not dog)
      results_stats_dic (dict) - Statistics dictionary containing counts (n_*) and
                                percentages (pct_*) calculated by calculates_results_stats()
    Returns:
      None - Prints to console
    """
    if results_stats_dic is None:
        print("* Cannot check Results Dictionary - 'calculates_results_stats' not defined.")
    else:
        # Recalculate statistics independently to verify calculates_results_stats()
        # Initialize counters
        n_images = len(results_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_match_breed = 0
    
        # Iterate through results dictionary to compute statistics
        for filename, values in results_dic.items():
            labels_match = values[2]
            pet_is_dog = values[3]
            classifier_is_dog = values[4]

            # Count dog images
            if pet_is_dog == 1:
                n_pet_dog += 1
                
                # Count correct dog classifications
                if classifier_is_dog == 1:
                    n_class_cdog += 1
                    
                    # Count correct breed matches (both are dogs AND labels match)
                    if labels_match == 1:
                        n_match_breed += 1
            
            # Count non-dog images
            else:
                # Count correct non-dog classifications
                if classifier_is_dog == 0:
                    n_class_cnotd += 1
                    
        # Calculate derived statistics
        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = (n_class_cdog / n_pet_dog) * 100 if n_pet_dog > 0 else 0
        pct_corr_notdog = (n_class_cnotd / n_pet_notd) * 100 if n_pet_notd > 0 else 0
        pct_corr_breed = (n_match_breed / n_pet_dog) * 100 if n_pet_dog > 0 else 0
    
        # Display comparison of statistics
        print("\n" + "="*70)
        print("** Statistics from calculates_results_stats() function:")
        print("="*70)
        print(f"N Images: {results_stats_dic['n_images']:2d}  |  "
              f"N Dog Images: {results_stats_dic['n_dogs_img']:2d}  |  "
              f"N NotDog Images: {results_stats_dic['n_notdogs_img']:2d}")
        print(f"Pct Correct Dog: {results_stats_dic['pct_correct_dogs']:5.1f}%  |  "
              f"Pct Correct NOTdog: {results_stats_dic['pct_correct_notdogs']:5.1f}%  |  "
              f"Pct Correct Breed: {results_stats_dic['pct_correct_breed']:5.1f}%")
        
        print("\n" + "="*70)
        print("** Check Statistics (calculated independently for verification):")
        print("="*70)
        print(f"N Images: {n_images:2d}  |  "
              f"N Dog Images: {n_pet_dog:2d}  |  "
              f"N NotDog Images: {n_pet_notd:2d}")
        print(f"Pct Correct Dog: {pct_corr_dog:5.1f}%  |  "
              f"Pct Correct NOTdog: {pct_corr_notdog:5.1f}%  |  "
              f"Pct Correct Breed: {pct_corr_breed:5.1f}%")
        print("="*70)
