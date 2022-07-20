from django.db import models

# Create your models here.

class WebsiteInfo(models.Model):
	title = models.CharField(max_length=250)
	logo = models.ImageField(upload_to='media/websiteinfo/')
	gmap_link = models.CharField(max_length=250)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Website Information'
		verbose_name_plural = 'Website Informations'



class SliderImages(models.Model):
	date_uploaded = models.DateTimeField(auto_now_add=True)
	slider_image = models.ImageField(upload_to='media/sliderimages/')

	class Meta:
		verbose_name = 'Slider Image'
		verbose_name_plural = 'Slider Images'


class WhyUs(models.Model):
	title = models.CharField(max_length=250)
	content = models.TextField()


	class Meta:
		verbose_name = 'Why Us'
		verbose_name_plural = 'Why Us'








