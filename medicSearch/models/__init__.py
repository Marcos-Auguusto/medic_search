from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente'),
)

from .rating import rating
from .dayWeek import dayWeek
from .state import state
from .city import city
from .neighborhood import neighborhood
from .address import address
from .speciality import speciality
from .profile import Profile

