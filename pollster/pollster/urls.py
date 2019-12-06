"""pollster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
# include; if we are going to bring in another urls file.  
from django.urls import include, path

urlpatterns = [
	# for anything polls/; include polls.urls.
	# As soon as we go to /polls/ anything, it'll look at the polls.urls file. 
	path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
