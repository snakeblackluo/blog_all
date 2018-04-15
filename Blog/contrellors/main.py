# coding=utf-8

from flask import Blueprint,redirect, url_for, flash, render_template
from Blog.form.forms import LoginForm, RegisterForm
from Blog.models.blogs import User, db

main_bluepint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

@main_bluepint.route('/')
def index():
    return redirect(url_for('blog.home'))



@main_bluepint.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate.on_submit():
        flash('You have been logged in .', category='success')
        return redirect(url_for('blog.home'))
    return render_template('login.heml', form=form)


@main_bluepint.route('/logout', method=['GET', 'POST'])
def logout():
    flash('You have ben logged out.', category='success')
    return redirect(url_for('.home'))


@main_bluepint.route('/register', method=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.username = form.username.data
        new_user.set_password(form.username.data)

        db.session.add(new_user)
        db.session.commit()

        flash(
            'You user has been create, please login.',
            category='success'
        )

        return redirect(url_for('.login'))
    return render_template('register.html', form=form)








