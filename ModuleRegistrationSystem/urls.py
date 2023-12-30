from django.urls import path
from . import views
from .views import PostListView, PostDetailView, ContactFormView

app_name = 'ModuleRegistrationSystem'

urlpatterns = [
 path('', views.home, name = 'home'),
 path('about', views.about, name = 'about'),
 path('contact/', ContactFormView.as_view(), name = 'contact'),
#  path('courselist', Courselist.as_view(), name = 'courselist'),
 path('modulelist/<int:fk>', PostListView.as_view(), name = 'modules'),
 path('module/<int:pk>', PostDetailView.as_view(), name = 'module-detail'),
 path('register_module/<int:module_id>/', views.register_module, name='register_module'),
 path('unregister_module/<int:module_id>/', views.unregister_module, name='unregister_module'),
]