# Yelp Dataset Machine Learning Integration

---
![image](https://github.com/user-attachments/assets/9c8ed554-5a14-4a65-a163-bd2a05490536)

## Objective

This project aims to merge and preprocess Yelp datasets to create a machine learning pipeline capable of predicting whether a user liked a business. Using an **XGBoost Classifier**, the project integrates categorical and numerical features for improved prediction accuracy.

---

## Workflow

### 1. Data Loading and Preprocessing

- Load datasets: **business**, **check-in**, **review**, **tip**, and **user**.
- Convert date columns (`yelping_since`, `date`) to datetime format for consistency.
- Rename columns for better readability (e.g., prefixing with dataset type like `business_`, `review_`).

### 2. Dataset Integration

- Merge datasets to create comprehensive tables:
  - **`df_main_1`**: Merges review, business, user, and tip datasets.
  - **`df_main_2`**: Combines review-based scores, business segments, and user segments.
  - **`df_main`**: Final dataset merging `df_main_1` and `df_main_2`.

- Remove duplicate columns to simplify the final dataset.

### 3. Feature Engineering

- Extract categorical columns for further analysis.
- Calculate aggregated averages (`mean`) for each user-business pair.
- Add a target variable (`liked`) based on whether the user rating is **4 or higher**.

![image](https://github.com/user-attachments/assets/288432ae-be5e-4e0f-9f10-38cc7a9e4d11)


---

## Machine Learning Pipeline

### 1. Data Preparation

- Convert categorical variables (`user_id`, `business_id`, `business_main_category`, etc.) to categorical types for efficient processing.
- Split data into training and testing sets with a 70-30 ratio.

### 2. Model Training

- Use **XGBoost Classifier** with categorical feature support enabled.
- Train the model on the training set (`X_train`, `y_train`).

### 3. Model Evaluation

- Predict on the test set (`X_test`) and calculate metrics:
  - **Accuracy Score**
  - **Classification Report**
  - **Confusion Matrix**

---

## Real-Time Prediction Example

### Filter and Combine Data

- Extract user-specific and business-specific features.
- Combine user and business attributes for prediction.
- Fill missing values for non-applicable fields.

### Prediction

- Use the trained XGBoost model to predict the probability of the user liking the business.
- Save the trained model for future use with **Joblib**.

---

## Results

- **Feature Columns**: Exported a comprehensive list of columns used for training the model for reproducibility.
- **Categorical Columns**: Extracted for efficient processing within the machine learning pipeline.
- **Model Save**: The trained XGBoost model is saved as `y7_xgboost_model.pkl`.

![D10A7ABA-ADEA-4793-A6A3-8845313255FC](https://github.com/user-attachments/assets/169582be-36c2-45ac-a882-17cfe2020e4c)


---

## Insights

This project showcases the integration of multiple datasets and the application of machine learning to predict user preferences. By leveraging a robust feature engineering pipeline and advanced machine learning models, the system provides a framework for personalized business recommendations.

<br><br>
---

## Contributors and Contact Information

Aybüke Çilingir

[LinkedIn](https://www.linkedin.com/in/aybukecilingir/) | [Email](mailto:aybukecilingir@outlook.com) | [Github](https://github.com/AybukeCilingir)
  
---

Furkan Karakuz

[LinkedIn](https://www.linkedin.com/in/furkankarakuz/) | [Email](mailto:karakuzfurkan.98@gmail.com) | [Github](https://github.com/furkankarakuz)

---
Güldeniz Güzelay

[LinkedIn](https://www.linkedin.com/in/guldenizguzelay/) | [Email](mailto:denizguzelay@hotmail.com) | [Github](https://github.com/Guldenizguzelay)

