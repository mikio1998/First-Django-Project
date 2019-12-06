# To deal with urls.
# https://docs.djangoproject.com/en/2.2/ref/urls/

# path(route, view, kwargs=None, name=None)
# route: String that contains url pattern
# 	may contain <> to send it as an argument to the view.
#	can also include converter, eg. <int:question_id>
# view: View function
# kwargs: Allows to pass additional arguments.
# name: Naming arguments

from django.urls import path

# from all import views
from . import views

# create namespace 
app_name = 'polls'
urlpatterns = [
	# Empty quotes (want it to be /polls)
	# it will be polls/'(whatever)'
	# leave it blank, should be index. 
	path('', views.index, name='index'),

	# Details, results, vote functions in views.py gets <int:question_id> 
	# passed to it from here.
	path('<int:question_id>', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),

]