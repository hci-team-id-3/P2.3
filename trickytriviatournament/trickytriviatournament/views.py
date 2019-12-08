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

def question(request: HttpRequest, index = 1) -> HttpResponse:
	question = Question.objects.all()[index];
	return render(request, 'question_template.html', {
		'index': index,
		'question': question
	})
