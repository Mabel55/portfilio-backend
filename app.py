import os
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    # Print this so we can SEE in the terminal where it connects
    print("🔌 CONNECTING TO LOCALHOST (YOUR LAPTOP)...")
    
    conn = mysql.connector.connect(
        host='localhost',          # <--- Looking at your laptop
        user='root',
        password='1234',           # <--- Your local password
        database='portfolio_db'
    )
    return conn
    
    # Fallback (Just in case)
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT', 3306))
    )

# --- ENDPOINTS ---

@app.route('/api/bio')
def get_bio():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM bio WHERE id =1')
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify(data) if data else (jsonify({"error": "No bio found"}), 404)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/projects')
def get_projects():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM projects')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/skills')
def get_skills():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM skills')
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/testimonials')
def get_testimonials():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM testimonials')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

@app.route('/api/contact', methods=['POST'])
def contact_form():
    try:
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (data.get('name'), data.get('email'), data.get('message')))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Message sent!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)