from django.contrib import admin
from cars.models import Car
from cars.models import Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','model', 'brand', 'factory_year', 'model_year', 'value', ) #campos que aparecem
    search_fields = ('model','brand')  #busca somente nesse campo

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',) #campos que aparecem
    search_fields = ('name',)  #busca somente nesse campo


admin.site.register(Brand, BrandAdmin) 
admin.site.register(Car, CarAdmin) 



