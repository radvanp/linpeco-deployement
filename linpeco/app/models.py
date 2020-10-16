from django.db import models
#doplnil som toto from django.utils.translation import gettext as _
from django.utils.translation import gettext as _
EVENT_CHOICES = (
	( 1,"CUSTOMER IN"),
	( 2,"CUSTOMER OUT"),
	( 3,"CASH OPEN"),
	( 4,"CASH CLOSE"),
	( 5,"CASHIER ALARM"),
	( 6,"CASHIER ALARM"),
	( 7,"TAG ALARM"),
	( 8,"GATE SHIELDING"),
	( 9,"OCTOPUS ALARM"),
	(90,"T-CON REQUEST"),
	(99,"TEST"),
)

class Place(models.Model):
    place = models.IntegerField(_("place"), primary_key=True)
    name = models.CharField(_("name"), max_length=50)
    tms = models.DateTimeField(_("timestamp"), auto_now=True)

    class Meta:
        db_table = 'sg_place'
        verbose_name = _("place")
        verbose_name_plural = _('places')
        ordering = ('place',)

    def __str__(self):
        return str(self.name)

    class Admin:
        fields = (
            (None, {
                'fields': ('place', 'name')}),
            (_('Timestamp'), {
                'classes': 'collapse',
                'fields': ('tms',)}),
        )
        list_display = ('place', 'name')
        list_display_links = list_display

class Device(models.Model):
    device = models.IntegerField(_("device"), primary_key=True)
    place = models.ForeignKey(Place, verbose_name = _("place"), db_column='place', on_delete=models.CASCADE,)
    name = models.CharField(_("name"), max_length=50)
    tms = models.DateTimeField(_("timestamp"), auto_now=True)

    class Meta:
        db_table = 'sg_device'
        verbose_name = _("device")
        verbose_name_plural = _('devices')
        ordering = ('device',)

    def __str__(self):
        return str(self.name)

    class Admin:
        fields = (
            (None, {
                'fields': ('device', 'place', 'name')}),
            (_('Timestamp'), {
                'classes': 'collapse',
                'fields': ('tms',)}),
        )
        list_display = ('device', 'place', 'name')
        list_display_links = list_display
        list_filter = ['device', 'place', 'name']
        search_fields = ['device', 'place', 'name']
        date_hierarchy = 'tms'

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, verbose_name = _("device"), db_column='device',on_delete=models.CASCADE,)
    event = models.IntegerField(_("event"), choices=EVENT_CHOICES)
    tms = models.DateTimeField(_("timestamp"), auto_now=True)

    class Meta:
        db_table = "sg_record"
        verbose_name = _("record")
        verbose_name_plural = _("records")
        ordering = ("id",)

    def __str__(self):
        return str(self.event)

    def cvs(self):
        return (self.device, self.get_event_display(), self.tms.strftime("%Y-%m-%d %H:%M:%S"))

    class Admin:
        fields = (
            (None, {
                'fields': ('device', 'event')}),
            (_('Timestamp'), {
                'classes': 'collapse',
                'fields': ('tms',)}),
        )
        list_display = ('device', 'event', 'tms')
        list_display_links = list_display
        list_filter = ['device', 'event']
        search_fields = ['device', 'event']
        date_hierarchy = 'tms'

class RecordSumHour(models.Model):
    date = models.DateTimeField(_("date"), primary_key=True)
    place = models.CharField(_("place"), max_length=50)
    event_in = models.IntegerField(_("event in"))
    event_out = models.IntegerField(_("event out"))
    event_tag = models.IntegerField(_("event tag"))

    class Meta:
        db_table = "sg_recordsumhour"
        ordering = ("date",)

    def cvs(self):
        return (self.date, self.place, self.event_in, self.event_out, self.event_tag)

class RecordSumDay(models.Model):
    date = models.DateField(_("date"), primary_key=True)
    place = models.CharField(_("place"), max_length=50)
    event_in = models.IntegerField(_("event in"))
    event_out = models.IntegerField(_("event out"))
    event_tag = models.IntegerField(_("event tag"))

    class Meta:
        db_table = "sg_recordsumday"
        ordering = ("date",)

    def cvs(self):
        return (self.date, self.place, self.event_in, self.event_out, self.event_tag)

class RecordSumMonth(models.Model):
    date = models.DateField(_("date"), primary_key=True)
    place = models.CharField(_("place"), max_length=50)
    event_in = models.IntegerField(_("event in"))
    event_out = models.IntegerField(_("event out"))
    event_tag = models.IntegerField(_("event tag"))

    class Meta:
        db_table = "sg_recordsummonth"
        ordering = ("date",)

    def cvs(self):
        return (self.date, self.place, self.event_in, self.event_out, self.event_tag)

class RecordSumYear(models.Model):
    date = models.DateField(_("date"), primary_key=True)
    place = models.CharField(_("place"), max_length=50)
    event_in = models.IntegerField(_("event in"))
    event_out = models.IntegerField(_("event out"))
    event_tag = models.IntegerField(_("event tag"))

    class Meta:
        db_table = "sg_recordsumyear"
        ordering = ("date",)

    def cvs(self):
        return (self.date, self.place, self.event_in, self.event_out, self.event_tag)
