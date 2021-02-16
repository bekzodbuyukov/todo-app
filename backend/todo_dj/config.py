import environ


# created instance of Env
env = environ.Env()


# read local .env file
env.read_env()


# reading variables from .env
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
API_TITLE = env('API_TITLE')
API_DEFAULT_VERSION = env('API_DEFAULT_VERSION')
API_DESCRIPTION = env('API_DESCRIPTION')