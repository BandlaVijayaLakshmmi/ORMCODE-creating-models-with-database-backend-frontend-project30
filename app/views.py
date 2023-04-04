from django.shortcuts import render


# Create your views here.
from app.models import *
def insert_Topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'insert_Topic.html',context=d)
def insert_Webpage(request):
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'insert_Webpage.html',context=d)
def insert_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    d={'Acess':LOA}
    return render(request,'insert_AccessRecord.html',context=d)