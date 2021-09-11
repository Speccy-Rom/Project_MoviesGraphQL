from django.db import models


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    description = models.TextField("Описание")
    country = models.CharField("Страна", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
