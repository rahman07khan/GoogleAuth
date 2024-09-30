from django.shortcuts import render

def home(request):
    print("YES")
    return render(request, 'index.html')  # Create a template for this
