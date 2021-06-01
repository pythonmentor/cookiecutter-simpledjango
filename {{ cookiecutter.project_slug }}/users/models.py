from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Utilisateur personnalisé pour mon projet sur mesure."""
