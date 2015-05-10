from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #el verbose_name nos sirve para renombrar un campo de la base de datos en el admin de django
    about = models.CharField(max_length=50, verbose_name='acerca', blank=True)

    def __str__(self):
        return self.user.username


class Categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=800)
    category = models.ForeignKey(Categorie)
    user = models.ForeignKey(UserProfile)
    fecha = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    commentary = models.TextField(max_length=600)
    user = models.ForeignKey(UserProfile)


    def __str__(self):
        return str(self.post)
