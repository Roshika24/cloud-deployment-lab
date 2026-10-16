
from flask import Flask

app = Flask(__name__)

YOUR_NAME = "Roshika Mishra"
APP_VERSION = "1.0.0"


@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Cloud Deployment Lab</title>
        </head>
        <body>
            <h1>Welcome to My Application!</h1>
            <p>Created by: {YOUR_NAME}</p>
            <p>Application Version: {APP_VERSION}</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
