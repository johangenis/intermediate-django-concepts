from django.db import models


class PostManager(models.Manager):
    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        # queryset = queryset # TODO
        return super().get_queryset()

    def valid(self):
        return self.get_queryset().filter(valid=True)


class Post(models.Model):
    title = models.CharField(max_length=20)
    valid = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title
