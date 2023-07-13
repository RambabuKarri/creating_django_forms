from django.shortcuts import render

# Create your views here.
from app.forms import * 
def djforms(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}

    if request.method=='POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['name']
    return render(request,'djforms.html')

