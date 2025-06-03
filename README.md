
#  Crop Recommendation System

A web-based platform that leverages machine learning and real-time weather data to recommend optimal crops for smallholder farmers in Kenya. The system empowers farmers to make informed planting decisions based on soil and climatic conditions.

---

##  Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#️-prerequisites)
- [Installation](#-installation)
- [Database Setup (MySQL via XAMPP)](#️-database-setup-mysql-via-xampp)
- [ML Model Setup](#ml-model-setup)
- [Usage](#-usage)
- [Project Structure](#️-project-structure)



---

## 🚀 Features

- 📊 **ML-Based Crop Recommendations** using real-time user input and historical data.
- ☁️ **Weather Forecast Integration** via Open-Meteo API.
- 👥 **Role-based Access** for Farmers, NGOs, Government Agencies, and Admins.
- 🧑‍🌾 **Farmer Community Portal** for discussion and support.
- 📈 **Admin Dashboard** for system monitoring and user management.
- 🗓️ **Virtual Consultation (Coming Soon)**

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5, CSS3, Bootstrap

**Backend:**
- Django (Python)
- MySQL (via XAMPP)

**Machine Learning:**
- scikit-learn, pandas, numpy

**External APIs:**
- Open-Meteo API (for real-time weather data)

---

## 🧰 Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8+** – [Download Python](https://www.python.org/downloads/)
- **pip** – Python package manager
- **virtualenv** – For isolated development environment
- **Git** – [Download Git](https://git-scm.com/downloads)
- **XAMPP** – With MySQL enabled: [Download XAMPP](https://www.apachefriends.org/index.html)
- **MySQL Client Library**
  - `mysqlclient` or `pymysql` for Django support
- **A code editor** – (VSCode, PyCharm, etc.)

---

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Otieno-clinton/Crop_recommendation_final_project.git
   cd Croprecommend
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv myvenv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database** (see below)

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## 🗄️ Database Setup (MySQL via XAMPP)

1. **Start Apache and MySQL** using the XAMPP Control Panel.

2. **Create a new database**
   - Go to [http://localhost/phpmyadmin](http://localhost/phpmyadmin)
   - Click **"New"**, name your database (e.g., `crop_db`), and click **Create**

3. **Configure Django to use MySQL**

   In `settings.py`, update the `DATABASES` setting:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'crop_db',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Install MySQL client library**

   ```bash
   pip install mysqlclient
   ```

   *Alternatively, use `pymysql` if you face issues:*

   ```bash
   pip install pymysql
   ```

   Add this to `__init__.py` in your main project folder:

   ```python
   import pymysql
   pymysql.install_as_MySQLdb()
   ```

---

## 🤖 ML Model Setup

The core engine of this system is a **Random Forest Classifier** trained on historical crop data.

### 📈 Model Information

- **Algorithm**: Random Forest  
- **Input Features**:
  - Soil nutrients: `N`, `P`, `K`
  - Soil pH  
  - Climate: `Temperature`, `Humidity`, `Rainfall`  
- **Performance**:
  - Accuracy: ~99% on test set

### 📂 ML Files

- `Crop_recommendation.py`: Core script for prediction  
- `model.pkl`: Serialized trained model  
- `minmaxscaler.pkl`, `standardscaler.pkl`: Feature scaling tools  
- `crop_rec_model.ipynb`: Notebook for training and evaluation

### 🧠 ML Prediction Flow

1. User inputs: soil & weather values  
2. Scalers preprocess the data  
3. Trained model predicts the optimal crop  
4. Result shown in UI + optional explanation

---

## 🧪 Usage

- Register and log in as a specific user type.
- Input soil nutrient levels and view real-time weather data.
- Receive ML-based crop recommendations.
- Interact with other users in the community support portal.
- Admins can manage system settings and user roles.

---

CROPRECOMMEND/
├── Croprecommend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── recommendapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── crop_rec_model.ipynb
│   ├── Crop_recommendation.py
│   ├── forms.py
│   ├── minmaxscaler.pkl
│   ├── model.pkl
│   ├── models.py
│   ├── services.py
│   ├── standardcaler.pkl
│   ├── tests.py
│   └── views.py
├── static/
├── templates/
├── db.sqlite3
└── manage.py

```
