from django.db import models

# Create your models here.

class CustomUser():
    ROLES = (
        (1, 'SuperAdmin'),
        (2, 'Guest'),
    )
    role=models.IntegerField(choices=ROLES)
