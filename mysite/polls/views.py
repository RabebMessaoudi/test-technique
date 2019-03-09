from django.shortcuts import render, get_object_or_404
from .models import Equipe, Joueur


def index(request):
    all_equipes = Equipe.objects.all()
    return render (request,'polls/index.html',{'all_equipes': all_equipes})

def detail(request, id):

    equipe = get_object_or_404(Equipe, pk=id)
    return render(request,'polls/detail.html',{'equipe': equipe})


def register(request):
    form = UserCreatForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)

