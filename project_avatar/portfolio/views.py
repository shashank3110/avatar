from django.shortcuts import render
from .models import Project
# Create your views here.

def portfolio(request):
    projects=Project.objects.all()
    # colors=['bisque','lightpink','lightblue','ivory','lightgreen','lightyellow']'#284D73' '#0C4276
    colors=['#0E2B47' for _ in range(len(projects))]
    # colors=['#12232e','#164a41','#3f3f3f','#ff8080','#cc33ff','#ffcc66']'#00182F' 
    # colors='blue'
    projects=list(zip(projects,colors))
    context={'projects':projects,
            #  'colors':colors
    
    }

    return render(request,'index.html',context,status=200)