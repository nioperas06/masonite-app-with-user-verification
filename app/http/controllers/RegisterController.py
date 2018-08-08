''' A Module Description '''
from masonite.facades.Auth import Auth
from config import auth
from app.notifications.EmailVerificationNotification import EmailVerificationNotification
from app.User import User
import bcrypt, jwt, os

class RegisterController(object):
    ''' Class Docstring Description '''

    def __init__(self):
        pass

    def show(self, Request, Application):
        ''' Show the registration page '''
        return view('auth/register', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request, Mail, Session, Notify):
        ''' Register a new user '''
        password = bytes(bcrypt.hashpw(
            bytes(Request.input('password'), 'utf-8'), bcrypt.gensalt()
        )).decode('utf-8')

        user = auth.AUTH['model'].create(
            name=Request.input('name'),
            password=password,
            email=Request.input('email'),
        )

        data = {'email': user.email}
        encoded = jwt.encode(data, os.environ.get('KEY'), algorithm='HS256')
        token = str(encoded, 'utf-8')

        if token:
            Notify.mail(EmailVerificationNotification, to=user.email, link='http://localhost:8000/activate/{0}'.format(token))
            Session.flash('success', 'Almost done! Please check your email to complete the registration process.')
            return Request.redirect('/login')

        return Request.redirect('/register')

    def validate(self, Request):
        if Request.param('token'):
            data = jwt.decode(Request.param('token'), os.environ.get('KEY'), algorithms=['HS256'])
            user = User.where('email', data['email']).first()
            
            if user:
                user.active = True
                user.save()
                Session.flash('success', 'You\'re in! Please login!')

        return Request.redirect('/login')