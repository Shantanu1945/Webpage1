from django.shortcuts import render

#from django.http import RequestContext
#from django.http import HttpResponseRedirect
from .forms import Registration
from .models import Category


#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
#count = 5

# Create your views here.

def home(request):      
  
           
  #print(context_dict.values())
  
  if request.method == 'POST':
    stud1 = ' '
    cm =Registration(request.POST)
    if cm.is_valid():
          cm1 = cm.cleaned_data['category']
          
          sm1  = cm.cleaned_data['subcateg']

          pm1 = cm.cleaned_data['product']

          reg2 = Category(category = cm1,subcateg = sm1,product = pm1)
          reg2.save()
          cm = Registration()
        
  else :
  
     cm = Registration()
     stud1 = Category.objects.all()
     print(stud1)

  return render(request,'project/registration.html', {'forms': cm ,'Register' : stud1} )
