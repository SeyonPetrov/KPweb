from flask import Flask, render_template, redirect
from data import db_session
from data.user import User
from data.files import Files
from flask_login import LoginManager, login_user, login_required, logout_user
from forms import RegisterForm, LoginForm, Form

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


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Form()
    return render_template('main_page.html', form=form)


@app.route('/reg', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    print('OPEN')
    if form.validate_on_submit():
        sess = db_session.create_session()

        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = form.age.data
        user.sex = form.sex.data
        user.phone_num = form.phone.data
        user.email = form.log.data
        user.set_password(form.password.data)

        sess.add(user)
        sess.commit()
        print('GOOD')
        return redirect('/', code=302)
    return render_template('reg_form.html', form=form)


@app.route('/log', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('log_form.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
