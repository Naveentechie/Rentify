from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Property
from .forms import PropertyForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('my_properties')  # Redirect to my_properties after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            return redirect('my_properties')
    else:
        form = PropertyForm()
    return render(request, 'create_property.html', {'form': form})

@login_required
def my_properties(request):
    properties = request.user.properties.all()
    return render(request, 'my_properties.html', {'properties': properties})

@login_required
def update_property(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('my_properties')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'update_property.html', {'form': form})

@login_required
def delete_property(request, pk):
    property = Property.objects.get(pk=pk)
    property.delete()
    return redirect('my_properties')
