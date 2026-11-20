# Phishing Website Detection System

This project is a machine learning-based web application that detects phishing websites in real-time. It extracts features from a given URL and uses a trained Random Forest model to classify it as legitimate or phishing.

## Features
- **Real-time URL Scanning**: Enter a URL and get instant classification.
- **Feature Extraction Module**: Extracts key indicators of phishing such as URL length, IP address usage, and domain age.
- **Machine Learning Model**: Powered by a Random Forest Classifier trained on a custom dataset.
- **Modern UI**: A responsive, glassmorphism-styled web interface.

## Project Structure
- `app/`: Flask web application (backend and frontend).
- `data/`: Contains the datasets used for training.
- `models/`: Saved trained ML models (`.pkl` files).
- `notebooks/`: Scripts and Jupyter notebooks for training the model.

## Setup Instructions

1. **Clone the repository** (if applicable) or navigate to the project directory:
   ```bash
   cd "d:\phishing project"
   ```

2. **Set up a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Model**:
   If the `models/` directory doesn't have a `.pkl` file, generate it by running:
   ```bash
   cd notebooks
   python train_model.py
   cd ..
   ```

5. **Run the Application**:
   ```bash
   cd app
   python app.py
   ```

6. Open your browser and navigate to: `http://127.0.0.1:5000`

## Technologies Used
- Python, Flask
- scikit-learn, pandas, numpy
- HTML5, CSS3 (Vanilla CSS with modern design patterns)
- python-whois (for domain analysis)
