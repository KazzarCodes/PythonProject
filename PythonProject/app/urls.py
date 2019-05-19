from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView
)
from . import views

# Set url paths for the views
urlpatterns = [
    path('', views.home, name='app-home'),

    path('clients', ClientListView.as_view(), name='app-clients'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),

    path('projects', ProjectListView.as_view(), name='app-projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]