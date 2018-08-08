''' A Module Description '''
from masonite.facades.Auth import Auth
from app.User import User

class LoginController(object):
    ''' Login Form Controller '''

    def __init__(self):
        pass

    def show(self, Request, Application):
        ''' Show the login page '''
        return view('auth/login', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request, Session):
        user = User.where('email', Request.input('email')).first()

        if user.active:
            if Auth(Request).login(Request.input('email'), Request.input('password')):
                return Request.redirect('/home')
            return Request.redirect('/login')
        else:
            Session.flash('warning', 'Please check your email to complete the registration process.')
            return Request.back()

    def logout(self, Request):
        Auth(Request).logout()
        return Request.redirect('/login')
