import os

from flask import Flask

#178 metodo para hacer testing en nuestra app o crear varias intancias de nuestra aplicacion
def create_app():
    app = Flask(__name__)
    
    #178 from.mapping nos permite definir variables de configuracion
    app.config.from_mapping(
        #178 variables de entorno
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )
    
    from . import db
    
    db.init_app(app)
    
    from . import auth
    
    app.register.blueprint(auth.bg)
    
    @app.route('/hola')
    def hola():
        return 'hola'
    
    return app
