from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title = title, content = content)
        note.save()
        
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/notes.html', {'notes': all_notes})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('index')

def edit(request,id):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag  = request.POST.get('tag')
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    note.save()

    return redirect('index')