from django.shortcuts import render
from cars.models import Car

def cars_view(request): #faz um get que pega todas os dados como objeto
    #print(request.GET.get('search')) #vai passar tudo o que o usuario passar na url
    cars = Car.objects.all().order_by('model') #vai buscar todos os carros e ordernar por midelo,se colocar - faz o contrario
    search = request.GET.get('search') #o search é o que coloca na nu url,se nao passar algum vai dar erro por dar um valor nulo

    if search: #ai se fizer uma busca vai achar,se não colocar parametro vai mostrar tudo+
        cars = Car.objects.filter(model__icontains=search) #vai buscar o valor e faz um filtro pelo modelo,icontains ignona uppercase
        #cars = Car.objects.filter(model__contains=search) #vai buscar o valor e faz um filtro pelo modelo
        
    
    return render(
        request, 
        'cars.html',
        {'cars': cars}
    )

