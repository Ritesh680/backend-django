from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def create_user(name, email, password):
        hashed_password = make_password(password)
        user = User(name=name, email=email, password=hashed_password)
        user.save()
        return user

    @staticmethod
    def authenticate(email, password):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
        except User.DoesNotExist:
            pass
        return None
