# Credit Data Analysis of Gold Atlantis

## Overview
This case study presents an analysis of the credit data of Gold Atlantis, aimed at identifying patterns in the data and making predictions on the likelihood of a customer becoming a defaulter. The analysis utilizes various statistical techniques such as univariate, bivariate, and multivariate analysis to develop insights and help the firm identify customers with a lower probability of defaulting.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Analysis Techniques](#analysis-techniques)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset
The dataset used for this analysis contains various features related to customers' credit history, demographics, and financial status. The key variables include:

- **CustomerID**: Unique identifier for each customer
- **Age**: Age of the customer
- **Gender**: Gender of the customer
- **Income**: Annual income of the customer
- **CreditScore**: Credit score of the customer
- **LoanAmount**: Amount of loan taken by the customer
- **LoanDuration**: Duration of the loan
- **Default**: Whether the customer defaulted (1) or not (0)

## Analysis Techniques
The analysis was conducted using the following statistical techniques:

### Univariate Analysis
- **Descriptive Statistics**: Summary statistics of individual variables
- **Distribution Plots**: Histograms, box plots, and density plots

### Bivariate Analysis
- **Correlation Analysis**: Identifying relationships between pairs of variables
- **Scatter Plots**: Visualizing relationships between continuous variables
- **Box Plots**: Comparing distributions across different categories

### Multivariate Analysis
- **Logistic Regression**: Predicting the probability of default
- **Decision Trees**: Classifying customers based on predictor variables
- **Random Forest**: Ensemble method to improve prediction accuracy

## Results
The analysis revealed several key insights:
- Customers with lower credit scores are more likely to default.
- Income and loan amount have a significant impact on the likelihood of default.
- Gender and age also play a role in predicting default, with younger customers showing a higher probability of defaulting.

The logistic regression model and random forest classifier were the most effective in predicting customer defaults, achieving an accuracy of over 85%.

## Usage
To replicate the analysis, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/sakshi-raj05/gold-atlantis-credit-analysis.git
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the analysis script:
    ```bash
    python analysis.py
    ```
