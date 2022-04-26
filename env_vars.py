from utilities.utils import get_env


DJANGO_SECRET_KEY = get_env(variable_name="DJANGO_SECRET_KEY")
ENVIRONMENT = get_env(variable_name="ENVIRONMENT")
