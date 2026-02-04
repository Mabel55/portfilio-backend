#  Portfolio Backend API

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0-black?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

This is the RESTful API that powers my personal portfolio website. It connects to a MySQL database to serve dynamic content including my projects, skills, and testimonials.

---

##  Quick Links

| Resource | Link |
| :--- | :--- |
| ** API Documentation** | [**View Postman Docs**](https://documenter.getpostman.com/view/51663183/2sBXVkCVNS) |
| ** Live Server Base URL** | `https://portfilio-backend-mbjp.onrender.com` |
| ** GitHub Repository** | [View Source Code](https://github.com/owoeyemo/owoeyemichael) |

---

## 🛠 Tech Stack

* **Framework:** Flask (Python)
* **Database:** MySQL (Cloud Hosted)
* **Database Driver:** mysql-connector-python
* **Querying:** Raw SQL (Optimized for performance)
* **Deployment:** Render Cloud Hosting

---

##  Key Features

* **Dynamic Content:** Fetches Projects, Skills, and Services directly from the MySQL database.
* **Error Handling:** Robust try/except blocks to prevent server crashes.
* **CORS Enabled:** Configured to allow secure requests from the frontend application.
* **Environment Security:** Uses `.env` files to keep database credentials safe.

---

##  API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/bio` | Fetches personal biography and resume stats |
| `GET` | `/api/projects` | Returns a list of all portfolio projects |
| `GET` | `/api/skills` | Returns technical skills list |
| `GET` | `/api/services` | Returns services offered |
| `GET` | `/api/testimonials` | Returns client testimonials |
| `POST` | `/api/contact` | Processes contact form submissions |

---

## 💻 Local Installation Guide

If you want to run this API on your local machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/owoeyemo/owoeyemichael.git](https://github.com/owoeyemo/owoeyemichael.git)
    cd owoeyemichael
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root folder and add your MySQL credentials:
    ```env
    DB_HOST=your_host
    DB_USER=your_user
    DB_PASSWORD=your_password
    DB_NAME=your_db_name
    DB_PORT=3306
    ```

5.  **Run the Server**
    ```bash
    python app.py
    ```
    The API will be available at `http://127.0.0.1:5000`.

---

###  Author
  Arua Mabel - *Backend Engineer*