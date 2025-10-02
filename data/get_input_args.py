#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Pyae Linn
# DATE CREATED: 30/09/25                                  
# REVISED DATE: 
# PURPOSE: Retrieves 3 command line inputs from user using argparse.
#          If user doesn’t provide inputs, defaults are used:
#            1. --dir with default value 'pet_images/'
#            2. --arch with default value 'vgg'
#            3. --dogfile with default value 'dognames.txt'
#
##
import argparse

def get_input_args():
    """
    Retrieves and parses 3 command line arguments from user for dog image classification.
    
    This function uses argparse to handle command line arguments with sensible defaults.
    The arguments control which images to classify, which CNN model to use, and which
    dog names file to reference for validation.
    
    Command Line Arguments:
      --dir     : Path to folder containing pet images (default: 'pet_images/')
      --arch    : CNN model architecture to use (default: 'vgg')
                  Valid options: 'resnet', 'alexnet', 'vgg'
      --dogfile : Text file with valid dog breed names (default: 'dognames.txt')
    
    Returns:
      argparse.Namespace - Object containing parsed command line arguments with attributes:
                          .dir (str), .arch (str), .dogfile (str)
    
    Example Usage:
      python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
    """
    # Create ArgumentParser object with description
    parser = argparse.ArgumentParser(
        description='Classify pet images using CNN models and evaluate performance'
    )

    # Argument 1: Image directory path
    parser.add_argument(
        '--dir', 
        type=str, 
        default='pet_images/',
        help='Path to folder of images to classify'
    )

    # Argument 2: CNN model architecture
    parser.add_argument(
        '--arch', 
        type=str, 
        default='vgg',
        choices=['resnet', 'alexnet', 'vgg'],
        help='CNN model architecture: resnet, alexnet, or vgg (default: vgg)'
    )

    # Argument 3: Dog names file
    parser.add_argument(
        '--dogfile', 
        type=str, 
        default='dognames.txt',
        help='Text file containing valid dog breed names (one per line)'
    )

    # Parse and return arguments
    return parser.parse_args()
