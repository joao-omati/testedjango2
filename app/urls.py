
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import cars_view #agora ta importando da view a função


urlpatterns = [
    path('admin/', admin.site.urls), #2 parametros,uma a rota e a outra é uma função(view) que vai retornar uma http
    path('cars/', cars_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

