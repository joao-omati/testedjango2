from cars.models import Car
from cars.forms import CarModelForm #importar os formularios
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required #proteger as partes que precisam login
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


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


@method_decorator(login_required(login_url = 'login'), name = 'dispatch') #vai usar o login required pra ver se esta logado,se não tiver ele não acessa a view
#o login_url login é só pra mostrar o caminho pra tela de login e
class NewCarCreateView(CreateView): #nao se esqueça de checar os templates
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/' #pra qual url mandar


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name  = 'car_update.html'
    #success_url = '/cars'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    succes_url = '/cars/'


