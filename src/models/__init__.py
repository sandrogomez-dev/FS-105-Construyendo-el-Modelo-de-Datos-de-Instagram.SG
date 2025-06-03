from database.db import db
from .index import *

# Esto hace que db y los modelos estén disponibles cuando hagas 'from models import ...'
__all__ = ['db'] + [m for m in dir() if not m.startswith('_')]
