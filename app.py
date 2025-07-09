from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Read database connection info from environment variables
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'flaskdb')
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASS = os.environ.get('DB_PASS', 'postgres')

@app.route('/')
def home():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f'✅ Hello from Poornesh! Connected to PostgreSQL {db_version}'
    except Exception as e:
        return f'❌ Failed to connect to database: {e}'

@app.route('/users')
def users():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute('SELECT id, name FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    Triggering redeploy to Azure
