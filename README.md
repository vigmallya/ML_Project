# **Complete ML Project Pipeline**

This project implements a machine learning pipeline for data ingestion, transformation, model training, evaluation, and deployment. It includes steps for hyperparameter tuning and is built using Flask for web-based interaction, with deployment options on AWS Elastic Beanstalk and Azure.

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Key Components](#key-components)
5. [Training Models](#training-models)
6. [Hyperparameter Tuning](#hyperparameter-tuning)
7. [Deployment](#deployment)

## **Project Overview**

This project demonstrates an end-to-end machine learning solution, covering:
- Data ingestion from various sources
- Data preprocessing and feature engineering
- Model training and evaluation
- Deployment using Flask for predictions and AWS/Azure for hosting the web app

## **Project Structure**

```bash
├── src/                      # Source code for the project
│   ├── components/           # Main components like data ingestion, transformation, etc.
│   ├── pipeline/             # Training and prediction pipelines
│   ├── logger.py             # Custom logging module
│   ├── exception.py          # Custom exception handling module
│   ├── utils.py              # Utility functions (e.g., saving model)
├── app.py                    # Flask web app for model prediction
├── requirements.txt          # Required dependencies
├── setup.py                  # Package configuration
└── README.md                 # Project documentation

```

## **Setup Instructions**

1. **Create a Python environment**:
   ```bash
   conda create -n ml_project python=3.8 -y
   conda activate ml_project
   ```

2. **Install dependencies**:
   Make sure to install all necessary dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Start with data ingestion by running**:
   ```bash
   python data_ingestion.py
   ```

## **Key Components**

### 1. **Data Ingestion**
   - Reads data from multiple sources, splits it into train and test datasets.
   - The main logic is implemented in the `data_ingestion.py` file under `components`.

### 2. **Data Transformation**
   - Responsible for feature engineering, data cleaning, and converting categorical data to numerical.
   - Handles encoding and scaling for training and testing datasets.

### 3. **Model Training**
   - Trains multiple models and evaluates them.
   - The best model is saved as a `.pkl` file for deployment.

### 4. **Model Evaluation**
   - Compares models based on performance metrics.
   - Uses techniques like hyperparameter tuning to get the best model.

### 5. **Model Deployment**
   - The project is deployed using AWS Elastic Beanstalk or Azure Web App.
   - Flask serves as the frontend to interact with the model and make predictions.

## **Training Models**

You can train various machine learning models and perform evaluation by running the pipeline. The models supported include:
- Decision Tree
- Random Forest
- Gradient Boosting, and more.

Example code for hyperparameter tuning is in the `model_trainer.py` file.

## **Hyperparameter Tuning**

To perform hyperparameter tuning, you can adjust the parameters in the `params` dictionary and rerun the training script. Here's an example:
```python
params = {
    "Random Forest": {
        'n_estimators': [8, 16, 32, 64, 128, 256]
    },
    "Gradient Boosting": {
        'learning_rate': [0.1, 0.01, 0.05],
        'n_estimators': [8, 16, 32, 64, 128, 256]
    }
}
```

## **Deployment**

### 1. **AWS Elastic Beanstalk**:
   - Create an environment and set up a continuous deployment pipeline using CodePipeline.
   - Elastic Beanstalk automatically sets up the infrastructure for hosting the application.
   - To host the project in AWS, rename app.js to application.js

### 2. **Azure Web App**:
   - Create a new web app on Azure, connect it to GitHub for automatic deployment using GitHub Actions.

For detailed deployment steps, refer to the `AWS Deployment` and `Azure Deployment` sections in the project documentation.

Vignesh Mallya
