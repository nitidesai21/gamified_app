from flask import Flask,render_template,redirect,url_for,request,session,flash,abort,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import create_engine
from lesson import lessons,get_lesson_by_id,get_lesson_by_subject
from datetime import datetime
from quiz import get_quizzes_by_lesson
#engine=create_engine('sqlite:///school_user.db')
#print("Database created successfully")
app=Flask(__name__)
app.config['SECRET_KEY']='rural'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///school_user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
@app.before_request
def setup():
    db.create_all()
    if not User.query.filter_by(username='student1').first():
        hashed_pw=generate_password_hash('student1@123',method='pbkdf2:sha256')
        user=User(username='student1',password=hashed_pw,role="student")
        db.session.add(user)
    if not User.query.filter_by(username='teacher1').first():
        hashed_pw = generate_password_hash('teacher1@123',method='pbkdf2:sha256')
        user = User(username='teacher1', password=hashed_pw, role="teacher")
        db.session.add(user)
    db.session.commit()
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    role=db.Column(db.String(10),nullable=False)
    points=db.Column(db.Integer,default=0)
class Score(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    lesson_id=db.Column(db.Integer,nullable=False)
    score=db.Column(db.Integer,nullable=False)
    total = db.Column(db.Integer, nullable=False)
    points_earned = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    user = db.relationship('User', backref=db.backref('scores', lazy=True))
class Story_lesson(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    content=db.Column(db.Text,nullable=False)
class Quiz(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    lesson_id=db.Column(db.Integer,db.ForeignKey('story_lesson.id'),nullable=False)
    question=db.Column(db.Text,nullable=False)
    answer=db.Column(db.String(200),nullable=False)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST': 
        username=request.form['username']
        password=request.form['password']
        role_form=request.form.get('role','student').lower()
        user=User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password,password) and user.role.lower()==role_form.lower():
            session['user_id']=user.id
            session['username']=user.username
            session['role']=user.role
            flash("Logged in successfully!",'success')
            if user.role.lower()=='student':
                return redirect(url_for('subjects'))
            else:
                return redirect(url_for('teacher_scores'))
            return redirect(url_for('subjects'))
        else:
            flash('Invalid credentials or not a student','Danger')
    return render_template('login.html')
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.",'Info')
    return redirect(url_for('login'))
@app.route('/subjects')
def subjects():
    if 'user_id' not in session:
        flash('Please log in.','warning')
        return redirect (url_for('login'))
    subject_list=['Maths','Science','English','Social Science']
    return render_template('subjects.html',subjects=subject_list)
@app.route('/lessons/<subject>')
def lessons(subject):
    if 'user_id' not in session:
        flash('Please log in.','warning')
        return redirect(url_for('login'))
    subject_lessons=get_lesson_by_subject(subject)
    if not subject_lessons:
        flash("No lessons found for this subject.",'danger')
        return redirect(url_for('subjects'))
    return render_template('lessons.html',lessons=subject_lessons,subject=subject)
@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    if 'user_id' not in session:
        flash('Pleas e log in.','warning')
        return redirect(url_for('login'))
    lesson=get_lesson_by_id(lesson_id)
    if not lesson:
        flash('Lesson not found','dannger')
        return redirect(url_for('subjects'))
    video_links = {
        1:"math.mp4",
        2:"science.mp4",
        3:"english.mp4",
        4:"ss.mp4"
    }
    video_url = video_links.get(lesson_id, "")

    return render_template("lesson_detail.html", lesson=lesson, video_url=video_url)
    #return render_template('lesson.html',lesson=lesson)
@app.route('/quiz/<int:lesson_id>', methods=['GET', 'POST'])
def quiz(lesson_id):
    if 'user_id' not in session:
        flash('Please log in.', 'warning')
        return redirect(url_for('login'))

    lang = session.get('language', 'english')
    quizzes_data = get_quizzes_by_lesson(lesson_id)

    # Localize quiz questions and answers based on the user's chosen language
    localized_quizzes = [
        {
            "question": q["question"].get(lang, q["question"]["english"]),
            "answer": q["answer"].get(lang, q["answer"]["english"])
        }
        for q in quizzes_data
    ]

    if request.method == 'POST':
        user = User.query.get(session['user_id'])
        correct_answers = 0
        total = len(localized_quizzes)
        for idx, quiz in enumerate(localized_quizzes):
            user_answer = request.form.get(str(idx), '').strip().lower()
            if user_answer == quiz['answer'].strip().lower():
                correct_answers += 1
        points_earned = correct_answers * 10
        user.points += points_earned
        score_record = Score(
            user_id=user.id,
            lesson_id=lesson_id,
            score=correct_answers,
            total=total,
            points_earned=points_earned,
            timestamp=datetime.utcnow()
        )
        db.session.add(score_record)
        db.session.commit()

        # Motivational message
        percentage = (correct_answers / total) * 100
        if percentage == 100:
            msg = "Perfect score! You are a super learner! 🌟"
        elif percentage >= 80:
            msg = "Great job! Keep up the excellent work! 👍"
        elif percentage >= 50:
            msg = "Good effort! Practice makes perfect! 💪"
        else:
            msg = "Don't give up! You can do better next time! 😊"

        return render_template(
            'quiz.html',
            score=correct_answers,
            total=total,
            points=points_earned,
            message=msg
        )

    return render_template('quiz.html', quizzes=enumerate(localized_quizzes), lesson_id=lesson_id)

@app.route('/teacher/scores')
def teacher_scores():
    if 'user_id' not in session:
        flash('Please log in.', 'warning')
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    if user.role != 'teacher':
        abort(403)
    scores = Score.query.join(User).order_by(Score.timestamp.desc()).all()
    return render_template('teacher_scores.html', scores=scores)
@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form.get('language')
    if lang in ['english', 'hindi', 'gujarati']:
        session['language'] = lang
    return redirect(request.referrer or url_for('subjects'))
if __name__=='__main__':
    app.run(debug=True)               