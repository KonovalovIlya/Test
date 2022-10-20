from django.shortcuts import render, redirect
from test_pages.models import User
from test_pages.forms import UserForm


def form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            # user = \
            User.objects.create(name=name, surname=surname)
            return redirect('')
    form = UserForm()
    return render(request, 'test_pages/main.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'test_pages/users_list.html', {'users':users})
