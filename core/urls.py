from django.urls import path
from .views import register, create_property, my_properties, update_property, delete_property

urlpatterns = [
    path('register/', register, name='register'),
    path('create/', create_property, name='create_property'),
    path('my-properties/', my_properties, name='my_properties'),
    path('update/<int:pk>/', update_property, name='update_property'),
    path('delete/<int:pk>/', delete_property, name='delete_property'),
]
