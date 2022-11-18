from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=30
    )
    lastname = models.CharField(
        max_length=50
    )
    birthday = models.DateField()
    email = models.EmailField(
        max_length=50
    )

    def __str__(self):
        return self.name
