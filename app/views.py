from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='k') 
    LOW=Webpage.objects.filter(email__endswith='.com')
    LOW=Webpage.objects.filter(email__endswith='.in')
    LOW=Webpage.objects.filter(name__contains='v')
    LOW=Webpage.objects.filter(name__in=('Ravi','Krishna'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='Ravi'))
    LOW=Webpage.objects.filter(Q(topic_name='cricket'))
    LOW=Webpage.objects.all()
    d={'web':LOW}
    return render(request,'insert_Webpage.html',context=d)
def insert_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.all()[1:]
    LOA=AccessRecord.objects.filter(date__gt='2001-5-10')
    LOA=AccessRecord.objects.filter(date__lt='2001-5-10')
    LOA=AccessRecord.objects.filter(date__gte='2000-2-22')
    LOA=AccessRecord.objects.filter(date__lte='2001-5-10')
    LOA=AccessRecord.objects.filter(date__year='2000')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__month='4')
    LOA=AccessRecord.objects.filter(date__day='22')
    LOA=AccessRecord.objects.filter(date__day__gt='22')
    LOA=AccessRecord.objects.filter(date__day__lt='22')
    LOA=AccessRecord.objects.filter(date__day__gte='22')
    LOA=AccessRecord.objects.filter(date__day__lte='22')
    d={'Acess':LOA}
    return render(request,'insert_AccessRecord.html',context=d)
def update_Webpage(request):
      LOW=Webpage.objects.filter(name='Ravi').update(email='ravi@gmail.in')
      LOW=Webpage.objects.filter(name='Ravi').update(email='ravi@gmail.com',Url='https://ravi.com')
      LOW=Webpage.objects.update_or_create(topic_name='cricket',defaults={'email':'krishna@gmail.com'})
      d={'web':Webpage.objects.all()}
      return render(request,'insert_Webpage.html',context=d)
def delete_Webpage(request):
    LOW=LOW=Webpage.objects.filter(name='Ravi').delete()
    d={'web':Webpage.objects.all()}
    return render(request,'insert_Webpage.html',context=d)