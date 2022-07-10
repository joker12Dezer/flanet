from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Ok: 200"
app.run(port=1169)