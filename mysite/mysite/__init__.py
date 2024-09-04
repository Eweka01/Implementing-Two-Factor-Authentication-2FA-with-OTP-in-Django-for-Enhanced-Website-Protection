from django.apps import apps

# Define a function that accesses the app configs and models
def get_app_info():
    # Access app configs and models only when needed
    app_configs = apps.get_app_configs()
    models = apps.get_models()
    return app_configs, models
