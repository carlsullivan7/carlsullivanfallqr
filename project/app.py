from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Tops page
@app.route("/tops")
def tops():
    return render_template("tops.html")

# Bottoms page
@app.route("/bottoms")
def bottoms():
    return render_template("bottoms.html")

# Outerwear page
@app.route("/outerwear")
def outerwear():
    return render_template("outerwear.html")

# Accessories page
@app.route("/accessories")
def accessories():
    return render_template("accessories.html")

if __name__ == "__main__":
    app.run(debug=True)


