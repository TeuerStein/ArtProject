from art.models import Art
from art.forms import AddArtForm
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import (
	HttpResponse,
	HttpResponseRedirect,
)


def show_all_objects_from_art_model(request):
	''' Take all objects from Art model for showing with pagination '''

	all_objects = Art.objects.all()
	paginator = Paginator(all_objects, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'page_obj': page_obj
	}

	return render(request, 'index.html', context)

def show_current_object_from_art_model(request, object_id):
	''' Take the current object from Art model for showing on a page '''

	current_object = Art.objects.get(pk=object_id)

	context = {
		'current_object': current_object,
	}

	return render(request, 'current.html', context)

def work_with_object_after_true_validation(request, add_object_form):
	''' Save information about object after validation '''

	if 'img' in request.FILES:
		print('found it')
		add_object_form.img = request.FILES['img']

	add_object_form.save()

	return HttpResponseRedirect(reverse('index'))

def take_info_about_object_and_save(request):
	''' General work with object infomation
    and return a context for templates '''

	if request.method == 'POST':
		add_object_form = AddArtForm(request.POST, request.FILES)

		if add_object_form.is_valid():
			work_with_object_after_true_validation(request, add_object_form)

		else:
			print(add_object_form.errors)
			return HttpResponse(add_object_form.errors)

	else:
		add_object_form = AddArtForm()

	context = {
		'add_object_form': add_object_form,
	}

	return render(request, 'add_new_art_object.html', context)

def take_info_about_object_and_delete(request, object_id):
	''' General work with object infomation '''

	try:
		current_object = Art.objects.get(pk=object_id)

		current_object.delete()

		return HttpResponseRedirect(reverse('index'))
		
	except:
		return HttpResponseRedirect(reverse('index'))
