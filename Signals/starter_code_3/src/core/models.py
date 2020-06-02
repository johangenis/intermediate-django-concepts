from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class PostQueryset(models.QuerySet):
    def valid(self):
        return self.filter(valid=True)

    def in_valid(self):
        return self.filter(valid=False)

class PostManager(models.Manager):
    # def get_queryset(self):
    #     return super().get_queryset()

    def get_queryset(self):
        return PostQueryset(self.model, using=self._db)

    def valid(self):
        return self.get_queryset().valid()

    def in_valid(self):
        return self.get_queryset().in_valid()

class Post(models.Model):
    title = models.CharField(max_length=20)
    valid = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title


def post_model_post_save_receiver(sender, *args, **kwargs):
    print("The save method was called")

post_save.connect(post_model_post_save_receiver, sender=Post)


@receiver(post_delete)
def post_model_post_delete_receiver(sender, *args, **kwargs):
    print("The delete method was called")