from app.course import Courses, Course
from app import app
from flask import render_template, redirect


@app.route('/')
@app.route('/courses')
def index():
    courses = Courses()
    coursesNames = courses.get_courses()
    return render_template('index.html', title="main page", customCss="home", courses=coursesNames)

@app.route('/courses/<coursename>')
def course(coursename):
    course = Course(coursename)
    courseContent = course.get_course_content()
    return render_template('course.html', title=coursename, customCss='course', courseContent=courseContent, courseName=coursename)
