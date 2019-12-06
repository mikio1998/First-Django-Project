from django.contrib import admin

from .models import Question, Choice

# pollster site admin interface


# Site header, title, index header
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_header = "Welcome to the Pollster Admin"




# have choices within questions app (admins screen)
# using TabularInline
class ChoiceInline(admin.TabularInline):
	model = Choice
	#how many extra choices
	extra = 3

# set the fields
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['question_text']}),
	('Date Information', {'fields': ['pub_date'], 'classes': 
	['collapse']}),]
	inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)

# register both Question, but also QuestionAdmin class. 
admin.site.register(Question, QuestionAdmin)

