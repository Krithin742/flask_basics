from flask import Flask , render_template
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"
@app.route('/about')
def about():
    return "<h1>About Us</h1> <p>This is the about page.</p>"
@app.route('/contact')
def contact():
    return render_template("index.html")
@app.route('/jinja-basics')
def jinja_basics():
    user_name = "Rithin"
    return f"<h1>Hello, {user_name}<h1> <p>This is a simple HTML template.</p>"  




if __name__ == '__main__':
    app.run(debug=True)
