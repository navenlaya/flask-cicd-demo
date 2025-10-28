from flask import Flask

app = Flask(__name__)

@app.route("/")

@app.route("/")
def home():
    return (
        "<h1>Hello from Flask CI/CD Demo v2!</h1>"
        "<p>Automatic Build → Test → Deploy via GitHub Actions.</p>"
    )

if __name__=="__main__":
    app.run (host="0.0.0.0", port=8080) 
