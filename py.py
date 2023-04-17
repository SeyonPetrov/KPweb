from flask import Flask, render_template, url_for, redirect, jsonify
from flask_wtf import FlaskForm
from data import db_session
from data.user import User
from data.files import Files
from flask_login import LoginManager, login_user, login_required, logout_user
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField, TelField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwertyuiopasdfghjkl;zxcvbnm,'

login = LoginManager()
login.init_app(app)
db_session.global_init('db/owners.db')


@login.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


class LoginForm(FlaskForm):
    email = EmailField('', validators=[DataRequired()], render_kw={'placeholder': 'ВАША ПОЧТА'})
    password = PasswordField('', validators=[DataRequired()], render_kw={'placeholder': 'ВАШ ПАРОЛЬ'})
    but = SubmitField('ВОЙТИ')


class Form(FlaskForm):
    text = StringField('', validators=[DataRequired()], render_kw={
        'placeholder': 'Посмотреть портфолио по коду'
    })
    sub = SubmitField('СМОТРЕТЬ')


class RegisterForm(FlaskForm):
    but = SubmitField('ПРОДОЛЖИТЬ')
    name = StringField('', validators=[DataRequired()], render_kw={
        'placeholder': 'ИМЯ'
    })
    surname = StringField('', validators=[DataRequired()], render_kw={
        'placeholder': 'ФАМИЛИЯ'
    })
    age = SelectField('ВАШ ВОЗРАСТ', validators=[DataRequired()], choices=range(100),
                      render_kw={'placeholder': 'ВОЗРАСТ'})
    sex = SelectField('ВАШ ПОЛ', validators=[DataRequired()], choices=['Мужской', 'Женский'])
    phone = TelField('', validators=[DataRequired()], render_kw={
        'placeholder': 'НОМЕР ТЕЛЕФОНА'
    })
    log = EmailField('', validators=[DataRequired()],
                     render_kw={'placeholder': 'ПРИДУМАЙТЕ ЛОГИН'})
    password = PasswordField('', validators=[DataRequired()],
                             render_kw={'placeholder': 'ПРИДУМАЙТЕ ПАРОЛЬ'})


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Form()
    log_form = LoginForm()
    reg_form = RegisterForm()
    css = url_for('static', filename='css/css.css')
    if reg_form.validate_on_submit():
        registration(reg_form)
    return render_template('main_page.html', form=form, css=css, lg=log_form, reg=reg_form)


def registration(form):
    sess = db_session.create_session()
    if sess.query(User).filter(User.email == str(form.log.data)).first():
        return render_template('/', form=form, message='Такой пользователь уже есть')

    user = User()
    user.email = form.log.data
    user.name = form.name.data
    user.surname = form.surname.data
    user.sex = form.sex.data
    user.age = form.age.data
    user.set_password(form.password.data)
    user.phone_num = form.phone.data

    sess.add(user)
    sess.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
