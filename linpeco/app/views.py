import csv, datetime
from django.http import HttpResponse
#from django.shortcuts import render_to_response
#oprava pr
from django.shortcuts import render
from app.models import Record, RecordSumDay, RecordSumHour, RecordSumMonth, RecordSumYear

def base(request):
    return render('app/base.html')

def today(request):
    date = datetime.datetime.now()
    date_from = date.date()
    date_to = date_from + datetime.timedelta(days=1)
    robj = Record.objects.filter(tms__gte=date_from, tms__lt=date_to)
    todayIn = robj.filter(event=1).count()
    todayOut = robj.filter(event=2).count()
    todayTag = robj.filter(event=7).count()
    header = ['Customer', 'Count']
    headerE = ['Device', 'Event', 'Date']
    rows = (('In', todayIn), ('Out', todayOut), ('Tag', todayTag))
    rowsE = Record.objects.order_by('-id')[:10]
    return render(request, '/var/www/linpeco/templates/app/today.html', {'header': header, 'rows': rows, 'header': header, 'rows': rows, 'headerE': headerE, 'rowsE': rowsE, 'date': date})

def total(request):
    header = ['Date', 'Place', 'In', 'Out', 'Tag']
    date = datetime.datetime.now()
    rows = RecordSumYear.objects.all()
    if request.method == 'GET' and 'csv' in request.GET:
        return csv_to_response(header, rows, 'total', date)
    return render(request,'/var/www/linpeco/templates/app/total.html', {'header': header, 'rows': rows})

def year(request):
    header = ['Date', 'Place', 'In', 'Out', 'Tag']
    date = datetime.datetime.now()
    year = date.year
    if request.method == 'GET' and 'year' in request.GET:
        date = request.GET['year']
        year = date.split('-')[0]
        year = int(year)
    date_from = datetime.date(year, 1, 1)
    date_to = datetime.datetime(year+1, 1, 1).date()
    rows = RecordSumMonth.objects.filter(date__gte=date_from, date__lt=date_to)
    if request.method == 'GET' and 'csv' in request.GET:

        return csv_to_response(header, rows, 'year', date)
    return render(request,'/var/www/linpeco/templates/app/year.html', {'header': header, 'rows': rows, 'date_from': date_from})

def month(request):
    header = ['Date', 'Place', 'In', 'Out', 'Tag']
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    if request.method == 'GET' and 'month' in request.GET:
        date = request.GET['month']
        year, month = date.split('-')
        year = int(year)
        month = int(month)
    date_from = datetime.date(year, month, 1)
    if month == 12:
        date_to = datetime.datetime(year+1, 1, 1).date()
    else:
        date_to = datetime.datetime(year, month+1, 1).date()
    rows = RecordSumDay.objects.filter(date__gte=date_from, date__lt=date_to)
    if request.GET.has_key('csv'):
        return csv_to_response(header, rows, 'month', date)
    return render_to_response('app/month.html', {'header': header, 'rows': rows, 'date_from': date_from})

def day(request):
    header = ['Date', 'Place', 'In', 'Out', 'Tag']
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    if request.method == 'GET' and 'day' in request.GET:
        date = request.GET['day']
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
    date_from = datetime.date(year, month, day)
    date_to = date_from + datetime.timedelta(days=1)
    rows = RecordSumHour.objects.filter(date__gte=date_from, date__lt=date_to)
    if request.method == 'GET' and 'csv' in request.GET:
        return csv_to_response(header, rows, 'day', date)
    return render(request,'/var/www/linpeco/templates/app/day.html', {'header': header, 'rows': rows, 'date_from': date_from})

def event(request):
    header = ['Device', 'Event', 'Date']
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    if request.method == 'GET' and 'day' in request.GET:
        date = request.GET['day']
        year, month, day, hour = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
    date_from = datetime.datetime(year, month, day, hour)
    date_to = date_from + datetime.timedelta(hours=1)
    rows = Record.objects.filter(tms__gte=date_from, tms__lt=date_to)
    if request.method == 'GET' and 'csv' in request.GET:
        return csv_to_response(header, rows, 'event', date)
    return render(request,'/var/www/linpeco/templates/app/event.html', {'header': header, 'rows': rows, 'date_from': date_from})

class excel_x(csv.excel):
    delimiter = ';'
csv.register_dialect("excel-x", excel_x)

def csv_to_response(header, rows, filename, date):
    if date:
        fname = 'sg-%s-%s.csv' % (filename, date)
    else:
        fname = 'sg-%s.csv' % filename
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + fname
    # Create the CSV writer using the HttpResponse as the "file"
    writer = csv.writer(response, dialect='excel-x')
    writer.writerow(header)
    for row in rows:
        writer.writerow(row.cvs())
    return response
