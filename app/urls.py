
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view  #agora ta importando da view a função
from cars.views import new_car_view
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls), #2 parametros,uma a rota e a outra é uma função(view) que vai retornar uma http
    path('register/', register_view, name= 'register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cars/', cars_view, name = 'cars_list'), #o name configura o nome da url
    path('new_car/', new_car_view, name = 'new_car'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

