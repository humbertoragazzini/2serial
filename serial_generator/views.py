from django.shortcuts import render

# Create your views here.

def serial_generator(request):
    """ render home page """
    return render(request, 'serial_generator/serial_generator.html')
