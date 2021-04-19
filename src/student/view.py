from flask import render_template, url_for, redirect
from src.model import db
from src.student import student
from src.model.student import Student
from src.student.forms import StudentForm
from flask_login import login_required



@student.route('/student') # индексная страница http://localhost/student
@login_required
def index():
	students=Student.query.all()	
	return render_template('student/index.html', students=students)


@student.route('/add', methods=['POST', 'GET']) # добавление новой записи http://localhost/student/add
def add_student():
	# часть функционала обрабатывает GET, а часть POST запросы, сделаем условие
	form = StudentForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		phone = form.phone.data
		try:
			student = Student(name=name, email=email, phone=phone)
			db.session.add(student)
			db.session.commit()
		except:
			print('Что -то пошло не так')
		return redirect(url_for('students.index')) # возврат на пустую форму
	#form = StudentForm() # иначе вернем форму
	return render_template('student/add_student.html', form=form)


@student.route('/delete_student/<student_id>', methods=('GET','POST')) # удаление записи http://localhost/student/delete_student/<student_id>
def delete_student(student_id):
	# удаление записей о студентах
	try:
		student = Student.query.filter_by(id=student_id).first_or_404()
		db.session.delete(student)
		db.session.commit()
		flash('Запись была удалена', 'danger')
	except:
		print('Что-то пошло не так')		
	return redirect(url_for('students.index'))
