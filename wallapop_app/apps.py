from django.apps import AppConfig



class WallapopAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wallapop_app'




class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals