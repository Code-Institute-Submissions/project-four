from django.db import models
from django.urls import reverse

class Category(models.Model):
	
	name = models.CharField(max_length=100)
	slug = models.SlugField(null=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

		def __str__(self):
			return self.name

class Product(models.Model):
	GRAPHITE = 'Graphite'
	MODERN = 'Modern'
	METAL = 'Metal'
	OVERSIZE = 'Oversize'
	WOOD = 'Wood'

	CATEGORY_GROUPS = [
		(GRAPHITE, 'Graphite'),
		(MODERN, 'Modern'),
		(METAL, 'Metal'),
		(OVERSIZE, 'Oversize'),
		(WOOD, 'Wood'),
	]
	category = models.ForeignKey(Category, on_delete=models.PROTECT, choices=CATEGORY_GROUPS)
	title = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(upload_to='images')
	slug = models.SlugField(null=False, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('products:product-detail', kwargs={'slug': self.slug})
