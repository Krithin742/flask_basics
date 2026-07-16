from flask import Flask , render_template,request
 #importing flask module and render_template function
app = Flask(__name__) #application instance
@app.route('/') #index route
def home(): #route function
    return render_template("home.html") #rendering the base.html template

@app.route('/about')
def about():
    return render_template("about.html") #rendering the about.html template

@app.route('/contact')
def contact():
    return render_template("index.html",name="Rithin",age=21)
@app.route('/jinja-basics')
def home_page():
    user_name = "Rithin"
    return f"<h1>Hello, {user_name}</h1> <p>This is a simple HTML template.</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here
        return render_template("index.html", name=username, age=21)  # Example: Redirect to index page after login
    return render_template("login.html")





if __name__ == '__main__':
    app.run(debug=True)
