from django.urls import path
from . import views
from .views import PostListView, PostDetailView, ContactFormView

app_name = 'ModuleRegistrationSystem'
urlpatterns = [
 path('', views.home, name = 'home'),
 path('about', views.about, name = 'about'),
 path('contact/', ContactFormView.as_view(), name = 'contact'),
#  path('coursepage', views.course, name = 'coursepage'),
 path('modulelist/<int:fk>', PostListView.as_view(), name = 'modules'),
 path('module/<int:pk>', PostDetailView.as_view(), name = 'module-detail'),
]