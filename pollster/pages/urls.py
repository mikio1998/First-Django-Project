from django.urls import path

from . import views

urlpatterns = [
	# Empty quotes (want it to be /polls)
	# it will be polls/'(whatever)'
	# leave it blank, should be index.  
	path('', views.index, name='index'),
]