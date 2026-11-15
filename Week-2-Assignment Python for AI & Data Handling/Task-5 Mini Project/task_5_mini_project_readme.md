# Student Performance Data Analysis

**Task 5: Mini Project — 20 Marks**  
**Name:** Nune Venkata Yasasvi  
**Week 2 Assignment:** Python for AI & Data Handling  

---

## 1. Project Description
This mini project performs basic data analysis on a student performance dataset containing 30 student records.

The project uses Python, Pandas, and Matplotlib to:
- Load and display the student dataset.
- Check dataset information and important columns.
- Handle missing values.
- Remove duplicate records.
- Calculate average, highest, and lowest marks.
- Count passed and failed students.
- Create three charts to visualize student performance.

---

## 2. Technologies Used
- Python
- Jupyter Notebook
- Pandas
- Matplotlib

---

## 3. Dataset Details
- **Dataset filename:** `students_cleaned.csv`
- **Total Records:** 30
- **Columns:**
  - `Student_ID`
  - `Name`
  - `Age`
  - `Marks`
  - `Department`

---

## 4. Project Files
```text
Task-5 Mini Project/
│
├── students_cleaned.csv
├── Task-5-Mini Project.ipynb
├── README.md
├── Task-5-Mini Project Report.pdf
│
└── Screenshot Outputs/
    ├── 0_students_cleaned_csv.png
    ├── 1_load_dataset.png
    ├── 2_dataset_information.png
    ├── 3_data_cleaning_input.png
    ├── 3_data_cleaning_output_1.png
    ├── 3_data_cleaning_output_2.png
    ├── 4_analysis_results.png
    ├── 5_department_bar_chart_input.png
    ├── 5_department_bar_chart_output.png
    ├── 6_marks_histogram_input.png
    ├── 6_marks_histogram_output.png
    ├── 7_pass_fail_chart_input.png
    └── 7_pass_fail_chart_output.png
```

---

## 5. How to Run the Project
1. Install Python on your computer.
2. Install Jupyter Notebook.
3. Install the required libraries:
   ```bash
   pip install pandas matplotlib
   ```
4. Keep `students_cleaned.csv` and the Jupyter Notebook in the same project folder.
5. Open Jupyter Notebook.
6. Open `Task-5-Mini Project.ipynb`.
7. Run the notebook cells one by one.
8. View the data analysis results and generated graphs.

---

## 6. Data Handling
The student performance dataset is loaded using the Pandas library. The dataset contains 30 student records with important information about students.

**Data Handling Operations:**
- Load the dataset using Pandas.
- Display the first five records using `df.head()`.
- Display dataset information using `df.info()`.
- Check the number of rows and columns using `df.shape`.
- Display column names using `df.columns`.

**Important Columns:**
- **Student_ID:** Unique identification number of each student.
- **Name:** Name of the student.
- **Age:** Age of the student.
- **Marks:** Marks obtained by the student.
- **Department:** Department of the student (CSE, ECE, IT).

---

## 7. Data Cleaning
Data cleaning is performed to improve dataset quality and accuracy before analysis.

**Data Cleaning Operations:**
- Identify missing values using `df.isnull().sum()`.
- Convert `Age` and `Marks` columns into numeric values using `pd.to_numeric()`.
- Replace missing `Age` values with the median.
- Replace missing `Marks` values with the mean.
- Convert `Age` and `Marks` into integer values.
- Remove duplicate records using `df.drop_duplicates()`.
- Reset the dataset index using `df.reset_index(drop=True)`.

**Data Cleaning Results:**
- Missing values are handled successfully.
- Duplicate records are removed.
- `Age` and `Marks` columns contain numeric values.
- The cleaned dataset is ready for further analysis.
- **Final Dataset:** 30 student records.

---

## 8. Data Analysis
The project calculates:
- Average marks of students.
- Highest marks.
- Lowest marks.
- Number of passed students.
- Number of failed students.

**Passing Criteria:** Students scoring 35 marks or above are considered passed. Students scoring below 35 are considered failed.

---

## 9. Data Visualization
Three charts are created using Matplotlib:
1. **Bar Chart:** Average marks by department.
2. **Histogram:** Distribution of student marks.
3. **Bar Chart:** Comparison of passed and failed students.

---

## 10. Conclusion
This project demonstrates how Python can be used for student performance data analysis. Pandas is used for data handling, data cleaning, and statistical calculations, while Matplotlib is used to create visual representations of student performance.

The project provides useful insights into student marks, department performance, and pass/fail results. It also improves practical knowledge of Python libraries used in Data Analysis and Artificial Intelligence.

---

## 11. Final Deliverables
- Jupyter Notebook (`.ipynb`)
- Student dataset (`.csv`)
- README file (`.md`)
- Three visualization charts
- Required project screenshots