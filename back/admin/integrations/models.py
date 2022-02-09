import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from fernet_fields import EncryptedTextField

INTEGRATION_OPTIONS = (
    (0, "Slack bot"),
    (1, "Slack account creation"),
    (2, "Google account creation"),
    (3, "Google Login"),
    (4, "Asana"),
)
INTEGRATION_OPTIONS_URLS = [
    {
        "create_url": reverse_lazy("settings:slack-bot"),
        "disable_url": reverse_lazy("settings:google-login"),
        "extra_action_url": "settings:slack-account-update-channels",
        "extra_action_text": "Update Slack channels list",
    },
    {
        "create_url": reverse_lazy("settings:slack-account"),
        "disable_url": reverse_lazy("settings:google-login"),
    },
    {
        "create_url": reverse_lazy("settings:google-account"),
        "disable_url": reverse_lazy("settings:google-account"),
    },
    {
        "create_url": reverse_lazy("settings:google-login"),
        "disable_url": reverse_lazy("settings:google-account"),
    },
    {
        "create_url": reverse_lazy("settings:asana"),
        "disable_url": reverse_lazy("settings:asana"),
    },
]

class AccessTokenManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def account_provision_options(self):
        # Add items here that are meant for account creation. Making it static, as this won't change.
        return self.get_queryset().filter(integration__in=[1,2,4])


class AccessToken(models.Model):
    integration = models.IntegerField(choices=INTEGRATION_OPTIONS)
    token = EncryptedTextField(max_length=10000, default="", blank=True)
    refresh_token = EncryptedTextField(max_length=10000, default="", blank=True)
    base_url = models.CharField(max_length=22300, default="", blank=True)
    redirect_url = models.CharField(max_length=22300, default="", blank=True)
    account_id = models.CharField(max_length=22300, default="", blank=True)
    active = models.BooleanField(default=True)
    ttl = models.IntegerField(null=True, blank=True)
    expiring = models.DateTimeField(null=True, blank=True)
    one_time_auth_code = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True
    )

    # Slack
    app_id = models.CharField(max_length=100, default="")
    client_id = models.CharField(max_length=100, default="")
    client_secret = models.CharField(max_length=100, default="")
    signing_secret = models.CharField(max_length=100, default="")
    verification_token = models.CharField(max_length=100, default="")
    bot_token = EncryptedTextField(max_length=10000, default="", blank=True)
    bot_id = models.CharField(max_length=100, default="")

    @property
    def name(self):
        return self.get_integration_display()

    def api_class(self):
        from .slack import Slack
        from .asana import Asana
        from .google import Google
        if self.integration == 1:
            return Slack()
        if self.integration == 3:
            return Google()
        if self.integration == 4:
            return Asana()

    def add_user_form_class(self):
        from .forms import AddSlackUserForm, AddGoogleUserForm, AddAsanaUserForm
        if self.integration == 1:
            return AddSlackUserForm()
        if self.integration == 3:
            return AddGoogleUserForm()
        if self.integration == 4:
            return AddAsanaUserForm

    def add_user(self, user, params):
        self.api_class().add_user(user, params)

    objects = AccessTokenManager()

