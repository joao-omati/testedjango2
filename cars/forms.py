from django import forms
from cars.models import  Car  # Certifique-se que Brand está definido em models.py e car


    

class CarModelForm(forms.ModelForm): #é um formulario que se liga com o modelo e isso substitui todas as 25 linhas acima
    class Meta:
        model = Car #o modelo
        fields = '__all__' #vai pegar todos os campos do formulario car


    def clean_value(self): #clean quer dizer que é de validação
        value = self.cleaned_data.get('value') #vai pegar o valor que o usuario ta mandando no campo value
        if value < 20000:
            self.add_error('value', 'valor minimo do carro deve ser 20.000') #add error pede 2 campos,sendo o primeiro qual é e o segundo a mensagem
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'não é possivel cadastrar carros fabricados antes de 1975')
        return factory_year

