from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

