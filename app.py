from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "song" not in request.files:
            return "No file selected"

        file = request.files["song"]

        if file.filename == "":
            return "No file selected"

        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

        return "✅ Song uploaded successfully!"

    return render_template("upload.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
