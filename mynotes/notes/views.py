from django.shortcuts import render,redirect
from notes.models import NotesList,Notes
import json
from django.http import HttpResponse

# Create your views here.

def main_page(request ,*args, **kwargs):
    context={}
    user=request.user
    if request.method=="GET":
        notelist=NotesList.objects.filter(user=user)
        context['note_list']=notelist
    return render(request,'main_page.html',context)

def create_notelist(request,*args,**kwargs):
    user=request.user
    payload={}
    if request.method=="POST":
        notelist_name=request.POST.get('notelist')
        print(notelist_name)
        nl=NotesList(user=user,name=notelist_name)
        nl.save()
        payload['response']='success'
    else:
        payload['response']='...error...'
    return HttpResponse(json.dumps(payload),content_type='application/json')
        

def notes_page(request,*args,**kwargs):
    user=request.user
    context={}
    if request.method=="GET":
        notelist_id=kwargs.get('name_id')
        notelist=NotesList.objects.get(pk=notelist_id)
        notes=Notes.objects.filter(under_notelist=notelist)
        context['notes']=notes
        context['id']=notelist_id
    return render(request,'notes.html',context)

def create_note(request,*args,**kwargs):
    user=request.user
    context={}
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        name_id=kwargs.get('name_id')
        notelist=NotesList.objects.get(pk=name_id)
        note=Notes(title=title,description=description,under_notelist=notelist)
        note.save()
        return redirect('notes:notes_page',name_id=name_id)
    return render(request,'create_note.html',context)

def notes_detail(request,*args,**kwargs):
    user=request.user
    context={}
    if request.method=='GET':
        note_id = kwargs.get('note_id') 
        note=Notes.objects.get(pk=note_id)
        context['note']=note
    return render(request,'note_detail.html',context)

def remove_notelist(request,*args,**kwargs):
    user=request.user
    payload={}
    if request.method=="GET":
        notelist_id=kwargs.get('name_id')
        notelist=NotesList.objects.get(pk=notelist_id)
        if notelist:
            notelist.delete()
            payload['response']='notelist deleted'
        else:
            payload['response']='notelist not found'
    return HttpResponse(json.dumps(payload),content_type='application/json')

def remove_note(request,*args,**kwargs):
    user=request.user
    payload={}
    if request.method=='GET':
        note_id=kwargs.get('note_id')
        note=Notes.objects.get(pk=note_id)
        if note:
            note.delete()
            payload['response']='note deleted'
        else:
            payload['response']='note not found'
    return HttpResponse(json.dumps(payload),content_type='application/json')

































