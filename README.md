**Project Overview**

This project is an end-to-end Air Quality Index (AQI) prediction system built using machine learning ensemble techniques. The system leverages a Voting Regressor composed of Random Forest and Gradient 
Boosting models to generate accurate AQI predictions based on multi-city pollution data.
The trained model is integrated into a Flask-based web application that supports real-time inference, enabling users to input pollutant values and receive immediate AQI predictions
through a simple web interface.

 **Key Features**

End-to-end machine learning pipeline (data preprocessing → feature engineering → model training → evaluation → deployment)Ensemble learning using Voting Regressor for improved predictive stability
Trained on 100,000+ pollution records across multiple cities
Real-time AQI prediction via Flask REST interface
Optimized inference pipeline with low-latency predictions
Modular and production-ready project structure

**Machine Learning Approach**

Model Type: Voting Ensemble Regressor

Base Models:
Random Forest Regressor
Gradient Boosting Regressor

Preprocessing:
Data cleaning and normalization
Feature selection and transformation
Evaluation Metric: Predictive consistency and inference latency

**Performance**

Predictive Consistency: Up to 92% during evaluation
Inference Latency: <150 ms per prediction
Designed for scalability and real-time deployment

**Tech Stack**
Programming & ML: Python, Scikit-learn, Pandas, NumPy
Backend & Deployment: Flask
Frontend: HTML, CSS

**How It Works**
Pollution data is preprocessed using structured feature pipelines
Multiple regression models are trained and combined using voting ensemble logic
The trained model is serialized and served via a Flask application
User inputs are processed in real time to generate AQI predictions
