# Real-Time Network Anomaly & Intrusion Detection System

A Machine Learning-powered Intrusion Detection System (IDS) built using Django and Scikit-Learn to classify network traffic as normal or anomalous in real time.

## Features

- Real-time network anomaly detection
- K-Nearest Neighbors (KNN) classification model
- Interactive web dashboard
- AWS deployment with Auto Scaling and Load Balancing
- Responsive user interface
- Machine learning model integration with Django

## Tech Stack

- Python
- Django
- Scikit-Learn
- Pandas
- AWS EC2
- Elastic Load Balancer (ELB)
- Auto Scaling
- Ubuntu Linux

## Machine Learning Model

- Algorithm: K-Nearest Neighbors (KNN)
- Dataset Size: 100,000+ network records
- Accuracy: 87.7%
- Feature Scaling: StandardScaler
- Hyperparameter Optimization performed for model selection

## System Architecture

1. User submits network traffic parameters.
2. Django backend processes the request.
3. Features are scaled using StandardScaler.
4. Trained KNN model predicts traffic status.
5. Result is displayed as Normal or Anomaly.

## Learning Outcomes

- Machine Learning model deployment
- AWS cloud infrastructure
- High availability architecture
- Django application development
- Real-time prediction systems

## Future Enhancements

- Real packet capture integration
- Additional ML models
- Alerting and notification system
- Monitoring dashboard
