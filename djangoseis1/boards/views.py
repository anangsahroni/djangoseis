from django.shortcuts import render

# Create your views here.

def boards_list(request):
    return render(request, 'boards/boards_list.html')