from art.views import (
    add_new_art_object,
    current_page_for_obj,
    delete_art_object,
    show_all_from_art_model
)
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from search.views import Search
from user.views import (
    change_email,
    change_password,
    change_portfolio_page,
    change_portfolio_picture,
    have_not_permission,
    register,
    success_change,
    support,
    user_login,
    user_logout,
    user_personal_page,
)


urlpatterns = [
    path('add/', add_new_art_object, name='add'),
    path('admin/', admin.site.urls, name='admin'),
    path('art/<str:object_id>/', current_page_for_obj, name='current_page_for_obj'),
    path('art/delete/<str:object_id>/', delete_art_object, name='delete'),
    path('personalpage/changeimg/', change_portfolio_picture, name='change_portfolio_picture'),
    path('personalpage/changeemail/', change_email, name='change_email'),
    path('personalpage/changepassword/', change_password, name='change_password'),
    path('personalpage/changepage/', change_portfolio_page, name='change_portfolio_page'),
    path('personalpage/logout/', user_logout, name='user_logout'),
    path('personalpage/success', success_change, name='success_change'),
    path('personalpage/', user_personal_page, name='personal_page'),
    url(r'^login/$', user_login, name='login'),
    url(r'^registration/$', register, name='register'),
    path('permissionerror/', have_not_permission, name='have_not_permission'),
    path('support/', support, name='support'),
    path('search/', Search.as_view(), name = 'search'),
    path('', show_all_from_art_model, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
