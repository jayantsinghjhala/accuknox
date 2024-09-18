from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from .forms import UserForm
from .models import Rectangle
from django.db import transaction
from django.contrib import messages



def create_user_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose another one.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered. Please use another one.')
            else:
                try:
                    with transaction.atomic():
                        user = user_form.save()

                    messages.success(request, 'User created successfully!')
                    return render(request, 'user_created.html', {'user': user})  # Pass user to template
                
                except IntegrityError:
                    messages.error(request, 'There was an error saving the user. Please try again.')

        else:
            messages.error(request, 'Invalid form submission. Please correct the errors.')

    else:
        user_form = UserForm()

    return render(request, 'create_user.html', {'user_form': user_form})

def rectangle_view(request):
     if request.method == 'POST':
          length = int(request.POST.get('length'))
          width = int(request.POST.get('width'))

          rect = Rectangle(length, width)
          dimensions = list(rect)

          return render(request, 'rectangle.html', {'dimensions': dimensions, 'length': length, 'width': width})
     
     return render(request, 'rectangle.html', {})