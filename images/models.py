from django.db import models

class Image(models.Model):
    original = models.ImageField(upload_to='originals/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    big_thumb = models.ImageField(upload_to='big_thumbs/', blank=True, null=True)
    big_1920 = models.ImageField(upload_to='big_1920/', blank=True, null=True)
    d2500 = models.ImageField(upload_to='d2500/', blank=True, null=True)
    state = models.CharField(max_length=20, default='pending')
    project_id = models.IntegerField()

    def __str__(self):
        return f"Image {self.id} for project {self.project_id}"
