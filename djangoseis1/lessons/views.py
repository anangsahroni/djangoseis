from django.shortcuts import render, redirect
from .models import Lesson
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def lessons_list(request):
    lessons = Lesson.objects.all().order_by('date')
    return render(request,'lessons/lessons_list.html',{ 'lessons':lessons })

def lesson_detail(request, slug):
    #eturn HttpResponse(slug)
    lesson = Lesson.objects.get(slug=slug)
    return render(request, 'lessons/lessons_detail.html', {'lesson': lesson})

@login_required(login_url="/accounts/login/")
def lesson_create(request):
    if request.method == 'POST':
        form = forms.CreateLesson(request.POST, request.FILES)
        if form.is_valid():
            # save lesson to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('lessons:list')
    else:
        form = forms.CreateLesson()
    return render(request, 'lessons/lessons_create.html', {'form': form})
