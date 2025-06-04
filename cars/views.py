from cars.models import Car
from cars.forms import CarModelForm #importar os formularios
from django.views import View #importar a classe
from django.views.generic import ListView, CreateView

#class CarsView(View):

    #def get(self, request):
        #cars = Car.objects.all().order_by('model')
        #search = request.GET.get('search')

        #if search:
            #cars = cars.filter(model__icontains=search)
    
        #return render(request, 'cars.html', {
            #'cars': cars,
            #'user': request.user  # Garante que o usuário está no contexto
        #})

class CarsListView(ListView): #ela ja tem essas propriedades e já tem o metodo get
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    #def get_queryset(self)
        #return Car.objects.all()

    def get_queryset(self): #usar o filtro
        cars = super().get_queryset().order_by('model') #super é uma função pra usar metodo da classe pai(ao inves de self)
        #queryset padrão ele pega o all  mesma coisa que cars = Car.objects.all().order_by('model)
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars



#class NewCarView(View):

    #def get(self, request):
        #new_car_form = CarModelForm()
        #return render(request, 'new_car.html', { 'new_car_form': new_car_form }) #vai retornar renderizando pro html

    
    #def post(self, request):
        #new_car_form = CarModelForm(request.POST, request.FILES) #vai pegar os dados e o files é pra imagem
        #if new_car_form.is_valid(): #ele executa todas as validações antes de executar essse is valid
            #new_car_form.save() #precisa criar o metodo save
            #return redirect('cars_list')
        #return render(request, 'new_car.html', { 'new_car_form': new_car_form}) # tem que ter esse retorno por questão do if

class NewCarCreateView(CreateView): #nao se esqueça de checar os templates
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #pra qual url mandar
