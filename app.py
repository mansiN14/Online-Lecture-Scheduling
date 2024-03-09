from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
class Instructor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lectures = db.relationship('Lecture', backref='instructor', lazy=True)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    lectures = db.relationship('Lecture', backref='course', lazy=True)

class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.id'), nullable=False)

def create_app():
    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        courses = Course.query.all()
        instructors = Instructor.query.all()
        lectures = Lecture.query.all()  # Query all lectures
        return render_template('index.html', courses=courses, instructors=instructors, lectures=lectures)

    @app.route('/add_course', methods=['POST'])
    def add_course():
        name = request.form['name']
        level = request.form['level']
        description = request.form['description']
        image = request.form['image']
        new_course = Course(name=name, level=level, description=description, image=image)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/add_instructor', methods=['POST'])
    def add_instructor():
        name = request.form['name']
        new_instructor = Instructor(name=name)
        db.session.add(new_instructor)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/assign_lecture', methods=['POST'])
    def assign_lecture():
        course_id = request.form['course_id']
        instructor_id = request.form['instructor_id']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        # Check for conflict
        existing_lecture = Lecture.query.filter_by(instructor_id=instructor_id, date=date).first()
        if existing_lecture:
            return "This instructor already has a lecture scheduled on this date.", 400
        lecture = Lecture(course_id=course_id, instructor_id=instructor_id, date=date)
        db.session.add(lecture)
        db.session.commit()
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
