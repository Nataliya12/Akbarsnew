from django.contrib import admin
from .models import *

admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(UserProfile)
admin.site.register(TestHistory)
admin.site.register(AnswerHistory)