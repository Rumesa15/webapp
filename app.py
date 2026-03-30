from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello This is RUMESA hosted an app using azure application service!!! 🚀"

if __name__ == "__main__":
    app.run()
