from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Médico'),
    (3, 'Paciente'),
)

from .rating import Rating
from .dayWeek import DayWeek
from .state import State
from .city import City
from .neighborhood import Neighborhood
from .address import Address
from .speciality import Speciality
from .profile import Profile

