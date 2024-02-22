from django.shortcuts import render
from .models import Togrisoz, Notogrisoz


def index(request):
    search = request.GET.get('search')
    togriSozlar = Togrisoz.objects.filter(soz=search)
    if togriSozlar and search:
        togrisoz = togriSozlar[0]
        notogriSozlar = Notogrisoz.objects.filter(togri_soz=togrisoz)
        context = {
            'togriSoz': togrisoz,
            'notogriSozlar': notogriSozlar
        }
        return render(request, 'index.html', context)
    elif search:
        notogriSoz = Notogrisoz.objects.filter(soz = search).first()
        if notogriSoz:
            togriSoz = Togrisoz.objects.get(id=notogriSoz.id)
            notogriSozlar = Notogrisoz.objects.filter(togri_soz=togriSoz)
            context = {
                'togriSoz': togriSoz,
                'notogriSozlar': notogriSozlar
            }
            return render(request,"index.html",context)
    n = Notogrisoz.objects.all()
    for i in n:
        if i != search:
            context = {
                'togriSoz': Togrisoz.objects.filter(soz='Mavjud emas'),
                'notogriSozlar': Notogrisoz.objects.filter(soz='Mavjud emas')
            }
            return render(request, 'index.html', context)

        elif search == '':
            context = {
                'togriSoz': Togrisoz.objects.filter(soz='Malumot kiriting'[0]),
                'notogriSozlar': Notogrisoz.objects.filter(soz='Malumot kiriting')
            }
            return render(request, 'index.html', context)
    return render(request, 'index.html')
