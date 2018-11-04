from django.db import models
from django.urls import reverse


class FileModel(models.Model):
    file = models.FileField()

    def get_url(self):
        return reverse('file_handler', args=(self.id,))
