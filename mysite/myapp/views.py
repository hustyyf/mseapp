from django.shortcuts import render
from django.http import HttpResponse
from .models import fasongzhe,jieshouzhe
from .forms import UploadExcelForm
import xlrd


def index(request):
    return  render(request,'myapp/forms.html',{})


def sender(request):
    fasong=fasongzhe.objects.all()
    return render(request,'myapp/fasongzhe.html',{"fasongzhes":fasong})


def jname(request,jieshouzhe_id):
    jieshou=jieshouzhe.objects.get(pk=jieshouzhe_id)
    return render(request,"myapp/detail.html",{'jieshouzhe':jieshou})


def fasongjieshou(request,fasongzhe_id):
    fasong=fasongzhe.objects.get(pk=fasongzhe_id)
    jieshoulist=fasong.jieshouzhe_set.all()
    return render(request,"myapp/jieshouzhe.html",{'jieshouzhes':jieshoulist})

def post(request):
    form = UploadExcelForm(request.POST, request.FILES)
    if form.is_valid():
        wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read()) # 关键点在于这里
        table = wb.sheets()[0]
        row = table.nrows
        for i in range(1, row):
            col = table.row_values(i)
            q=fasongzhe(fname=col[0],fnumber=col[1],message=col[2])
            q.save()
        return HttpResponse(table.row_values(0)[0])
'''
    def open_excel(file= 'file.xls'):
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception,e:
            print str(e)
    def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
        data = open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        colnames =  table.row_values(colnameindex) #某一行数据 
        list =[]
        for rownum in range(1,nrows):
            row = table.row_values(rownum)
            if row:
                app = {}
                for i in range(len(colnames)):
                    app[colnames[i]] = row[i] 
                    list.append(app)
        return list
'''


# Create your views here.
