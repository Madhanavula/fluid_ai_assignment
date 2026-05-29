from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

@app.route('/')
def home():
    return "DevOps Kubernetes Challenge Running Successfully"

@app.route('/health')
def health():
    return "OK", 200

@app.route('/db')
def db_check():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = conn.cursor()
        cursor.execute("SELECT NOW()")
        result = cursor.fetchone()

        return f"Database Connected Successfully: {result}"

    except Exception as e:
        return f"Database Connection Failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
