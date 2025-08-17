from flask import Flask, redirect, url_for, session, request
from google_auth_oauthlib.flow import Flow
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Dev only

CLIENT_SECRETS_FILE = "client_secret.json"  # downloaded from GCP

SCOPES = ["https://www.googleapis.com/auth/userinfo.profile",
          "https://www.googleapis.com/auth/userinfo.email", "openid"]

@app.route("/")
def index():
    return '<a href="/login">Login with Google</a>'

@app.route("/login")
def login():
    return 'You are logged in'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
