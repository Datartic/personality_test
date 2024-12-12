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
    pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=get_connection,
)
    print("This is pool",pool)
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

        # Determine the dominant temperament
        dominant_type = max(scores, key=scores.get)

        # Get user email and ethnicity from the form
        email = request.form.get("email")
        ethnicity = request.form.get("ethnicity")

        # Insert user data into the database
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO users (email, ethnicity, dominant_type)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(query, (email, ethnicity, dominant_type))
                conn.commit()
        finally:
            conn.close()

        return render_template("result.html", scores=scores, dominant_type=dominant_type)

    return render_template("index.html")

if __name__ == "__main__":
    # Test the database connection before starting the app
    test_connection()
    app.run(debug=True)
