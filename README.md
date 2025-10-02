# Dog Image Classification with CNN Models

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Latest-red.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

A comprehensive machine learning project that evaluates and compares three pre-trained CNN (Convolutional Neural Network) architectures for dog breed classification and dog detection tasks.

## 📋 Project Overview

This repository demonstrates practical application of deep learning for image classification by:

1. **Comparing CNN Architectures** - Evaluating ResNet, AlexNet, and VGG models
2. **Dog vs Non-Dog Classification** - Determining which model best identifies dogs
3. **Breed Identification** - Assessing accuracy in identifying specific dog breeds
4. **Performance Analysis** - Measuring the accuracy-runtime trade-off for each model

### Key Questions Answered

- Which CNN architecture provides the best accuracy for dog detection?
- How well can these models identify specific dog breeds?
- What is the computational cost (runtime) of each model?
- What is the optimal balance between accuracy and speed?

## 🎯 Key Features

✅ **Multi-Model Comparison**: Test and compare ResNet, AlexNet, and VGG architectures  
✅ **Comprehensive Metrics**: Track dog detection, breed identification, and non-dog classification accuracy  
✅ **Error Analysis**: Detailed reporting of false positives, false negatives, and misclassifications  
✅ **Performance Profiling**: Runtime measurement and efficiency analysis  
✅ **Modular Architecture**: Clean, well-documented, and reusable code structure  
✅ **Command-Line Interface**: Flexible configuration via command-line arguments  
✅ **Validation Tools**: Built-in debugging and verification functions  

## 🏗️ Repository Structure

```
Future_AWS_AI_Scientist/
├── README.md                                    # This file
├── data/                                        # Main project directory
│   ├── check_images.py                         # Main orchestration script
│   ├── get_input_args.py                       # Command-line argument parser
│   ├── get_pet_labels.py                       # Label extraction from filenames
│   ├── classify_images.py                      # CNN classification module
│   ├── adjust_results4_isadog.py               # Dog validation logic
│   ├── calculates_results_stats.py             # Statistics computation
│   ├── print_results.py                        # Results display and formatting
│   ├── classifier.py                           # CNN classifier interface
│   ├── test_classifier.py                      # Classifier testing utility
│   ├── print_functions_for_lab_checks.py       # Validation functions
│   ├── dognames.txt                            # Dog breed database (133 breeds)
│   ├── pet_images/                             # Test image directory
│   ├── alexnet_pet-images.txt                  # AlexNet results
│   ├── resnet_pet-images.txt                   # ResNet results
│   ├── vgg_pet-images.txt                      # VGG results
│   └── run_models_batch.sh                     # Batch testing script
├── project-workspace-command-line-arguments/   # Lab workspace: CLI args
├── project-workspace-pet-image-labels/         # Lab workspace: Label extraction
├── project-workspace-classifying-images/       # Lab workspace: Classification
├── project-workspace-adjusting-results/        # Lab workspace: Dog validation
├── project-workspace-calculating-results/      # Lab workspace: Statistics
├── project-workspace-printing-results/         # Lab workspace: Output formatting
├── project-workspace-timing/                   # Lab workspace: Performance timing
├── project-workspace-classify-uploaded-images/ # Lab workspace: Custom images
└── project-workspace-final-results/            # Lab workspace: Final analysis
```

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.6 or higher
- **PyTorch**: Latest stable version
- **torchvision**: For pre-trained models
- **PIL/Pillow**: For image processing

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Future_AWS_AI_Scientist.git
cd Future_AWS_AI_Scientist/data

# Install dependencies
pip install torch torchvision pillow

# Or use requirements.txt if available
pip install -r requirements.txt
```

### Quick Start

```bash
# Run with default settings (VGG model)
python check_images.py

# Test with different models
python check_images.py --arch resnet
python check_images.py --arch alexnet

# Use custom image directory
python check_images.py --dir my_images/ --arch vgg
```

## 💻 Usage

### Command-Line Arguments

| Argument | Description | Default | Options |
|----------|-------------|---------|------|
| `--dir` | Path to image folder | `pet_images/` | Any valid directory |
| `--arch` | CNN model architecture | `vgg` | `vgg`, `alexnet`, `resnet` |
| `--dogfile` | Dog breed names file | `dognames.txt` | Any text file |

### Example Commands

```bash
# Compare all three models
python check_images.py --arch vgg
python check_images.py --arch alexnet
python check_images.py --arch resnet

# Test with custom dog breeds file
python check_images.py --dogfile my_dognames.txt

# Run batch tests on all models
bash run_models_batch.sh
```

### Testing the Classifier

```bash
# Test classifier with a single image
python test_classifier.py
```

## 📊 Results and Performance

### Sample Output

```
======================================================================
*** Results Summary for VGG CNN Model ***
======================================================================

--- Image Counts ---
Total Images Processed:                     40
Dog Images:                                 30
Non-Dog Images:                             10

--- Classification Accuracy ---
Overall Match Accuracy:                  87.5%
Dog Detection Accuracy:                 100.0%
Breed Identification Accuracy:           93.3%
Non-Dog Classification Accuracy:         90.0%
======================================================================

** Total Elapsed Runtime: 00:02:15
```

### Model Comparison Results

| Model | Dog Detection | Breed Accuracy | Non-Dog Accuracy | Avg Runtime |
|-------|---------------|----------------|------------------|----------|
| **VGG** | 100% | 93.3% | 90% | ~135s |
| **AlexNet** | 100% | 80% | 100% | ~3s |
| **ResNet** | 100% | 90% | 90% | ~25s |

### Key Insights

🏆 **Best Overall Accuracy**: VGG (93.3% breed identification)  
⚡ **Fastest Runtime**: AlexNet (~3 seconds)  
⚖️ **Best Balance**: ResNet (good accuracy, reasonable speed)  

**Recommendation**: 
- Use **VGG** when accuracy is critical and time is not a constraint
- Use **AlexNet** for real-time applications requiring fast inference
- Use **ResNet** for production systems needing balanced performance

## 🔧 Technical Architecture

### Processing Pipeline

```
1. Input Arguments → Parse CLI arguments (model, directory, dog file)
                  ↓
2. Label Extraction → Extract ground truth from filenames
                  ↓
3. Classification → Run images through CNN model
                  ↓
4. Normalization → Lowercase labels, handle multi-word breeds
                  ↓
5. Dog Validation → Check against dog breed database
                  ↓
6. Statistics → Calculate accuracy metrics
                  ↓
7. Results Display → Format and present results
```

### Core Data Structures

**Results Dictionary**:
```python
results_dic = {
    'Beagle_01141.jpg': [
        'beagle',              # [0] Pet label (ground truth)
        'beagle',              # [1] Classifier label
        1,                     # [2] Match (1=yes, 0=no)
        1,                     # [3] Pet is dog (1=yes, 0=no)
        1                      # [4] Classifier says dog (1=yes, 0=no)
    ]
}
```

**Statistics Dictionary**:
```python
stats_dic = {
    'n_images': 40,              # Total images
    'n_dogs_img': 30,            # Dog images
    'n_notdogs_img': 10,         # Non-dog images
    'n_correct_dogs': 30,        # Correct dog detections
    'n_correct_notdogs': 9,      # Correct non-dog classifications
    'n_correct_breed': 28,       # Correct breed identifications
    'pct_correct_dogs': 100.0,   # Dog detection accuracy %
    'pct_correct_breed': 93.3,   # Breed accuracy %
    'pct_correct_notdogs': 90.0  # Non-dog accuracy %
}
```

## 📚 Module Documentation

### Core Modules

#### `check_images.py`
Main orchestration script that coordinates the entire classification pipeline.

#### `get_input_args.py`
Parses and validates command-line arguments using argparse.

#### `get_pet_labels.py`
Extracts pet breed labels from image filenames.
- Handles underscores and numeric suffixes
- Normalizes to lowercase
- Filters alphabetic words only

#### `classify_images.py`
Interfaces with CNN models to classify images.
- Supports VGG, AlexNet, ResNet
- Handles comma-separated breed names
- Compares predictions with ground truth

#### `adjust_results4_isadog.py`
Validates whether labels represent dog breeds.
- Loads dog breed database
- Checks pet and classifier labels
- Adds is-a-dog flags to results

#### `calculates_results_stats.py`
Computes comprehensive performance statistics.
- Calculates counts and percentages
- Handles division by zero
- Returns formatted statistics dictionary

#### `print_results.py`
Formats and displays classification results.
- Summary statistics
- Optional error analysis
- False positive/negative reporting

### Support Modules

#### `classifier.py`
Pre-built interface to PyTorch CNN models.

#### `test_classifier.py`
Standalone testing utility for quick classifier verification.

#### `print_functions_for_lab_checks.py`
Debugging and validation functions for development.

## 🎓 Learning Outcomes

This project demonstrates:

### Python Skills
- ✅ Functions and modular programming
- ✅ Dictionaries and data structures
- ✅ File I/O operations
- ✅ Command-line argument parsing
- ✅ String manipulation and formatting

### Machine Learning Concepts
- ✅ Convolutional Neural Networks (CNNs)
- ✅ Transfer learning with pre-trained models
- ✅ Image classification pipelines
- ✅ Model evaluation metrics
- ✅ Accuracy vs. performance trade-offs

### Software Engineering
- ✅ Modular code design
- ✅ Documentation and docstrings
- ✅ Testing and validation
- ✅ Error handling
- ✅ Code organization

## 🐛 Troubleshooting

### Common Issues

**Problem**: `ModuleNotFoundError: No module named 'torch'`  
**Solution**: Install PyTorch
```bash
pip install torch torchvision
```

**Problem**: Images not found  
**Solution**: Verify image directory path
```bash
ls pet_images/  # Check if images exist
python check_images.py --dir pet_images/
```

**Problem**: Slow performance  
**Solution**: Use AlexNet for faster results
```bash
python check_images.py --arch alexnet
```

**Problem**: Out of memory errors  
**Solution**: Process fewer images or use a smaller model
```bash
python check_images.py --arch alexnet  # Smallest model
```

## 🔬 Advanced Usage

### Batch Testing All Models

```bash
# Run all three models and save results
bash run_models_batch.sh
```

### Custom Image Testing

1. Place your images in a directory
2. Name files with format: `breed_name_number.jpg`
3. Run classification:

```bash
python check_images.py --dir my_images/
```

### Adding New Dog Breeds

Edit `dognames.txt` and add breed names (one per line, lowercase):

```
beagle
golden retriever
german shepherd
your_new_breed
```

## 📈 Performance Optimization Tips

1. **For Speed**: Use AlexNet architecture
2. **For Accuracy**: Use VGG architecture
3. **For Balance**: Use ResNet architecture
4. **Batch Processing**: Use the batch script for multiple tests
5. **GPU Acceleration**: Ensure PyTorch uses CUDA if available

## 👤 Author

**Pyae Linn**  
Date: 30/09/25  
Project: AI Image Classification with CNN Models

## 📄 License

This project is part of an educational program focused on AI and machine learning fundamentals.

## 🙏 Acknowledgments

- **PyTorch Team**: For excellent deep learning framework
- **ImageNet**: For pre-trained model weights
- **AI Programming Nanodegree**: For project structure and guidance
- **Open Source Community**: For tools and libraries

## 📚 Additional Resources

### Documentation
- [PyTorch Documentation](https://pytorch.org/docs/)
- [torchvision Models](https://pytorch.org/vision/stable/models.html)
- [Python argparse](https://docs.python.org/3/library/argparse.html)

### Learning Materials
- [CS231n: CNN for Visual Recognition](http://cs231n.stanford.edu/)
- [Deep Learning Specialization](https://www.deeplearning.ai/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

### Related Papers
- VGG: [Very Deep Convolutional Networks](https://arxiv.org/abs/1409.1556)
- ResNet: [Deep Residual Learning](https://arxiv.org/abs/1512.03385)
- AlexNet: [ImageNet Classification](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)

## 🚀 Future Enhancements

- [ ] Add support for more CNN architectures (EfficientNet, MobileNet)
- [ ] Implement GPU acceleration optimization
- [ ] Add web interface for easy image upload
- [ ] Create visualization dashboard for results
- [ ] Add confidence scores for predictions
- [ ] Implement ensemble model voting
- [ ] Add data augmentation for training
- [ ] Create Docker container for easy deployment

## 📞 Contact

For questions, suggestions, or contributions, please open an issue or submit a pull request.

---

**Note**: This project is designed for educational purposes to understand image classification, CNN architectures, and model evaluation in practical machine learning applications.

**Happy Classifying! 🐕🎉**