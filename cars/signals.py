from django.db.models.signals import pre_save,pre_delete,post_save,post_delete #são as mais comuns
from django.dispatch import receiver
from cars.models import Car 

@receiver(pre_save, sender = Car) #vai ouvir tudo que ta acontecendo no pre-save
def car_pre_save(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    print('### PRE SAVE ###')
    print(instance)

@receiver(post_save, sender = Car) #vai ouvir tudo que ta acontecendo no post-save
def car_post_save(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    print('### POST SAVE ###')
    print(instance)

@receiver(pre_delete, sender = Car) #vai ouvir tudo que ta acontecendo no pre-delete
def car_pre_delete(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    print('### PRE DELETE ###')
    print(instance)


@receiver(post_delete, sender = Car) #vai ouvir tudo que ta acontecendo no post-delete
def car_post_delete(sender, instance, **kwarfs): #**kwargs é pra pegar qualquer outro parametro e instance é o novo dado
    print('### POST DELETE ###')
    print(instance)
    