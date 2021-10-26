import mysql.connector

import click
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            # host=current_app.config['DATABASE_HOST'],
            # user=current_app.config['DATABASE_USER'],
            # password=current_app.config['DATABASE_PASSWORD'],
            # database=current_app.config['DATABASE']
            
            host = "localhost",
            user= "olimpo",
            password = "1234",
            database = "prueba"
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()

#180 las instruciones que importamos de schema se encuentran escrita dentro de una lista
def init_db():
    db, c = get_db()
    
    for i in instructions:
        c.execute(i)
        
    db.commit()
    
@click.command('init-db')
@with_appcontext
    
#180 llamar una funcion init_db que se crea arriba, en este momento se hace uso de la libreria click 
def init_db_command():
    init_db()
    click.echo('base de datos inicializada')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)        