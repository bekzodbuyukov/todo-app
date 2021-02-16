import environ


# created instance of Env
env = environ.Env()


# read local .env file
env.read_env()


# reading variables from .env
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')