import functools

from flask import (
    Blueprint, flash, g, render_template, request, url_for, session 
)

from werkzeug.security import check_password_hash, generate_password_hash

from task.db import get_db

bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select id from user where username = %s'

        )
        if not username:
            error = 'username es requerido'
        if not password:
            error = 'password es requerido'
        elif c.fetchone() is not None:
            error = 'Usuario {} se encuentra registrado.'.format(username)
            
        if error is None:
            c.execute(
                'insert into user (username, password) values (%S, %s)',
                (username, generate_password_hash(password))
            )
            db.commit()
            
            return redirect(url_for('auth.login'))
        flash(error)
        
    return render_template('auth/register.html')
            
        