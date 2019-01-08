from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
	vehicle_type = models.CharField(max_length=100)
	manufacturer = models.CharField(null=True, blank=True,max_length=100)
	model = models.CharField(null=True, blank=True, max_length=100)
	year_of_purchase = models.CharField(null=True, blank=True, max_length=4)
	place = models.CharField(null=True, blank=True, max_length=100)
	distance_travelled = models.CharField(null=True, blank=True, max_length=100)
	price = models.CharField(null=True, blank=True, max_length=100)
	mileage = models.CharField(null=True, blank=True, max_length=100)
	image = models.ImageField(default='default.jpg', upload_to='media')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.vehicle_type

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def save(self, *args, **kwargs):
		super(Post, self).save(*args, **kwargs)
		img = Image.open(self.image.path)
		
		if img.height > 400 or img.width > 400:
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)

