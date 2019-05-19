from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Client
from .models import Project

def home(request):
    context = {
        'clients': Client.objects.all(),
        'projects': Project.objects.all()
    }
    return render(request, 'app/home.html', context)


#CLIENTS

# Display list of clients
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'app/clients.html'  
    context_object_name = 'clients'

# Display details of a particular client
class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

# Create a new client
class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['clientName', 'contactPerson', 'contactNumber']

    def form_valid(self, form):
        return super().form_valid(form)

# Update a client
class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['clientName', 'contactPerson', 'contactNumber']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        client = self.get_object()

# Delete a new client
class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = '/'

    def test_func(self):
        client = self.get_object()

#PROJECTS

# Display a list of projects
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'app/projects.html'  
    context_object_name = 'projects'
    ordering = ['client']

# Display details of a particular project
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project

# Create a new project
class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['projectName', 'projectStatus', 'client']

    def form_valid(self, form):
        return super().form_valid(form)

# Update a project
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['projectName', 'projectStatus', 'client']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()

# Delete a project
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        project = self.get_object()