from django.urls import path
from collegeapp.views import *
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('newpage1', views.newpage1, name='newpage1'),
    path('newpage2', views.newpage2, name='newpage2'),
    path('application', views.application, name='application'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),
]