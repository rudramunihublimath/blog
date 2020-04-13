from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import PetSearchForm
import xlwt

# Create your views here.
def home(request):
    pets = PetModel.objects.all()
    context = { 'pets': pets}
    return render(request, "posts/dashboard.html", context)


def search(request):
    pets = PetModel.objects.all()
    if request.method == 'POST':
        srch = request.POST['srh']
        request.session['srch'] = srch
        print("srch:"+srch)
        if srch:
            match = pets.filter(name__icontains=srch).values()
            context = {'pets': match}
            if match:
                return render(request, "posts/searchOutput.html", context)
            else:
                print('no result found')
        else:
            return  HttpResponse('/search/')
    return render(request, "posts/search.html")   ## First time open normal html


def export_users_xls(request):
    #print(request)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'owner', 'species', 'sex','birth','death', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    srch = request.session['srch']
    #print("srch::",srch)
    rows = PetModel.objects.all().filter(name__icontains=srch).values_list('name', 'owner', 'species', 'sex','birth','death')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def export_users_xls2(request):
    #print(request)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['name', 'owner', 'species', 'sex','birth','death', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()


    #print("srch::",srch)
    rows = PetModel.objects.all().values_list('name', 'owner', 'species', 'sex','birth','death')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response