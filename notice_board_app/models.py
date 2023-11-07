from django.db import models
import PIL

class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='Photos/', null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
