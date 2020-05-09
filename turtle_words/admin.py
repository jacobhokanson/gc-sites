from django.contrib import admin
from turtle_words.models import TurtleBrand, turtle_calls, TurtleBrandSignup

# register models with admin.site.register
admin.site.register(TurtleBrand)
admin.site.register(turtle_calls)
admin.site.register(TurtleBrandSignup)