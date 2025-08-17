from flask import Flask, render_template
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/demos")
def demos():
    return render_template("demos.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    
    port_env = int(os.environ.get("PORT", 8080))
    debug_env = int(os.environ.get("DEBUG", False))

    if debug_env:
        logger.info(f"Running in debug mode on port {port_env}")
    app.run(host="0.0.0.0", port=port_env, debug=debug_env)
