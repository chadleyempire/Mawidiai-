from flask import Flask, render_template, request
import os

app = Flask(__name__)

# folder ya kuhifadhi nyimbo
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# coins za mwanzo
coins = 100


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    global coins

    if request.method == "POST":

        if coins < 10:
            return "❌ Huna coins za kutosha kupakia wimbo"

        file = request.files.get("song")

        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

            coins -= 10

            return f"""
            ✅ Wimbo umeuploadiwa vizuri!<br>
            💰 Coins zilizobaki: {coins}<br><br>
            <a href="/">Rudi Home</a>
            """

        return "Hakuna file iliyochaguliwa"

    return render_template("upload.html")


@app.route("/buy-coins")
def buy_coins():
    global coins

    coins += 50

    return f"""
    💰 Umeongeza coins 50!<br>
    Coins zako sasa ni: {coins}<br><br>
    <a href="/">Rudi Home</a>
    """


@app.route("/coins")
def show_coins():
    return f"""
    💰 Coins zako: {coins}<br><br>
    <a href="/">Rudi Home</a>
    """


@app.route("/promotion")
def promotion():
    global coins

    if coins < 20:
        return "❌ Huna coins za promotion"

    coins -= 20

    return f"""
    📢 Promotion imeanzishwa!<br>
    💰 Coins zilizobaki: {coins}<br><br>
    <a href="/">Rudi Home</a>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
