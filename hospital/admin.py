from django.contrib import admin
from django.apps import apps

# Register your models here.

# # Register your models here.
hospital_app = apps.get_app_config("hospital")
models = hospital_app.get_models()

for model in models:
    admin.site.register(model)
