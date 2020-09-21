from .services.art_services import (
	take_info_about_object_and_delete,
	take_info_about_object_and_save,
	show_all_objects_from_art_model,
	show_current_object_from_art_model,
)
from django.contrib.admin.views.decorators import staff_member_required


def show_all_from_art_model(request):
	''' Controller for showing the objects on a page '''

	show_objects = show_all_objects_from_art_model(request)

	return show_objects

def current_page_for_obj(request, object_id):
	''' Controller for showing the current object on a page '''

	show_corrent_object = show_current_object_from_art_model(request, object_id)

	return show_corrent_object

@staff_member_required(login_url='/permissionerror/')
def add_new_art_object(request):
	''' Controller for save new object '''

	add_info = take_info_about_object_and_save(request)

	return add_info

@staff_member_required(login_url='/permissionerror/')
def delete_art_object(request, object_id):
	''' Controller for delete current object '''

	delete_object = take_info_about_object_and_delete(request, object_id)

	return delete_object
