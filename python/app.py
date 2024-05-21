from flask import Flask
app = Flask(__name__)

#simple route app
@app.route("/")
def hello():
    return "Hello ACGBILI Students!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
