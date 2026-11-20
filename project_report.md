# Project Report: Phishing Website Detection System using Machine Learning

## 1. Abstract
Phishing attacks remain one of the most prevalent cybersecurity threats, tricking users into revealing sensitive information through fraudulent websites. This project presents a machine learning-based approach to detect phishing URLs in real-time. By extracting lexical and domain-based features from URLs and applying classification algorithms (such as Random Forest), the system accurately classifies links as either legitimate or phishing. The solution is deployed as a user-friendly web application, providing an accessible tool for end-users to verify suspicious links.

## 2. Introduction
- **Problem Statement**: The exponential growth of phishing attacks and the limitations of traditional blacklist-based detection methods.
- **Objectives**: To build a robust, scalable machine learning model that analyzes URL features to identify phishing sites dynamically.
- **Scope**: Focuses on URL-based and domain-based feature extraction without requiring deep content analysis (e.g., rendering full HTML), ensuring fast, real-time scanning.

## 3. System Architecture & Modules
### 3.1 Data Collection & Preprocessing
- **Datasets**: Combination of UCI Phishing Websites Dataset and custom mock data representing modern phishing trends.
- **Preprocessing**: Handling missing values, encoding categorical data, and balancing the dataset.

### 3.2 Feature Extraction Module
This module takes a raw URL as input and extracts structural features:
- `url_length`: Phishing URLs tend to be longer to obscure the actual domain.
- `has_ip`: Legitimate sites rarely use IP addresses directly in the URL.
- `has_at_symbol`: The `@` symbol is often used to ignore the preceding string and redirect the user.
- `count_hyphen`: Phishers often use hyphens in domain names to mimic legitimate brands.
- `domain_age_days`: Querying WHOIS records to determine domain age; phishing domains are typically short-lived.

### 3.3 Machine Learning Classification
- **Algorithm Used**: Random Forest Classifier.
- **Why Random Forest?**: It handles non-linear relationships well, is resistant to overfitting, and provides feature importance metrics, which are crucial for interpretability in cybersecurity.

### 3.4 Web Application (Deployment)
- **Backend**: Flask API that receives URLs, triggers the feature extraction script, and feeds data to the ML model.
- **Frontend**: A modern, responsive interface using HTML/CSS/JS (with glassmorphism design) allowing users to paste URLs and view the detection results and confidence score.

## 4. Implementation Details
- **Tech Stack**: Python, Flask, scikit-learn, HTML/CSS.
- **Key Libraries**: `pandas` (data manipulation), `python-whois` (domain analysis), `joblib` (model serialization).

## 5. Results and Evaluation
- **Accuracy**: (Insert your test accuracy here, e.g., 94.5%)
- **Precision/Recall**: High recall is prioritized to minimize false negatives (failing to flag a phishing site).
- **Performance**: The system processes and classifies URLs in under a second on average.

## 6. Future Enhancements
- Integration of Deep Learning (e.g., LSTM for sequential character analysis of the URL).
- Real-time Blacklist API integration (e.g., Google Safe Browsing) as a primary filter.
- Development of a Chrome/Firefox browser extension for seamless user protection.

## 7. Conclusion
The developed Phishing Website Detection System successfully demonstrates how machine learning can be leveraged to proactively identify cyber threats. The combination of targeted feature extraction and ensemble learning provides a high-accuracy, real-time defense mechanism against phishing attacks.
