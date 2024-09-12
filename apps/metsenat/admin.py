from django.contrib import admin

from apps.metsenat.models import Homiy, Talaba, TalabaVaHomiy


# Register your models here.
@admin.register(Homiy)
class HomiyAdmin(admin.ModelAdmin):
    pass

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    pass

@admin.register(TalabaVaHomiy)
class TalabaVaHomiyAdmin(admin.ModelAdmin):
    pass