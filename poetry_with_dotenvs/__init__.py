import os

__version__ = '0.1.0'

def access_some_envs():
    """
    A simple function used to demonstrate accessing environment
    vars from within the contect of a virtual environment handled by Poetry
    """
    my_env_var = os.environ.get("MY_ENV_VAR")

    print(my_env_var)
