from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/contact')
def ali():
    return render_template('contact.html')

# @app.route('/lec4')
# def lec4():
#     return render_template('lec 4.html')

# @app.route('/lec4/<name>')
# def lec4(name):

#     return render_template('lec 4.html',name=name)   

# @app.route('/lec4/<username>')
# def lec4(username):
#     return render_template('lec 4.html',name=username) 

@app.route('/lec4/<username>/<table>')
def lec4(username,table):
    return render_template('lec 4.html',name=username,table=table)   

if __name__ == "__main__":
    app.run(debug=True)