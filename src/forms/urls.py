from django.urls import path

from . import views
# para evitar colisiones con otras apps que tengan iguales nombres, definiremos aqui:
# esto conlleva cambiar un detalle en los html que referencien un url (i.e. index.html)
# ahora, para saber qué url tomar al aplicar el comando url, se denota: url 'polls:detail'
app_name = 'forms'
urlpatterns = [
    # cambiamos el question_id por pk. porque el DetailView espera que se llame así el argumento
    # ex: /polls/
    # Esto va a mostrar solo las encuestas que tenemos por ahi
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # Esto sale cuando apretamos la 5ta pregunta y nos da el detalle
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # Esta nos da los resultados y asi
    path('specifics/<int:pk>/results/',
         views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # En el fondo, cada path nos muestra una views distinta
    path('specifics/<int:question_id>/vote/', views.vote, name='vote'),
]
