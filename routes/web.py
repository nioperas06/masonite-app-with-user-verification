''' Web Routes '''
from masonite.routes import Get, Post
from masonite.helpers.routes import get

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
]

ROUTES = ROUTES + [
    Get().route('/login', 'LoginController@show'),
    Get().route('/logout', 'LoginController@logout'),
    Post().route('/login', 'LoginController@store'),
    Get().route('/register', 'RegisterController@show'),
    Post().route('/register', 'RegisterController@store'),
    Get().route('/home', 'HomeController@show'),
    get('/activate/@token', 'RegisterController@validate')
]
