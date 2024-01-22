from django.db import models

class Reviews(models.Model):
    #user = models.ForeignKey('User', on_delete=models.CASCADE)
    user = models.CharField(max_length=90, default='User')
    text = models.CharField(max_length=90)

    def __str__(self):
        return self.text

class Film(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    year = models.SmallIntegerField()
    country = models.CharField(max_length=60)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    actors = models.ForeignKey('Actors', on_delete=models.CASCADE)
    genres = models.ForeignKey('Genres', on_delete=models.CASCADE)
    reviews = models.ForeignKey('Reviews', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Actors(models.Model):
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    description = models.TextField()
    # image = models.ImageField()
    def __str__(self):
        return  self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return  self.name

class Genres(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return  self.name
