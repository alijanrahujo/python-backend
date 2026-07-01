from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oratec.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database extension
db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Task {self.id}>'
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    fathername = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    contact = db.Column(db.String(15), nullable=True)
    course = db.Column(db.String(255), nullable=True)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Task {self.id}>'


products = [
    {"id":1,"name":"HP Laptop G5","price":55000,"stock":4},
    {"id":2,"name":"HP Laptop G6","price":58000,"stock":3},
    {"id":3,"name":"HP Laptop G7","price":60000,"stock":7},
    {"id":4,"name":"HP Laptop G8","price":75000,"stock":9},
]
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


@app.route('/product')
def index():
    return render_template('product/index.html',products=products)

@app.route('/product/create',methods=['get','POST'])
def create():
    if request.method == "POST":
        new_product = {
            "id":products[-1]['id']+1,
            "name":request.form['name'],
            "price":request.form['price'],
            "stock":request.form['stock'],
        }

        products.append(new_product)
        return redirect(url_for('index'))
    return render_template('product/create.html')

# @app.route('/product/save',methods=['POST','get'])
# def save():
#     return request.method
#     return render_template('product/create.html')

@app.route('/task')
def Taskindex():
    tasks = Task.query.order_by(Task.id).all()
    return render_template('task/index.html',tasks=tasks)

@app.route('/task/create',methods=['get','POST'])
def Taskcreate():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')

        new_task = Task(title=name, description=description)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('Taskindex'))

    return render_template('task/create.html')

@app.route('/student')
def student():
    students = Student.query.order_by(Student.id).all()
    return render_template('student/index.html',students=students)

@app.route('/student/create',methods=['get','POST'])
def studentCreate():
    if request.method == "POST":
        name = request.form.get('name')
        fathername = request.form.get('fathername')
        dob = request.form.get('dob')
        contact = request.form.get('contact')
        course = request.form.get('course')
        
        dob = datetime.strptime(dob, "%Y-%m-%d").date() if dob else None

        query = Student(name=name,fathername=fathername,dob=dob,contact=contact,course=course)
        db.session.add(query)
        db.session.commit()
        return redirect(url_for('student'))
        
    return render_template('student/create.html')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)