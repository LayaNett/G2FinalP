from django.contrib import admin

from .models import Character, Question, Answer
# Register your models here.

admin.site.register(Character)
admin.site.register(Question)
admin.site.register(Answer)