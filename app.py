from flask import Flask, render_template, request
from google.cloud.sql.connector import Connector
import pymysql
import sys
import sqlalchemy

app = Flask(__name__)

# Hardcoded database details
INSTANCE_CONNECTION_NAME = "boreal-graph-444300-j7:us-central1:personality-db"
DB_NAME = "personality_db"
DB_USER = "personality_user"
DB_PASS = "personality"

# Initialize Connector object
connector = Connector()

def get_connection():
    """Establishes a connection to the Cloud SQL instance."""
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pymysql",
        user=DB_USER,
        password=DB_PASS,
        db=DB_NAME
    )
    return conn

def test_connection():
    """Tests the database connection and exits if it fails."""
    try:
        conn = get_connection()
        conn.ping(reconnect=True)  # Tests the connection
        print("Database connection successful.")
    except Exception as e:
        print(f"Failed to connect to the database: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'conn' in locals():
            conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    total_users = 0  # Initialize the total user count

    # Get the total number of users from the database
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    cursor.close()
    conn.close()

    if request.method == "POST":
        answers = request.form
        scores = {"Sanguine": 0, "Choleric": 0, "Melancholic": 0, "Phlegmatic": 0}

        # Calculate scores for each temperament
        for key, value in answers.items():
            if key.startswith("sanguine"):
                scores["Sanguine"] += int(value)
            elif key.startswith("choleric"):
                scores["Choleric"] += int(value)
            elif key.startswith("melancholic"):
                scores["Melancholic"] += int(value)
            elif key.startswith("phlegmatic"):
                scores["Phlegmatic"] += int(value)
        
        # Determine dominant temperament
        dominant_type = max(scores, key=scores.get)

        # Get user email and ethnicity from the form
        email = request.form.get('email')
        ethnicity = request.form.get('ethnicity')

        conn = get_connection()
        cursor = conn.cursor()

        # Check if the user already exists
        query = "SELECT usage_count FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        if result:
            # User exists: increment usage count
            usage_count = result[0] + 1
            update_query = "UPDATE users SET usage_count = %s, ethnicity = %s, dominant_type = %s WHERE email = %s"
            cursor.execute(update_query, (usage_count, ethnicity, dominant_type, email))
        else:
            # New user: insert into the database
            insert_query = "INSERT INTO users (email, ethnicity, dominant_type, usage_count) VALUES (%s, %s, %s, 1)"
            cursor.execute(insert_query, (email, ethnicity, dominant_type))

        conn.commit()
        cursor.close()
        conn.close()

        return render_template("result.html", scores=scores, dominant_type=dominant_type, total_users=total_users)

    # Pass the total number of users to the template
    return render_template("index.html", total_users=total_users)

if __name__ == "__main__":
    # Test the database connection before starting the app
    test_connection()
    app.run(debug=True)
