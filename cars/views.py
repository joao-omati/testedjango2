from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm #importar os formularios

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

def new_car_view(request):
    if request.method == 'POST': #quando for post(preencher os dados)
        new_car_form = CarModelForm(request.POST, request.FILES) #vai pegar os dados e o files é pra imagem
        if new_car_form.is_valid(): #ele executa todas as validações antes de executar essse is valid
            new_car_form.save() #precisa criar o metodo save
            return redirect('cars_list')
        
    
    else:  #quando nao for vai so criar um formulario vazio e retornar a pagina
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form}) #vai retornar renderizando pro html
