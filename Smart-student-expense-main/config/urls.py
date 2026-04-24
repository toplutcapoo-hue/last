
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'), # Add this line
    path('', include('core.urls')),
]
