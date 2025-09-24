from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.forms import CustomAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
    path('register/', user_views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name="users/login.html",
            authentication_form=CustomAuthenticationForm
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
