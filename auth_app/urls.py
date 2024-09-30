from django.urls import path
from .views import home  # Adjust import based on your project structure

urlpatterns = [
    path('', home, name='home'),  # Home view
    # other paths...
]
