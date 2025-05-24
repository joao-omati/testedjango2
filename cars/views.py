from django.shortcuts import render
#from django.http import HttpResponse #pra funcionar o errado
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() #tudo do cars
    print(cars)
    
    
    return render(request, #request igual a dados e requisições e depois coloca nome do html(ele vai automaticamente no templates
                   'cars.html',
                     #{'cars': { 'model': 'astra 2.0'} } #aqui é um carro fixo
                     {'cars' : cars}
    ) 
# a função render renderiza o http e passa pro usuario,meio campo entre views e usuario e a ultima é o contexto






#isso tudo é um comentario de algo que funciona só que não deve ser feito
 #   def cars_view(request):
  #      html = '''
   #         <html>
    #            <head>
     #               <title>Meus Carros</title>
      #          </head>
       #         <body>
        #            <h1>Carros irados</h1>
         #           <h3>só carro top<h3>
          #      </body
           # <html>
    #
#
#        return HttpResponse(html) #voce pode retornar html direto daqui só que não deve
