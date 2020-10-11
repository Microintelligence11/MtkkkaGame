from django.contrib import admin
from .models import points
from .models import Jay_Bharat_Chart
from .models import Jay_Bharat_panle
from .models import Moon_night_Chart
from .models import Moon_night_panle
from .models import Great_India_Chart
from .models import Great_India_panle
from .models import Kalyan_day_Chart
from .models import Kalyan_day_panle
# Register your models here.

admin.site.register(points)
admin.site.register(Jay_Bharat_Chart)
admin.site.register(Jay_Bharat_panle)
admin.site.register(Moon_night_Chart)
admin.site.register(Moon_night_panle)
admin.site.register(Great_India_Chart)
admin.site.register(Great_India_panle)
admin.site.register(Kalyan_day_Chart)
admin.site.register(Kalyan_day_panle)



