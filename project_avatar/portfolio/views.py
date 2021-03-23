from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    # get all project objects from Project Model
    projects=Project.objects.all()
    # color scheme for the project cards
    colors=['#0E2B47' for _ in range(len(projects))] 
    projects=list(zip(projects,colors))
    context={'projects':projects}

    return render(request,'index.html',context,status=200)