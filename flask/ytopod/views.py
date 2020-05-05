from ytopod import app

@app.route("/")
def index():
    return "Hello Wotld"