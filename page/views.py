from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def story(request):
    return render(request, 'story.html')