from .forms import (
    ChangeEmailForm,
    ChangePortfolioPageForm,
    ChangePortfolioPictureForm,
)
from .services.user_services import (
    after_true_method_verification_for_user_login,
    take_all_users_and_give_to_page,
    validation_and_work_with_info,
    validation_and_work_with_password_change_form,
    work_with_email_change_form,
    work_with_portfolio_page_change_form,
    work_with_portfolio_picture_change_form,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse


@login_required
def special(request):
    ''' Controller for telling to User
    that he is authorized '''

    return render(request, 'logged_in.html', {})

@login_required
def user_logout(request):
    ''' Controller for logout '''

    logout(request)

    return HttpResponseRedirect('/')

def register(request):
    ''' Controller for registration page '''

    if request.user.is_authenticated:
        return special(request)

    else:
        registered = False

        context = validation_and_work_with_info(request, registered)

        return render(request, 'registration.html', context)

def user_login(request):
    ''' Controller for login page '''

    if request.user.is_authenticated:
        return special(request)

    else:
        if request.method == 'POST':
            return after_true_method_verification_for_user_login(request)

        else:
            return render(request, 'login.html', {})

@login_required
def user_personal_page(request):
    ''' Controller for show or change personal info about Users '''

    context = take_all_users_and_give_to_page(request)

    return render(request, 'personal_page.html', context)

def have_not_permission(request):
    ''' Controller for tell the User that is have not
    a permissions for add new objects '''

    return render(request, 'permissionerror.html', {})

@login_required
def change_portfolio_picture(request):
    ''' Controller for portfolio picture changer '''

    if request.method == 'POST':
        return work_with_portfolio_picture_change_form(request)

    else:
        change_form = ChangePortfolioPictureForm()

    context = { 'change_form': change_form }

    return render(request, 'change_portfolio_picture.html', context)

@login_required
def change_email(request):
    ''' Controller for email changer '''

    if request.method == 'POST':
        return work_with_email_change_form(request)

    else:
        change_form = ChangeEmailForm()

    context = { 'change_form': change_form }

    return render(request, 'change_email.html', context)

@login_required
def change_password(request):
    ''' Controller for password changer '''

    return validation_and_work_with_password_change_form(request)

@login_required
def change_portfolio_page(request):
    ''' Controller for portfolio picture changer '''

    if request.method == 'POST':
        return work_with_portfolio_page_change_form(request)

    else:
        change_form = ChangePortfolioPageForm()

    context = { 'change_form': change_form }

    return render(request, 'change_portfolio_page.html', context)

def success_change(request):
    ''' Controller for telling to User that a
    change password was completed '''

    return render(request, 'success_change.html', {})

def support(request):
    ''' Controller for support page '''

    return render(request, 'support.html', {})
