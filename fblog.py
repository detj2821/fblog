from flask import Flask, escape, request,render_template

app = Flask(__name__)

posts = [
    {'author':'Mr One',
    'title': 'Blog 1',
    'content':'First Post content',
    'date_posted': 'August,13,2020'
    },
    {'author':'Mr Two',
    'title': 'Blog 2',
    'content':'2nd Post content',
    'date_posted': 'July,3,2020'
    }

]

@app.route('/')
@app.route('/home')
def home():
    name = request.args.get("name", "World")
    #return f'<h1> Hello ME, {escape(name)}! </h1>'
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    #return '<h1>About page </h1>'
    return render_template('about.html',title='About f blog')

if __name__ == '__main__':
    app.run(debug=True)

    
