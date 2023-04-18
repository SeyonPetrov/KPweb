from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField, IntegerField, \
    RadioField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    place_job_study = StringField("Место работы/учёбы", validators=[DataRequired()])
    address = StringField("Город", validators=[DataRequired()])
    age = IntegerField("Возраст", validators=[DataRequired()])
    phone_num = StringField('Номер телефона', validators=[DataRequired()])
    sex = RadioField('Пол', choices=['Женский', 'Мужской'])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

