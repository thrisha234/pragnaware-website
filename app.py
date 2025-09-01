from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder=".")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home1")
def home1():
    return render_template("homepage_1.html")

@app.route("/home2")
def home2():
    return render_template("homepage_2.html")

@app.route("/home3")
def home3():
    return render_template("homepage_3.html")

# Serve assets folder
@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

# Serve vendor folder
@app.route('/vendor/<path:filename>')
def vendor(filename):
    return send_from_directory('vendor', filename)

if __name__ == "__main__":
    app.run(debug=True)
