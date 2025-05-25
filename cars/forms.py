from django import forms
from cars.models import Brand, Car  # Certifique-se que Brand está definido em models.py e car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField() 

    def save(self): #o self ta acessando seu proprio form(carform)
        car = Car(
            model = self.cleaned_data['model'], #poderia colocar carform ao inves de self
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save() #esse save é pra salvar no bd
        return car

