from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
	"""
	The index page, '/', renders the main_menu.html file
	which determines whether the user is signed in or not
	then either takes the user to the Main Menu or redirects
	the user to the sign in page.
	"""
	return render(request, 'main_menu.html', {

	})


def how_to_play(request: HttpRequest) -> HttpResponse:
	return render(request, 'howtoplay.html', {

	})


def main_menu(request: HttpRequest) -> HttpResponse:
	return render(request, 'main_menu.html', {

	})


def question(request: HttpRequest, index: int = 1, correct: str = None) -> HttpResponse:
	value = request.COOKIES.get('score')
	if value is None:
		# Cookie never set, initialize to zero
		if correct is not None:
			score = 1
		else:
			score = 0
	else:
		if correct is not None:
			# Get the old score and increment by 1
			cscore = int(request.COOKIES.get('score'))
			score = str(cscore + 1)
		else:
			score = request.COOKIES.get('score')

	if index == 30:
		response = render(request, 'results.html', {
			'score': request.COOKIES.get('score')
		})
		return response

	question = Question.objects.all()[index];
	response = render(request, 'question_template.html', {
		'index': index,
		'question': question
	})
	response.set_cookie('score', score)

	return response
