from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from notes.models import Note
from notes.forms import NoteForm
# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(created_by=request.user)
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.created_by = request.user
            note.save()
            form.save_m2m()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})