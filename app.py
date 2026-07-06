import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

coins = 100


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    global coins

    if request.method == "POST":
        if coins < 10:
            return "❌ Huna coins za kutosha."

        file = request.files.get("song")

        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            coins -= 10
            return f"✅ Upload successful. Coins zilizosalia: {coins}"

        return "No file selected"

    return render_template("upload.html")


@app.route("/buy-coins")
def buy_coins():
    global coins
    coins += 50
    return f"💰 Umenunua coins! Sasa una {coins}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
