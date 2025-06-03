from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm #importar os formularios
from django.views import View #importar a classe

class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search)
    
        return render(request, 'cars.html', {
            'cars': cars,
            'user': request.user  # Garante que o usuário está no contexto
        })





class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', { 'new_car_form': new_car_form }) #vai retornar renderizando pro html

    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES) #vai pegar os dados e o files é pra imagem
        if new_car_form.is_valid(): #ele executa todas as validações antes de executar essse is valid
            new_car_form.save() #precisa criar o metodo save
            return redirect('cars_list')
        return render(request, 'new_car.html', { 'new_car_form': new_car_form}) # tem que ter esse retorno por questão do if
