from django.shortcuts import render
import base36

# Create your views here.

def serial_generator(request):
    start = 0    
    serials_list = []
    upper = 0
    lower = 0
    start = 0
    index_limit = 0

    if request.method == 'GET':
        print("paso por if")
        form = request.GET
        product_serial = form['product_serial']
        upper = form['upper_number']
        lower = form['lower_number']
        start = base36.loads(lower)
        index_limit = base36.loads(upper)
        while start < index_limit or start == index_limit:
            serials_list.append(product_serial + str(base36.dumps(start)))
            print(serials_list)
            start+=1
        print("no paso por if")
    context = {
            "serial_list": serials_list,
        }

    return render(request, 'serial_generator/serial_generator.html', context)
