from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#https://www.youtube.com/watch?v=mWBNI1cS0jg

#Definindo o model
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create_task():
    form_description = request.form['description']
    task_exists = Tasks.query.filter_by(descrption=form_description).first()
    if task_exists:
        return 'Error: Task already exists!', 400
    new_task = Tasks(description=form_description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@app.route('/delete<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5050)