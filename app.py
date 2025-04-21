from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#Definindo o model
# class Tasks(db.Model):
#     id = db.column(db.Integer)
#     description = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    # tasks = Tasks.query.all()
    tasks = ['t1', 't2']

    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5050)