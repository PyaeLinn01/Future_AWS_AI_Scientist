#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/test_classifier.py
#                                                                             
# PROGRAMMER: Pyae Linn                                                    
# DATE CREATED: 30/09/25                                  
# REVISED DATE:                         
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. See the example
#          usage below.
#
# Usage: python test_classifier.py    -- will run program from commandline

# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier 

# Define test image path from pet_images folder
test_image = "pet_images/Collie_03797.jpg"

# Define CNN model architecture for classification
# NOTE: Only the following model architectures are supported:
#       'vgg', 'alexnet', 'resnet'
model = "vgg"

# Run classifier function to classify the test image
# NOTE: image_classification is a text string containing mixed case labels
#       Multiple labels may be separated by commas when an image can be
#       described by more than one term (e.g., 'Collie, Border Collie')
image_classification = classifier(test_image, model)

# Print classification results
print("\n" + "="*70)
print("Results from test_classifier.py")
print("="*70)
print(f"Image:      {test_image}")
print(f"Model:      {model.upper()}")
print(f"Classified: {image_classification}")
print("="*70)
