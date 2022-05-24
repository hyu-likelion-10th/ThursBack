from django.contrib import admin
from .models import Survey
from .models import Answer

class SurveyAdmin(admin.ModelAdmin):
    list_display=('question','ans1','ans2','ans3','ans4')

admin.site.register(Survey)

admin.site.register(Answer)

# Register your models here.
