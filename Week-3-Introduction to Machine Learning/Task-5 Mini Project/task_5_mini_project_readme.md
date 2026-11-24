# 📝 Task 5: Mini Project — Student Performance Prediction 

**Week 3: Introduction to Machine Learning**

| Field | Details |
| :--- | :--- |
| **Name** | Nune Venkata Yasasvi |
| **Project Title** | Student Performance Prediction |
| **Programming Language** | Python |
| **Libraries** | Pandas, Scikit-learn |
| **Dataset Size** | 30 Student Records |
| **Algorithm** | Logistic Regression (Classification) |

---

## 1. Introduction
Student Performance Prediction is a Machine Learning mini project that predicts whether a student is likely to Pass or Fail based on their academic performance.  
In this project, I use student information such as Study Hours, Attendance, Previous Marks, and Assignment Score to predict the final result.  
I use Python, Pandas, and Scikit-learn to build a classification model.

---

## 2. Create the Dataset (30 Students)

### Code Block 1:
```python
import pandas as pd

# Create a dataset with 30 student records

data = {
    "Study_Hours": [
        2, 3, 1, 4, 2, 3, 1, 4, 2, 3,
        5, 6, 7, 5, 8, 6, 7, 4, 6, 9,
        5, 8, 7, 4, 6, 3, 2, 5, 4, 7
    ],

    "Attendance": [
        55, 60, 50, 58, 65, 52, 70, 68, 58, 72,
        75, 85, 90, 80, 95, 78, 82, 76, 88, 96,
        72, 90, 86, 80, 92, 45, 40, 68, 62, 70
    ],

    "Previous_Marks": [
        38, 42, 35, 39, 45, 48, 40, 43, 32, 38,
        55, 72, 80, 65, 88, 60, 75, 58, 68, 92,
        62, 85, 70, 55, 78, 30, 28, 48, 45, 50
    ],

    "Assignment_Score": [
        40, 45, 38, 42, 48, 50, 44, 46, 35, 40,
        60, 78, 85, 70, 92, 68, 80, 65, 75, 95,
        66, 88, 76, 62, 84, 32, 30, 52, 48, 55
    ],

    "Result": [
        "FAIL", "FAIL", "FAIL", "FAIL", "FAIL",
        "FAIL", "FAIL", "FAIL", "FAIL", "FAIL",
        "PASS", "PASS", "PASS", "PASS", "PASS",
        "PASS", "PASS", "PASS", "PASS", "PASS",
        "PASS", "PASS", "PASS", "PASS", "PASS",
        "FAIL", "FAIL", "FAIL", "FAIL", "PASS"
    ]
}

df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("student_performance.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())
print("\nTotal Records:", len(df))
```

### Output:
```text
Dataset Created Successfully!

   Study_Hours  Attendance  Previous_Marks  Assignment_Score Result
0            2          55              38                40   FAIL
1            3          60              42                45   FAIL
2            1          50              35                38   FAIL
3            4          58              39                42   FAIL
4            2          65              45                48   FAIL

Total Records: 30
```

---

## 3. Load the Dataset Using Pandas

### Code Block 2:
```python
# Load dataset

df = pd.read_csv("student_performance.csv")

print("Dataset Loaded Successfully!")

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()
```

### Output:
```text
Dataset Loaded Successfully!

Dataset Shape:
(30, 5)
```

**Explanation:**  
Pandas is used to load and display the student dataset. The dataset contains 30 student records and 5 columns.

---

## 4. Clean the Data

### Code Block 3:
```python
# Check missing values

print("Missing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset After Cleaning:")
print(df.shape)

print("\nData Cleaning Completed Successfully!")
```

### Output:
```text
Missing Values:
Study_Hours         0
Attendance          0
Previous_Marks      0
Assignment_Score    0
Result              0

Dataset After Cleaning:
(30, 5)

Data Cleaning Completed Successfully!
```

**Explanation:**  
Data cleaning helps identify missing values and duplicate records. In this dataset, there are no missing values or duplicate records.

---

## 5. Select Features and Target

### Code Block 4:
```python
# Select input features and target

X = df[
    ["Study_Hours", "Attendance",
     "Previous_Marks", "Assignment_Score"]
]

y = df["Result"]

print("Input Features (X):")
print(X.head())

print("\nTarget Variable (y):")
print(y.head())
```

### Output:
```text
Input Features (X):

   Study_Hours  Attendance  Previous_Marks  Assignment_Score
0            2          55              38                40
1            3          60              42                45
2            1          50              35                38
3            4          58              39                42
4            2          65              45                48

Target Variable (y):
0    FAIL
1    FAIL
2    FAIL
3    FAIL
4    FAIL
Name: Result, dtype: object
```

**Explanation:**
- `X` represents the input features.
- `y` represents the target variable.
- Input features include Study Hours, Attendance, Previous Marks, and Assignment Score.
- The target variable is Pass or Fail.

---

## 6. Split the Dataset

### Code Block 5:
```python
from sklearn.model_selection import train_test_split

# Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Data Size:", len(X_train))
print("Testing Data Size:", len(X_test))
```

### Output:
```text
Training Data Size: 24
Testing Data Size: 6
```

**Explanation:**  
The dataset is divided into two parts:
- 80% training data (24 students).
- 20% testing data (6 students).

Training data helps the model learn patterns, while testing data checks its performance on unseen records.

---

## 7. Train the Machine Learning Model

### Code Block 6:
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Create Logistic Regression model

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(random_state=42))
])

# Train the model

model.fit(X_train, y_train)

print("Machine Learning Model Trained Successfully!")
```

### Output:
```text
Machine Learning Model Trained Successfully!
```

**Explanation:**  
Logistic Regression is a classification algorithm used to predict categories such as Pass and Fail.  
`StandardScaler` helps bring numerical features to a similar scale before training.  
The `fit()` function trains the model using the training data.

---

## 8. Make Predictions

### Code Block 7:
```python
# Predict results using testing data

y_pred = model.predict(X_test)

print("Actual Results vs Predicted Results:")

results = pd.DataFrame({
    "Actual Result": y_test.values,
    "Predicted Result": y_pred
})

print(results.to_string(index=False))
```

### Output:
```text
Actual Results vs Predicted Results:

Actual Result Predicted Result
         FAIL            FAIL
         PASS            PASS
         FAIL            FAIL
         PASS            PASS
         FAIL            FAIL
         PASS            PASS
```

**Explanation:**  
The `predict()` function uses the trained model to predict whether students are likely to Pass or Fail.

---

## 9. Calculate Model Accuracy

### Code Block 8:
```python
from sklearn.metrics import accuracy_score

# Calculate model accuracy

accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")
```

### Output:
```text
Model Accuracy: 100.0 %
```

**Explanation:**  
Accuracy measures how many predictions are correct compared with the actual results.  
In this test, all 6 predictions were correct, giving 100% test accuracy. However, this is a small sample and does not guarantee the same performance on other students.

---

## 10. Test the Model with 3 New Students

### Code Block 9:
```python
# Test with three new student inputs

new_students = pd.DataFrame({
    "Study_Hours": [6, 2, 5],
    "Attendance": [85, 50, 75],
    "Previous_Marks": [72, 35, 60],
    "Assignment_Score": [78, 40, 65]
})

# Make predictions

predictions = model.predict(new_students)

print("New Student Predictions:")

for i in range(len(new_students)):

    print("\nStudent", i + 1)

    print("Study Hours:", new_students.iloc[i]["Study_Hours"])
    print("Attendance:", new_students.iloc[i]["Attendance"], "%")
    print("Previous Marks:", new_students.iloc[i]["Previous_Marks"])
    print("Assignment Score:", new_students.iloc[i]["Assignment_Score"])

    print("Prediction:", predictions[i])
```

### Output:
```text
New Student Predictions:

Student 1
Study Hours: 6
Attendance: 85 %
Previous Marks: 72
Assignment Score: 78
Prediction: PASS

Student 2
Study Hours: 2
Attendance: 50 %
Previous Marks: 35
Assignment Score: 40
Prediction: FAIL

Student 3
Study Hours: 5
Attendance: 75 %
Previous Marks: 60
Assignment Score: 65
Prediction: PASS
```

**Explanation:**  
The trained model is tested using three new student records. It predicts PASS or FAIL based on their study hours, attendance, previous marks, and assignment scores.

---

## 11. Explanation of How the Model Works
The Student Performance Prediction model works through the following steps:
1. **Load Dataset:** Loads 30 student records using Pandas.
2. **Clean Data:** Checks missing values and removes duplicate records.
3. **Select Features and Target:** Selects four input features and the Result column.
4. **Split Dataset:** Divides the dataset into 80% training and 20% testing data.
5. **Train Model:** Uses Logistic Regression to learn patterns from student data.
6. **Make Predictions:** Predicts whether students are likely to Pass or Fail.
7. **Calculate Accuracy:** Compares predicted results with actual results.

### Machine Learning Workflow
```text
Dataset → Data Cleaning → Feature Selection → Train-Test Split → Model Training → Prediction → Accuracy
```

---

## 12. Explanation of Important Functions

| Function | Purpose |
| :--- | :--- |
| `read_csv()` | Loads the dataset |
| `isnull()` | Checks missing values |
| `drop_duplicates()` | Removes duplicate records |
| `train_test_split()` | Divides data into training and testing sets |
| `StandardScaler()` | Scales numerical features |
| `LogisticRegression()` | Creates a classification model |
| `fit()` | Trains the model |
| `predict()` | Makes predictions |
| `accuracy_score()` | Calculates model accuracy |

---

## 13. Screenshots
Capture and attach your actual program screenshots for the following sections:
- Screenshot 1 – Dataset Creation
- Screenshot 2 – Dataset Loading
- Screenshot 3 – Data Cleaning
- Screenshot 4 – Feature and Target Selection
- Screenshot 5 – Training and Testing Split
- Screenshot 6 – Model Training
- Screenshot 7 – Prediction Results
- Screenshot 8 – Model Accuracy
- Screenshot 9 – Three New Student Predictions

---

## 14. Project Report (200–300 Words)

### Student Performance Prediction – Mini Project Report
In this mini project, I developed a Student Performance Prediction system using Machine Learning and Python. The main objective of this project is to predict whether a student is likely to Pass or Fail based on academic performance.

**Dataset Used:** I created a dataset containing 30 student records with five columns: Study Hours, Attendance, Previous Marks, Assignment Score, and Result. The dataset contains both PASS and FAIL examples.

**Features Selected:** I selected Study Hours, Attendance, Previous Marks, and Assignment Score as input features. The Result column was selected as the target variable.

**Model Used:** I used Logistic Regression, a classification algorithm from Scikit-learn. I divided the dataset into 80% training data and 20% testing data. I also used StandardScaler to scale the numerical features.

**Results Obtained:** The model successfully predicted Pass or Fail for the testing records. I also tested the model with three new student inputs. It predicted PASS for the first and third students and FAIL for the second student.

**Accuracy:** The model achieved 100% accuracy on the six testing records.

**Limitations:** The dataset contains only 30 records, which is a small amount of data. The high accuracy on this small test set does not guarantee accurate predictions for all students.

**Future Improvements:** In the future, I would use a larger real-world student dataset, include more academic features, and test different classification algorithms to improve prediction reliability.

---

## 15. Conclusion
In this mini project, I successfully developed a Student Performance Prediction model using Python, Pandas, and Scikit-learn.  
I learned how to create and load a dataset, clean data, select features, split training and testing data, train a classification model, make predictions, and calculate accuracy.  
This project helped me understand how Machine Learning can be used to predict student academic performance.

---

| Status | Summary |
| :--- | :--- |
| **Project Status** | Completed |
| **Algorithm** | Logistic Regression |
| **Dataset** | 30 Student Records |
| **Model Accuracy** | 100% on the test set |