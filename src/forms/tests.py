import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
# Create your tests here. Puede ser tb en cualquier archivo

from .models import Question

# Creamos una subclase del TestCase, especificamente para testear el programa de
# nuestro modelo creado de pregunta


class QuestionModelTests(TestCase):
    # todos los metodos para testear cosas empiezan con 'test'
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        # creamos una pregunta dummy, que debería darnos False en el test, pq está publicada en el futuro
        future_question = Question(pub_date=time)
        # El método assertIs() simplemente nos tirará problemas si no da lo que queremos
        self.assertIs(future_question.was_published_recently(), False)
    # este testea que funcionen bien las pasadas

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    # este hace que funcionen bien las recientes
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    # con esto, creamos una pregunta según como la queramos (pq BTW, nunca le hicimos un __init__ a esta clase)
    return Question.objects.create(question_text=question_text, pub_date=time)


# Creamos otra clase que tendrá Tests sobre el IndexView
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # recordemos que reverse nos devuelve un URL
        # la respuesta es donde sea que nos lleva el que el cliente se meta ahi
        response = self.client.get(reverse('forms:index'))
        # podemos preguntar si algunas cosas se dan:
        # el código es de conexion exitosa
        self.assertEqual(response.status_code, 200)
        # si en la respuesta aparece que no hay encuestas disponibles (pq no hemos metido ninguna)
        self.assertContains(response, "No forms are available.")
        # si el QuerySet que aparece de llamar esa variable está vacío
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('forms:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('forms:index'))
        self.assertContains(response, "No forms are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('forms:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('forms:index'))
        # Por ejemplo, aquí verificamos que a lo que apunta la variable es a un Queryset
        # Que tiene exactamente las preguntas que, en teoría, le metimos
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


# Con esto, testearemos si los DetailView funcionan como deberían, no permitiendo ver
# las preguntas que no estén correctamente en la fecha
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        Verificamos que: The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(
            question_text='Future question.', days=5)
        # hacemos al cliente 'adivinar' una url de una pregunta que no debería aún
        # existir publicada (pero que sí está guardada en la db
        url = reverse('forms:detail', args=(future_question.id,))
        response = self.client.get(url)
        # Esto es equivalente a decir que se llegó a un 404
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(
            question_text='Past Question.', days=-5)
        url = reverse('forms:detail', args=(past_question.id,))
        response = self.client.get(url)
        # verificamos que la respuesta a la que llegó el cliente, contiene el texto de la pregunta
        self.assertContains(response, past_question.question_text)


# Aqui, yo creo mi propia serie de TESTs, para los ResultView:
class QuestionResultViewTests(TestCase):
    def test_future_question(self):
        """
        Verificamos que: The result view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(
            question_text='Future question.', days=5)
        # hacemos al cliente 'adivinar' una url de una pregunta que no debería aún
        # existir publicada (pero que sí está guardada en la db)
        # recordemos que reverse le mete la variable faltante a ese url con ese arg que el damos
        url = reverse('forms:results', args=(future_question.id,))
        response = self.client.get(url)
        # Esto es equivalente a decir que se llegó a un 404
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The result view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(
            question_text='Past Question.', days=-5)
        url = reverse('forms:results', args=(past_question.id,))
        response = self.client.get(url)
        # verificamos que la respuesta a la que llegó el cliente, contiene el texto de la pregunta
        self.assertContains(response, past_question.question_text)
        self.assertContains(response, 'Vote again?')


# puedo meterle tantos tests como quiera, de distintas cosas (OJO, con nombres representativos)
# Por cada modelo o View a testear, una TestClass distinta
# Un método separado de test para cada cosa a testear, por ejemplo:
# si quiero que las preguntas sin choices no aparezcan, tengo que testear que:
# con una pregunta SIN choices, no aparece ni Result ni Detail
# Y que con una que SI tiene choices, aparecen ambas cosas

# Si quiero testear con Selenium, conviene invocar la clase:
# LiveServerTestCase (leer los docs y así...)
