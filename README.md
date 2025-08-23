# Phishing URL Detection Project

## Overview
This project is a simple phishing website detection system using machine learning. It analyzes URL features to predict whether a URL is phishing or legitimate.

## Files
- phishing_detection.py: The main Python script that extracts features from URLs and trains the machine learning model.
- urls_dataset.csv: A sample dataset containing URLs and their labels (phishing or legitimate) for training.

## Requirements
- Python 3.x
- Libraries: pandas, scikit-learn, requests, python-whois

## Installation

pip install pandas scikit-learn requests python-whois

## Usage
1. Train the model using the dataset:

python phishing_detection.py
2. Modify the script to test new URLs as needed.

## Notes
- This dataset is a small sample for demonstration. For real-world applications, a larger dataset is recommended.
- Optional live URL checking with PhishTank API is included.

