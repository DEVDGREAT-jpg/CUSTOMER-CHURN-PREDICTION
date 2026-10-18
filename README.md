# Customer Churn Prediction Using Machine Learning

## 📌 Overview

Customer churn prediction is a machine learning project that aims to identify customers who are likely to stop using a company's services. Retaining existing customers is essential for businesses, as acquiring new customers can be more expensive than retaining current ones.

This project involves Exploratory Data Analysis (EDA) to understand customer behavior and the application of a Support Vector Machine (SVM) classifier to predict customer churn.

## 🎯 Objectives

* Perform Exploratory Data Analysis (EDA) to identify patterns and trends in customer data.
* Understand the factors associated with customer churn.
* Preprocess customer data for machine learning.
* Build a Support Vector Machine (SVM) classification model.
* Evaluate the model's performance in predicting customer churn.

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Pandas** — Data manipulation and analysis
* **NumPy** — Numerical computations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical data visualization
* **Scikit-learn** — Machine learning and model evaluation
* **Jupyter Notebook** — Interactive development and analysis

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset, examine customer characteristics, and identify patterns associated with churn.

The analysis included:

* Understanding the dataset structure and features.
* Examining missing values and data distributions.
* Visualizing relationships between customer attributes and churn.
* Identifying patterns and trends that may influence customer retention.

## 🤖 Machine Learning Model

### Support Vector Machine (SVM)

A Support Vector Machine classifier was used to predict whether a customer is likely to churn.

SVM is a supervised machine learning algorithm that identifies a decision boundary separating different classes. It can be applied to binary classification problems such as customer churn prediction.

**Workflow:**

1. Data loading and preprocessing.
2. Exploratory Data Analysis.
3. Feature selection and preparation.
4. Splitting the data into training and testing sets.
5. Training the SVM classification model.
6. Evaluating predictions using appropriate classification metrics.

## 📈 Model Evaluation

The model's performance can be evaluated using the following metrics:

* **Accuracy:** Overall proportion of correct predictions.
* **Precision:** Proportion of predicted churn cases that were actual churn cases.
* **Recall:** Proportion of actual churn cases correctly identified by the model.
* **F1-score:** Harmonic mean of precision and recall.
* **Confusion Matrix:** Breakdown of correct and incorrect predictions.

These metrics help assess how effectively the model identifies customers who may leave a service.

## 📁 Project Structure

```text
customer-churn-prediction/
│
├── data/                  # Dataset (if included)
├── notebooks/             # Jupyter notebooks for EDA and modeling
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```

*Update the folder structure above to match your actual repository.*

## ⚙️ Installation and Usage

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd customer-churn-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the notebook

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open the project notebook to explore the data, review the EDA, train the SVM model, and examine the results.

## 💡 Key Learnings

* Performing Exploratory Data Analysis on customer data.
* Understanding customer churn patterns.
* Preparing data for supervised machine learning.
* Applying SVM to a classification problem.
* Evaluating classification models using performance metrics.

## 🔮 Future Improvements

* Compare SVM performance with Logistic Regression, Random Forest, and other classification algorithms.
* Perform hyperparameter tuning to improve model performance.
* Use feature importance or other interpretability techniques to understand churn-related factors.
* Develop an interactive web application for real-time churn predictions.

## 👨‍💻 Author

**Satya Dev Sharma**

Computer Science and Engineering

---

⭐ If you find this project useful, consider giving the repository a star!
