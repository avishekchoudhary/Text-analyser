from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"index.html")

def analyse(request):
    djtext = request.POST.get('text', "default")
    remove_punc = request.POST.get('remove punc', "off")
    capatialize = request.POST.get('uppercase', "off")
    newlineremover = request.POST.get('newlinecutter', "off")
    text = request.POST.get('counter', "off")
    if remove_punc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ''
    
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'removed punctuations', 'analysed_text': analysed}
        djtext = analysed
    if capatialize == 'on':
        analysed = ''
        analysed = djtext.upper()
        params = {'purpose': 'All Caps', 'analysed_text': analysed}
        djtext = analysed
    if newlineremover == "on":
        analysed = ''
        for char in djtext:
            if char != "\n" and char!="\r":
                analysed = analysed + char    
        params = {'purpose': 'Removed NewLines', 'analysed_text': analysed}    
        djtext = analysed
    if text == 'on':
        analysed = ''
        analysed = len(djtext)
        params = {'purpose': 'character counter', 'analysed_text': analysed}
    if(remove_punc != "on" and text!="on" and capatialize!="on" and newlineremover!='on'):
        return HttpResponse("<h1>please select any operation and try again</h1>")    
    return render(request, "analyse.html", params)    