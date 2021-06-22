from django.contrib import admin
from django.urls import path

from . import views
# para evitar colisiones con otras apps que tengan iguales nombres, definiremos aqui:
# esto conlleva cambiar un detalle en los html que referencien un url (i.e. index.html)
# ahora, para saber qué url tomar al aplicar el comando url, se denota: url 'polls:detail'
app_name = 'presta'
urlpatterns = [
    path('contact/', views.contactView, name='contact'),
    path('success/', views.successView, name='success'),
    path('name/', views.get_name, name='name'),
    path('list_prestas/', views.list_prestas, name='list_prestas'),
    path('<int:presta_id>/', views.details_prestas, name='details_prestas'),
]
