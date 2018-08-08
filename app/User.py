''' User Model '''
from config.database import Model

class User(Model):
    ''' User Model '''

    __fillable__ = ['name', 'email', 'password', 'active']

    __auth__ = 'email'
