from django.db.models.signals import pre_save,pre_delete,post_save,post_delete #são as mais comuns
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory 

def car_inventory_update(): #esse codigo tava nas duas só que colocando em um só canto melhora
    cars_count = Car.objects.all().count()
    #somar o camp value de todas
    cars_value = Car.objects.aggregate( #retorna um campo calculado
        total_value = Sum('value') #vai retornar um objeto query
    )['total_value'] #vai retornar um dicionario com o valor do estoque
    CarInventory.objects.create( #cria um registro na tabela
        cars_count = cars_count,
        cars_value = cars_value
    )


@receiver(post_save, sender = Car) #vai ouvir tudo que ta acontecendo no post-save
def car_post_save(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    car_inventory_update()

@receiver(post_delete, sender = Car) #vai ouvir tudo que ta acontecendo no post-delete
def car_post_delete(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    car_inventory_update()
    
