from flask import Flask, render_template, request

app = Flask(__name__)

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
        
        # Find dominant temperament
        dominant_type = max(scores, key=scores.get)
        return render_template("result.html", scores=scores, dominant_type=dominant_type)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)