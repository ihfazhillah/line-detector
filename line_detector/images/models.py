from django.db import models
from django.contrib.postgres.fields import JSONField

from django.db.models.signals import post_save


# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to="lines/")
    title = models.CharField(max_length=255, null=True, blank=True)
    options = JSONField(null=True, blank=True)
    scale = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


def after_post_image(sender, instance, created, **kwargs):
    if created:
        if not instance.title:
            instance.title = f"Line Image #{instance.id}"
            instance.save()


post_save.connect(after_post_image, sender=Image)
