import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator, TransformerMixin

# Sample dataset with more features
data = {
    'age': [25, 30, 35, np.nan, 40, 45, 50, 55, np.nan, 60],
    'salary': [50000, 60000, 65000, 70000, np.nan, 80000, 85000, 90000, 95000, np.nan],
    'city': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago', 'New York'],
    'gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
    'purchased': ['Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Custom Transformer for creating new features
class AgeSalaryRatio(BaseEstimator, TransformerMixin):
    def __init__(self, age_index, salary_index):
        self.age_index = age_index
        self.salary_index = salary_index

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        age_salary_ratio = X[:, self.age_index] / X[:, self.salary_index]
        return np.c_[X, age_salary_ratio]

# Define numerical and categorical features
numerical_features = ['age', 'salary']
categorical_features = ['city', 'gender']

# Preprocessing for numerical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Full pipeline with custom feature engineering
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('features', AgeSalaryRatio(age_index=0, salary_index=1))
])

# Separate features and target variable
X = df.drop('purchased', axis=1)
y = df['purchased'].map({'Yes': 1, 'No': 0})

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply the full preprocessing pipeline to the training and test data
X_train_preprocessed = full_pipeline.fit_transform(X_train)
X_test_preprocessed = full_pipeline.transform(X_test)

print("\nPreprocessed Training Data:")
print(X_train_preprocessed)

print("\nPreprocessed Test Data:")
print(X_test_preprocessed)

# Convert the preprocessed arrays back to DataFrames for better readability
# Note: The column names will include the original columns plus the new feature(s)
ohe = preprocessor.named_transformers_['cat'].named_steps['onehot']
categorical_columns = ohe.get_feature_names_out(categorical_features)
preprocessed_columns = numerical_features + list(categorical_columns) + ['age_salary_ratio']

X_train_preprocessed_df = pd.DataFrame(X_train_preprocessed, columns=preprocessed_columns)
X_test_preprocessed_df = pd.DataFrame(X_test_preprocessed, columns=preprocessed_columns)

print("\nPreprocessed Training DataFrame:")
print(X_train_preprocessed_df)

print("\nPreprocessed Test DataFrame:")
print(X_test_preprocessed_df)
