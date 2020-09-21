from art import views
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    update_session_auth_hash,
)
from django.contrib.auth.forms import PasswordChangeForm
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse
from user.forms import (
    UserForm,
    UserProfileInfoForm,
    ChangeEmailForm,
    ChangePortfolioPageForm,
    ChangePortfolioPictureForm,
)
from user.models import UserProfileInfo


def work_with_info_after_true_validation(request, user_form, profile_form, registered):
    ''' Save info about User after validation
    and return True for 'registered' '''

    user = user_form.save()
    user.set_password(user.password)
    user.save()

    profile = profile_form.save(commit=False)
    profile.user = user

    if 'portfolio_picture' in request.FILES:
        print('found it')
        profile.portfolio_picture = request.FILES['portfolio_picture']

    profile.save()
    registered = True
    return registered

def validation_and_work_with_info(request, registered):
    ''' General work with User info
    and return a context for templates '''

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            work_with_info_after_true_validation(request, user_form, profile_form, registered)

        else:
            print(user_form.errors, profile_form.errors)
            return HttpResponse(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }

    return context

def login_process(request, user, username):
    ''' If info about User is correct - Log in
    or if incorrect return HttpResponse about error '''

    if user:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse(views.show_all_from_art_model))

        else:
            return HttpResponse('Your account was inactive.')

    else:
        print('Someone tried to login and failed.')
        print('They used username: {}'.format(username))
        return render(request, 'loginerror.html', {})

def after_true_method_verification_for_user_login(request):
    ''' Get a info about User and take it in 'login_process'
    and return him '''

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username, password = password)

    login_response = login_process(request, user, username)

    return login_response

def take_all_users_and_give_to_page(request):
    ''' Take all users and give they to page,
    for choose current User and show info about him
    and change some info '''

    all_users = UserProfileInfo.objects.all()

    context = {
        'all_users': all_users,
    }

    return context

def work_with_password_change_form_after_true_validation(request, change_form):
    ''' Save new password after validation '''

    user = change_form.save()
    update_session_auth_hash(request, user)
    messages.success(request, 'Your password was successfully updated!')

def validation_and_work_with_password_change_form(request):
    ''' General work with PasswordChangeForm
    and return a context for templates '''

    if request.method == 'POST':
        change_form = PasswordChangeForm(request.user, request.POST)
        if change_form.is_valid():

            work_with_password_change_form_after_true_validation(request, change_form)

            return HttpResponseRedirect(reverse('success_change'))

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        change_form = PasswordChangeForm(request.user)

    context = { 'change_form': change_form }

    return render(request, 'change_password_page.html', context)

def work_with_portfolio_picture_change_form(request):
    ''' General work with the ChangePortfolioPictureForm
    for change a portfolio picture '''

    all_users = UserProfileInfo.objects.all()
    change_form = ChangePortfolioPictureForm(request.POST, request.FILES)

    for current_user in all_users:
        if request.user == current_user.user:

            if change_form.is_valid():

                if current_user.portfolio_picture:
                    current_user.portfolio_picture.delete()
                current_user.portfolio_picture = change_form.save(commit=False)

                if 'portfolio_picture' in request.FILES:
                    print('found it')
                    current_user.portfolio_picture = request.FILES['portfolio_picture']

                current_user.save()

                return HttpResponseRedirect(reverse('success_change'))

            else:
                messages.error(request, change_form.errors)

def work_with_portfolio_page_change_form(request):
    ''' General work with the ChangePortfolioPageForm
    for change a portfolio page '''

    all_users = UserProfileInfo.objects.all()
    change_form = ChangePortfolioPageForm(request.POST)

    for current_user in all_users:
        if request.user == current_user.user:

            if change_form.is_valid():
                current_user.portfolio_page = change_form.save(commit=False)

                if 'portfolio_page' in request.POST:
                    print('found it')
                    current_user.portfolio_page = request.POST['portfolio_page']

                current_user.save()

                return HttpResponseRedirect(reverse('success_change'))

            else:
                messages.error(request, change_form.errors)

def work_with_email_change_form(request):
    ''' General work with the ChangeEmailForm
    for change a user email '''

    change_form = ChangeEmailForm(request.POST)

    if change_form.is_valid():
        request.user.email = change_form.save(commit=False)

        if 'email' in request.POST:
            print('found it')
            request.user.email = request.POST['email']

        request.user.save()

        return HttpResponseRedirect(reverse('success_change'))

    else:
        messages.error(request, change_form.errors)
