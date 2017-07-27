from django.shortcuts import render


# Create your views here.
def projectslist(request):

    return render(request, 'projects/projectslist.html')