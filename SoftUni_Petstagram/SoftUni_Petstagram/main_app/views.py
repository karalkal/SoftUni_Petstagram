from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home_page.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def profile(request):
    return render(request, 'profile_details.html')


def photo_details(request, pk):
    context = {pk: "pk"}
    return render(request, 'photo_details.html', context)
