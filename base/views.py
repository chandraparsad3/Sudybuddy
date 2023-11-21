from django.shortcuts import render
from django.http import HttpResponse

rooms=[
    { 'id': 1, 'name': 'Parsad'},
    { 'id': 2, 'name': 'Pradeep'},
    { 'id': 3, 'name': 'Da'}
]


def home(request):
    r={'rooms':rooms}
    return render(request,'base/home.html',r)

def room(request,pk):
    room =None
    for i in rooms:
        if i['id']==int(pk):
            room=i
    context={'room': room}
    return render(request,'base/room.html',context)