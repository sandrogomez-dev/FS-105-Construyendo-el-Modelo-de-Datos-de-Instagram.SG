# src/database/db.py

from flask_sqlalchemy import SQLAlchemy

# Crea una instancia de SQLAlchemy.
# Esta instancia no está vinculada a una aplicación Flask en este punto,
# se inicializará más tarde en app.py
db = SQLAlchemy()

# NOTA: En este enfoque con Flask-SQLAlchemy,
# ya no necesitamos 'create_engine', 'sessionmaker' ni 'declarative_base' aquí.
# db = SQLAlchemy() se encarga de todo eso internamente.
