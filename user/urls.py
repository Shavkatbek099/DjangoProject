from django.http import HttpResponse
from django.urls import path
from user.views import user_login, user_logout, user_signup


urlpatterns = [
    path('login/', user_login, name="user_login_page"),
    path('logout/', user_logout, name="user_logout_page"),
    path('signup/', user_signup, name="user_signup_page"),
]
