from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

app_name = 'ModuleRegistrationSystem'
urlpatterns = [
 path('', views.home, name = 'home'),
 path('about', views.about, name = 'about'),
 path('contact', views.contact, name = 'contact'),
 path('coursepage', views.course, name = 'coursepage'),
 path('modulelist', PostListView.as_view(), name = 'modulelist'),
 path('module/<int:pk>', PostDetailView.as_view(), name = 'module-detail'),
 path('module/new', PostCreateView.as_view(), name = 'module-create'),
 path('module/<int:pk>/update/', PostUpdateView.as_view(), name = 'module-update'),
]