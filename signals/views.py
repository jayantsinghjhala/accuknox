from django.shortcuts import render
from django.contrib.auth.models import User, Rectangle


def create_user_view(request):
    User.objects.create(username="testuser")
    return render(request, 'user_created.html')

def rectangle_view(request):
    rect = Rectangle(10, 5)
    dimensions = list(rect)
    return render(request, 'rectangle.html', {'dimensions': dimensions})
