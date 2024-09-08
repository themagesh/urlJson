from django.db import models

class NameURL(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name or self.url
