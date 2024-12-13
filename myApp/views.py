from django.shortcuts import render, redirect,HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.



# rooms =[
#     {'id': 1, 'name':'Let learn python'},
#     {'id': 2, 'name':'Design with me'},
#     {'id': 3, 'name':'Coding has started'},
#     {'id': 4, 'name':'We will win!!'},
    
# ]

# shop = [
#     {'id':1, 'name': 'Shop one'},
#     {'id':2, 'name': 'Shop two'},
#     {'id':3, 'name': 'Shop three'},
# ]

def mana(request):
    room = Room.objects.all()
    context = {'house': room}
    return render(request, 'myApp/home.html', context)


# def home(request):
#     room = Room.objects.all()
#     context = {'rooms': room}
#     return render (request, 'myApp/home.html', context)

def sec(request, pk):
    rooms = Room.objects.get(id=pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    context = {'house':rooms}
    return render(request, 'myApp/room.html', context)

# def show(request, pk):
#     context = {'pk':pk}
#     return render(request, 'myApp/home.html', context)

def news(request, pk):
    cont ={'pk': pk}
    return render(request, "myApp/tester.html", cont)


def createRoom(request):
    form = RoomForm()
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'myApp/room_form.html', context)
