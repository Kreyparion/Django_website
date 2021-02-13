from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import F
from django.utils import timezone
#from django.template import loader


from .models import Choice, Question

# Esta es una subclase de ListView, que equivale a mostrar una lista de objetos


class IndexView(generic.ListView):
    # le damos el template_name, para que no ocupe:
    # <app_name>/<model_name>_list.html por defecto
    template_name = 'forms/index.html'
    # en general no damos contexto, pero para esto, la variable generada por defecto sería question_list (pq es una list view y usamos el modelo question)
    # esto le indica a Django que queremos usar ese nombre
    context_object_name = 'latest_question_list'

    # esto es lo que antes era el 'latest_question_list'
    # ahora es la forma en como definimos el método en esta clase
    # El ListView, posiblemente tiene esta función pa llamar a los objetos a enlistar
    # En particular, aquí hacemos que muestre las ultimas 5 preguntas, en una variable
    # a la que le cambiamos el nombre por 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (pero publicadas antes de 'ahora')"""
        # primero filtro entre las que llamaré a las que tienen timezone anterior a cierto tiempo
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# Es una subclase de DetailView, que es de mostrar los detallles de un objeto en particular
class DetailView(generic.DetailView):
    # Aquí debo decirle a la genericview cuál es el modelo sobre el que actuará
    # Eso, pq los detailView muestran los detalles de este objeto
    # El codigo HTML debe ser compatible con eso; esto solo hace el get objeto y lo renderea
    # en general, no damos contexto, pq como Question es un modelo Django, sabe que hacer
    model = Question
    # se le da ese template_name, pq sino tomaría por defecto: 'polls/question_detail.html'
    # dado el modelo que elegimos; OJO que ese detail que toma por defecto es pq se llama generic.DetailView
    template_name = 'forms/detail.html'

    def get_queryset(self):
        '''
        Me excluye las preguntas cuya fecha no apañe para nuestros fines
        La gracia es que evitamos que los usuarios puedan llegar y meterse advinando la URL
        Derechamente, el detalle de una pregunta NO va a estar disponible si aun no se publica
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())


# creo un ResultsView, que es un DetailView, pero responde a lo espec+ifico de results
# , pa que no se vea igual a la otra. (pq si no, tomaría igual un archivo que se llame:
# polls/question_detail.html (pq es un DetailView), asi como el ListView hace lo propio
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'forms/results.html'

    def get_queryset(self):
        '''
        Me excluye las preguntas cuya fecha no apañe para nuestros fines
        La gracia es que evitamos que los usuarios puedan llegar y meterse advinando la URL
        Derechamente, el detalle de una pregunta NO va a estar disponible si aun no se publica
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    # me da la pregunta o una excepcion
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Si la pregunta está bien, saco de su lista de alternativas la que sea
        # que clickeo el usuario; request.POST es un diccionario que siempre guarda str
        # y que en este caso tiene el id de la 'choice' hecha
        # (tb existe una request.GET)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Muestra de nuevo la forma pa votar, si no elegí opcion alguna (y por tanto, request.POST['choice'] no tiene nada
        return render(request, 'forms/detail.html', {'question': question, 'error_message': "No elegiste ninguna alternativa"})
    else:
        # lidiamos con lo que significa este input (dado por el POST data)
        # F lo opera directo desde la db
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        '''
        selected_choice.votes += 1
        selected_choice.save()
        '''

        # Devuelvo un HttpResponseRedirect si trabajé POST data, pa que no se repita el voto si se va para atras
        # reverse() es una funcion que recibe el nombre de la view a la que se le da control
        # y tb la parte variable de ese URL, que se la proveemos, en este caso, siendo la question.id
        # Dsps la URL redirigida va a irse a results
        return HttpResponseRedirect(reverse('forms:results', args=(question.id,)))
