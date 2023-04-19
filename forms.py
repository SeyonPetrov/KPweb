from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField, TelField
from wtforms.validators import DataRequired


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
    repeat_pw = PasswordField('', validators=[DataRequired()],
                              render_kw={'placeholder': 'ПОВТОРИТЕ ПАРОЛЬ'})


class LoginForm(FlaskForm):
    email = EmailField('', validators=[DataRequired()], render_kw={'placeholder': 'ВАША ПОЧТА'})
    password = PasswordField('', validators=[DataRequired()], render_kw={'placeholder': 'ВАШ ПАРОЛЬ'})
    but = SubmitField('ВОЙТИ')


class Form(FlaskForm):
    text = StringField('', validators=[DataRequired()], render_kw={
        'placeholder': 'Посмотреть портфолио по коду'
    })
    sub = SubmitField('СМОТРЕТЬ')