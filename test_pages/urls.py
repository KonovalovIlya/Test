from django.urls import path
from test_pages.views import form, user_list

urlpatterns = [
    path('', form, name='main'),
    path('users/', user_list, name='user_list')
]
