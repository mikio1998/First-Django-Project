# A view function, or view for short, is a Python function 
# that takes a Web request and returns a Web response. 

# This response can be the HTML contents of a Web page, 
# or a redirect, or a 404 error, or an XML document, 
# or an image . . . or anything, really. 

# The view itself contains whatever arbitrary logic is 
# necessary to return that response. 

# render(request, template_name, context=None, content_type=None, status=None, using=None)¶
# Combines a given template with a given context dictionary 
# and returns an HttpResponse object with that rendered text.



from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question,Choice


# Get questions and display them.
def index(request):
	# Pass through data to the polls template polls/index.html.
	# List questions: up to 5, order decending (latest). 
	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	context = {'latest_question_list': latest_question_list}

	# pass in request, and location of template.
	return render(request, "polls/index.html", context)

# show specific question and choices
def detail(request, question_id):
	try:
		# Getting data from DB.
		# Using pk question_id, as parameter, 
		# which is going to come from the url.
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist.")
	return render(request, 'polls/detail.html', { 'question': question })

# get question and display results
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', { 'question':question })


# Vote for a question choice
def vote(request, question_id):
	# print the choice value id 
	print(request.POST['choice'])

	# get the question, based on the choice id.
	question = get_object_or_404(Question, pk=question_id)
	
	try: 
		# set var selected_choice based on that choice
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form...
		# If they don't select a choice, 
		# render the details template and display error msg.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
			}) 
	else:
		# add 1 to the selected_choice votes!
		selected_choice.votes += 1
		selected_choice.save()

		# Always return an HttpResponseRedirect after
		# successfully dealing with POST data.
		# This prevents data from being posted twice if 
		# a user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))





