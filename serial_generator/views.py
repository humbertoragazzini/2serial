from django.shortcuts import render

# Create your views here.

def serial_generator(request):
    cache= 0
    
    if request.method == 'GET':
        form = request.GET
        print(form['product_serial'])
    
    context = {
            "cache": cache,
        }

    return render(request, 'serial_generator/serial_generator.html', context)
