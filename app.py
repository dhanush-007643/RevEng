from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"id": 1, "name": "John", "dept": "CSE"},
    {"id": 2, "name": "Priya", "dept": "AI & DS"},
    {"id": 3, "name": "Rahul", "dept": "ECE"}
]

@app.route('/')
def home():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)