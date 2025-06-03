
# 🌱 Crop Recommendation System

A web-based platform that leverages machine learning and real-time weather data to recommend optimal crops for smallholder farmers in Kenya. The system empowers farmers to make informed planting decisions based on soil and climatic conditions.

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Database Setup (MySQL via XAMPP)](#️-database-setup-mysql-via-xampp)
- [Usage](#-usage)
- [Machine Learning Model](#-machine-learning-model)
- [Project Structure](#️-project-structure)
- [Team](#-team)
- [License](#-license)

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

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
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

## 🧪 Usage

- Register and log in as a specific user type.
- Input soil nutrient levels and view real-time weather data.
- Receive ML-based crop recommendations.
- Interact with other users in the community support portal.
- Admins can manage system settings and user roles.

---

## 🤖 Machine Learning Model

- **Input Features**: Nitrogen, Phosphorus, Potassium, pH, Temperature, Humidity, Rainfall
- **Model Used**: [Random Forest / XGBoost — edit as needed]
- **Accuracy**: XX% on test dataset
- **Training Notebook**: Located in `ml_model/training.ipynb`

---

## 🗂️ Project Structure

```
crop_recommendation_system/
├── core/               # Common logic and shared models
├── farmers/            # Farmer-specific functionality
├── ml_model/           # ML model and prediction scripts
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👥 Team

- **Clinton Oluoch** – Project Manager
- **Jared Odhiambo** – Front-End Developer
- **Brian Omondi** – Machine Learning Engineer
- **Abraham Senteu** – Community Support & Content Strategist

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
