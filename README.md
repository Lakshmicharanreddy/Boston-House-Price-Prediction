# 🏠 Boston House Price Prediction Web Application

An end-to-end Machine Learning web application that predicts Boston housing prices using a trained regression model. The application provides both a web interface for users and REST API endpoints for programmatic access.

## 🚀 Live Demo

**Web Application:**
https://boston-house-price-prediction-1-2zwa.onrender.com

## 📌 Project Overview

This project demonstrates the complete machine learning deployment lifecycle:

* Data preprocessing and feature engineering
* Feature scaling using StandardScaler
* Model training and evaluation using Scikit-Learn
* Model serialization using Pickle
* REST API development using Flask
* Interactive web interface using HTML
* Cloud deployment using Render
* Version control and CI/CD integration using GitHub

The application predicts house prices based on multiple housing characteristics from the Boston Housing dataset.

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Scikit-Learn
* NumPy
* Pandas

### Backend

* Flask
* Gunicorn

### Frontend

* HTML5

### Deployment

* Render
* GitHub

---

## 📊 Dataset Information

The model uses the Boston Housing Dataset containing housing-related features such as:

| Feature | Description                                          |
| ------- | ---------------------------------------------------- |
| CRIM    | Per capita crime rate by town                        |
| ZN      | Proportion of residential land zoned for large lots  |
| INDUS   | Proportion of non-retail business acres              |
| CHAS    | Charles River dummy variable                         |
| NOX     | Nitric oxide concentration                           |
| RM      | Average number of rooms per dwelling                 |
| AGE     | Proportion of owner-occupied units built before 1940 |
| DIS     | Distance to employment centers                       |
| RAD     | Accessibility to radial highways                     |
| TAX     | Property tax rate                                    |
| PTRATIO | Pupil-teacher ratio                                  |
| B       | Proportion of Black population index                 |
| LSTAT   | Percentage of lower status population                |

Target Variable:

* **MEDV** → Median value of owner-occupied homes.

---

## ⚙️ Machine Learning Pipeline

### Data Preprocessing

* Missing value analysis
* Feature scaling using StandardScaler
* Train-test split for evaluation

### Model Training

* Linear Regression model implementation
* Model evaluation using regression metrics

### Model Serialization

* Trained model saved using Pickle (`regmodel.pkl`)
* StandardScaler saved using Pickle (`scaling.pkl`)

---

## 🌐 Application Features

### Web Interface

* User-friendly input form
* Real-time prediction generation
* Instant result display

### REST API Support

Supports JSON requests for external applications and testing tools such as Postman.

Example request:

```json
{
    "data": {
        "CRIM": 0.1,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.09,
        "RAD": 1,
        "TAX": 296,
        "PTRATIO": 15.3,
        "B": 396.90,
        "LSTAT": 4.98
    }
}
```

---

## 📂 Project Structure

```text
Boston-House-Price-Prediction/
│
├── app.py
├── regmodel.pkl
├── scaling.pkl
├── requirements.txt
├── Procfile
├── templates/
│   └── home.html
│
├── notebooks/
│   └── Boston House Price Prediction.ipynb
│
└── README.md
```

---

## ▶️ Running Locally

### Clone the Repository

```bash
git clone <repository-url>
cd Boston-House-Price-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## ☁️ Deployment

The application is deployed on Render using:

* Flask
* Gunicorn
* GitHub Integration
* Continuous Deployment Pipeline

---

## 📈 Future Improvements

* Improved UI using Bootstrap or TailwindCSS
* Docker containerization
* Model monitoring and logging
* Support for multiple regression models
* Feature importance visualization

---

## 👨‍💻 Author

**Nagireddy Lakshmi Charan Reddy**

* LinkedIn: https://www.linkedin.com/in/nagireddy-lakshmi-charan-reddy-812309303/
* GitHub: https://github.com/Lakshmicharanreddy/
