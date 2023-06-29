from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class post (models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField(max_length=1000)
    created_at=models.DateField( default=timezone.now)
    image=models.ImageField(upload_to='post-img/')

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
