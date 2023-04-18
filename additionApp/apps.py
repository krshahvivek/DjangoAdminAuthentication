from django.apps import AppConfig


class AdditionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'additionApp'

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'additionApp'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender, **kwargs):
            user = kwargs["instance"]
            if kwargs['created']:
                group, ok = Group.objects.get_or_create(name="default")
                group.user_set.add(user)

        post_save.connect(add_to_default_group,
                          sender=settings.AUTH_USER_MODEL)