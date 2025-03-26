from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PersonalInformation
from .models import Person


@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons=Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context=context)

    if request.method == 'POST':
        form=PersonalInformation(request.POST)
        if not form.is_valid():
            return HttpResponse('Error',status=400)
        full_name=form.cleaned_data['full_name']
        age=form.cleaned_data['age']
        height=form.cleaned_data['height']
        gender=form.cleaned_data['gender']
        person=Person.objects.create(full_name=full_name,age=age,height=height,gender=gender)
        person.save()
    return HttpResponse(person,status=201)
