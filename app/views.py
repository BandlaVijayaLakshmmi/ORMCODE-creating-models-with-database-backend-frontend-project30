from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def insert_Topic(request):
    LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='KHO-KHO')
    LOT=Topic.objects.filter(topic_name='vally Ball')
    d={'topic':LOT}
    return render(request,'insert_Topic.html',context=d)
def insert_Webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name='Ravi')
    LOW=Webpage.objects.all()[1:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())  
    d={'web':LOW}
    return render(request,'insert_Webpage.html',context=d)
def insert_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.all()[1:]
    LOA=AccessRecord.objects.filter(date__gt='2001-5-10')
    LOA=AccessRecord.objects.filter(date__lt='2001-5-10')
    LOA=AccessRecord.objects.filter(date__gte='2000-2-22')
    LOA=AccessRecord.objects.filter(date__lte='2001-5-10')

    
    d={'Acess':LOA}
    return render(request,'insert_AccessRecord.html',context=d)