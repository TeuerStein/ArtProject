from art.models import Art
from django.db.models import Q


def get_objects_from_model_with_filter(self):
	''' Take a object from the Art.model '''

	return Art.objects.filter(name__icontains = self.request.GET.get('q'))
