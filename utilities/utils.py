import os
from constants import ERR_MSG_TEMPLATE_ENVVAR_NOT_FOUND
from django.core.exceptions import ImproperlyConfigured


def get_env(variable_name: str, required=True):
    try:
        return os.environ[variable_name]
    except KeyError:
        if required:
            raise KeyError(
                ERR_MSG_TEMPLATE_ENVVAR_NOT_FOUND.format(var_name=variable_name)
            )
        pass
