# 🫀 Healthybeat AI: Heart Disease Risk Predictor

## 🌟 Project Overview

**Healthybeat AI** is a prototype web application designed to predict an individual's risk of heart disease based on various health parameters. This project serves as a comprehensive learning exercise, integrating a machine learning model (Artificial Neural Network) into a functional web interface using the Python Flask framework.

The goal is to provide users with an instant, data-driven assessment of their heart health status.

## ✨ Features

* **Risk Prediction:** Uses an Artificial Neural Network (ANN) to assess input parameters and output a binary prediction: "Healthy Heart" or "At Risk of Heart Disease."

* **Intuitive UI:** Simple and clean user interface built with HTML and CSS for easy data entry.

* **Backend Integration:** Seamless communication between the front-end (HTML form) and the backend (Flask server).

* **Model Persistency:** Loads a pre-trained Keras model (`heart_model.h5`) to ensure quick prediction response times.

## 🚀 Technologies Used

| **Category** | **Technology** | **Purpose** | 
| :--- | :--- | :--- | 
| **Backend** | Python 3.x | Core programming language. | 
| **Web Framework** | Flask | Micro web framework for handling routes and serving the web pages. | 
| **Machine Learning** | Keras / TensorFlow | Used for building, training, and loading the Artificial Neural Network (ANN). | 
| **Frontend** | HTML5, CSS3 | Structure and styling of the user interface. | 
| **Dependencies** | Pandas, NumPy | Data handling and numerical operations. | 

## ⚙️ Local Setup and Installation

### Prerequisites

You need **Python 3.x** installed on your system.

### Step 1: Clone the Repository

git clone https://github.com/Swaran4/HealthyBeat-AI.git
cd HealthyBeat-AI


### Step 2: Create a Virtual Environment (Recommended)

It is highly recommended to use a virtual environment to manage dependencies and avoid conflicts with other projects.

Create the environment
python -m venv venv

Activate the environment
On Windows:
.\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate


### Step 3: Install Dependencies

All necessary libraries, including Flask, Keras, and TensorFlow, are listed in `requirements.txt`.

pip install -r requirements.txt


### Step 4: Run the Application

The application is run via the main Flask file, `app.py`.

python app.py


You will see output indicating the server is running, typically on port 5000:
`Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

Open your web browser and navigate to the address provided (usually `http://127.0.0.1:5000/`) to access the application.

## 🧠 Learning Project Notes: ANN in Keras

This project was a deep dive into implementing Artificial Neural Networks for a real-world classification problem.

* **Model File:** The pre-trained ANN is saved as `heart_model.h5` and loaded within `app.py`.

* **Model Script:** The training logic, feature engineering, and model definition are contained within `model.py` (for reference and retraining).

* **Input Data:** The model expects specific, standardized input features based on clinical data.

Feel free to explore `model.py` to understand the ANN architecture and training process!

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

## 📧 Contact

Project Link: \[https://www.google.com/search?q=https://github.com/Swaran4/HealthyBeat-AI\]
