from flask import Flask, escape, request,render_template

app = Flask(__name__)

#adding another route '/home'
#so now it has 2 name can be called from brower
#lcalhost:5000
#or localhost:5000/home
#both return same page

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    #return f'<h1> Hello ME, {escape(name)}! </h1>'
    return render_template('home.html')


# creating another page
@app.route('/about')
def about():
    #return '<h1>About page </h1>'
    return render_template('about.html')

# to run this program using flask run
# without having to set environment variable
# FLASK_APP=fblog.py
# enter below if to indicate the main functions
if __name__ == '__main__':
    app.run(debug=True)

    
