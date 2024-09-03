import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "social_nest.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import social_nest.users.signals  # noqa: F401
