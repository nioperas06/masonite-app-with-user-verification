''' Web Routes '''
from masonite.helpers.routes import get, post

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
]

ROUTES = ROUTES + [
    get('/login', 'LoginController@show'),
    get('/logout', 'LoginController@logout'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/home', 'HomeController@show'),
    get('/activate/@token', 'RegisterController@validate')
]
