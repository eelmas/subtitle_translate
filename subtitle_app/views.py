import os

import parser
from django.shortcuts import render, redirect, get_object_or_404

from subtitle_app.models import Document,Translate
from subtitle_translate import settings
from .forms import DocumentForm, TranslateForm
import srt
import pysrt

# Create your views here.

def model_form_upload(request):
    if request.method == 'POST':        #request.method == 'POST' bunu yerine request.POST yazılabilir.
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else :
        form = DocumentForm()

    files = Document.objects.all()

    return render(request, 'subtitle_app/subtitle_template.html', {'form': form, 'files':files})





def translate2(request,pk):
    file = Document.objects.get(pk=pk)
    lines = []
    subs = pysrt.open(file.document.path, encoding='iso-8859-1')
    for i in range(0, len(subs)):
        sub = subs[i].text.replace("<i>", "").replace("</i>", "")
        lines.append(sub)
        Translate.objects.create(document=file, sentence=sub, suggestion='')
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TranslateForm()
    return render(request, 'subtitle_app/trans.html', {'form': form, 'lines': Translate.objects.all()})


def translate(request, pk):

    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            obj = Translate.objects.get(id=form.cleaned_data['id'])
            obj.suggestion = form.cleaned_data['suggestion']
            obj.save()
    else:
        file = Document.objects.get(pk=pk)
        lines = []
        subs = pysrt.open(file.document.path, encoding='iso-8859-1')

        for i in range(0, len(subs)):
            sub = subs[i].text.replace("<i>", "").replace("</i>", "")
            lines.append(sub)
            l=len(subs)

            if(Translate.objects.filter(document__pk=pk).count()<l):
                Translate.objects.create(document=file, sentence=sub, suggestion='')

    data = []
    for t in Translate.objects.filter(document__pk=pk):
        data.append((t, TranslateForm(initial={'id': t.id, 'suggestion': t.suggestion}, auto_id=True)))

    return render(request, 'subtitle_app/trans.html', {'data': data})

















