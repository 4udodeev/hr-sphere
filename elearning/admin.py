from django.contrib import admin

from .models import *

admin.site.register(Course)
admin.site.register(CourseResult)
admin.site.register(TestEntry)
admin.site.register(TestQuestion)
admin.site.register(Test)
admin.site.register(TestResult)
