# app.py

from flask import Flask, request, render_template
import os
from scanner import compute_hash, check_virustotal

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename == "":
            return render_template("index.html", error="No file selected.")

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file.filename)
        uploaded_file.save(file_path)

        file_hash = compute_hash(file_path)
        result = check_virustotal(file_hash)
        return render_template("result.html", hash=file_hash, result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)