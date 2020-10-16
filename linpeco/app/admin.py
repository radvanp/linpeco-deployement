from django.contrib import admin

# Register your models here.
#doplnene
from .models import Place, Device, Record, RecordSumHour, RecordSumMonth, RecordSumYear
#doplnene
admin.site.register(Place)
admin.site.register(Device)
admin.site.register(Record)
admin.site.register(RecordSumHour)
admin.site.register(RecordSumMonth)
admin.site.register(RecordSumYear)