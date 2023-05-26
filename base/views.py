from django.shortcuts import render
from .models import Room

# Create your views here.

#rooms = [
#  {'id':1, 'name':'First Room'},
#  {'id':2, 'name':'Second Room'},
#  {'id':3, 'name':'Third Room'},
#]


def home(request):
  rooms = Room.objects.all()
  context = {'rooms': rooms}
  return render(request,'base/home.html', context)

def room(request, pk):
  room = Room.objects.get(id=pk)
  context = {'room': room}
  return render(request,'base/room.html', context)