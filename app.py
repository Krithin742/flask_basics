from flask import Flask , render_template,request
 #importing flask module and render_template function
app = Flask(__name__) #application instance
@app.route('/') #index route
def home(): #route function
    return "Hello, World!"
@app.route('/about')
def about():
    return "<h1>About Us</h1> <p>This is the about page.</p>"
@app.route('/contact')
def contact():
    return render_template("index.html",name="Rithin",age=21)
@app.route('/jinja-basics')
def jinja_basics():
    user_name = "Rithin"
    return f"<h1>Hello, {user_name}<h1> <p>This is a simple HTML template.</p>"  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here
        return f"<h1> username is {username} and password is {password}</h1>"
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
