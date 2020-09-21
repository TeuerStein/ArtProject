from django.db import models


class Art(models.Model):
	''' Art model '''

	name = models.CharField(max_length=50, verbose_name='Name', unique=True)
	content = models.TextField(null=True, blank=True, verbose_name='Content')
	img = models.ImageField(verbose_name='Image')

	def __srt__(self):
		return self.name
