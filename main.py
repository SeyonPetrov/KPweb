from flask import Flask, render_template, redirect, abort, request, url_for
from data import db_session
from data.users import User
from forms.user import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import django

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/owners1.db")
    db_sess = db_session.create_session()
    @app.route("/")
    def index():
        js = url_for('static', filename='lg/jquery.js')
        glavccs = url_for('static', filename='lg/Главная.css')
        jvnicepage = url_for('static', filename='lg/nicepage.js')
        nicepageccs = url_for('static', filename='lg/nicepage.css')
        str1ccs = url_for('static', filename='lg/Страница-1.css')
        str2ccs = url_for('static', filename='lg/Страница-2.css')
        glav = url_for('index')
        reg = url_for('register')
        ou = url_for('login')
        db_sess = db_session.create_session()
        if current_user.is_authenticated:
            return render_template("Главная.html", js=jvnicepage, js2=js, glav=glav, glavcss=glavccs, str1=str1ccs, str2=str1ccs, ni=nicepageccs, reg=reg, log=ou)
        return render_template("Страница-2.html", js=jvnicepage, js2=js, glav=glav, glavcss=glavccs, str1=str1ccs, str2=str1ccs, ni=nicepageccs, reg=reg, log=ou)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = User(
                email=form.email.data,
                name=form.name.data,
                place_job_study=form.place_job_study.data,
                address=form.address.data,
                age=form.age.data,
                phone_num=form.phone_num.data,
                sex=form.sex.data
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)
        return render_template('login.html', title='Авторизация', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect("/")

    @app.route('/Страница-1.html', methods=['GET', 'POST'])
    def add_news():
        js = url_for('static', filename='lg/jquery.js')
        glavccs = url_for('static', filename='lg/Главная.css')
        jvnicepage = url_for('static', filename='lg/nicepage.js')
        nicepageccs = url_for('static', filename='lg/nicepage.css')
        str1ccs = url_for('static', filename='lg/Страница-1.css')
        str2ccs = url_for('static', filename='lg/Страница-2.css')
        glav = url_for('index')
        reg = url_for('register')
        ou = url_for('login')
        if current_user.is_authenticated:
            db_sess = db_session.create_session()
            user = current_user
            return render_template('Страница-1.html', js=jvnicepage, js2=js, glav=glav, glavcss=glavccs, str1=str1ccs, str2=str2ccs, ni=nicepageccs, current_user=user, reg=reg, log=ou)
        else:
            form = LoginForm()
            if form.validate_on_submit():
                db_sess = db_session.create_session()
                user = db_sess.query(User).filter(User.email == current_user).first()
                if user and user.check_password(form.password.data):
                    login_user(user, remember=form.remember_me.data)
                    return redirect("/")
                return render_template('login.html',
                                       message="Неправильный логин или пароль",
                                       form=form)
            return render_template('login.html', title='Авторизация', form=form)


    app.run()


if __name__ == '__main__':
    main()