# Student Result Prediction using Logistic Regression

This project demonstrates a simple implementation of Logistic Regression using Python and Scikit-learn to predict student results based on study hours and attendance percentage.

## Project Overview

The model uses:
- Study Hours
- Attendance Percentage

to predict whether a student will:
- Pass (1)
- Fail (0)

This project is useful for beginners learning:
- Machine Learning basics
- Logistic Regression
- Data preprocessing
- Model training and evaluation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn

---

## Dataset

The dataset is created manually within the program.

| StudyHours | Attendance | Result |
|------------|------------|--------|
| 2 | 50 | 0 |
| 4 | 60 | 0 |
| 6 | 70 | 1 |
| 8 | 80 | 1 |
| 10 | 90 | 1 |

### Target Variable
- 0 → Fail
- 1 → Pass

---

## Features of the Project

- Data creation using Pandas
- Splitting dataset into training and testing sets
- Logistic Regression model training
- Prediction on test data
- Accuracy evaluation
- Prediction for new student data

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Navigate to Project Folder

```bash
cd your-repository-name
```

### 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn
```

### 4. Run the Python File

```bash
python filename.py
```

---

## Sample Output

```bash
Original Data:
   StudyHours  Attendance  Result
0           2          50       0
1           4          60       0
2           6          70       1
3           8          80       1
4          10          90       1

Accuracy: 1.0

prediction for new student: [1]
```

---

## Machine Learning Model

### Logistic Regression

Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability of a categorical outcome.

---

## Future Improvements

- Add larger real-world datasets
- Build a web interface using Flask
- Visualize results using Matplotlib
- Deploy the project online

---

## Author

@Dwarakesh09
Developed as a beginner Machine Learning project using Python and Scikit-learn.

---

## License

This project is open-source and available under the MIT License.
