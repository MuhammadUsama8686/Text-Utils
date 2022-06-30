from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get("text","default")
    removePunc = request.POST.get("removePunc","Off")
    capfirst = request.POST.get("capfirst","Off")
    newlineremover = request.POST.get("newlineremover","Off")
    spaceremover = request.POST.get("spaceremover","Off")
    charcount = request.POST.get("charcount","Off")

    if removePunc == "on":        
        analyzed = ""
        punctuations = '''.,?"';:!@#$'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        djtext = analyzed

    if capfirst == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capitalize All','analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
                
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        djtext = analyzed

    if charcount == "on":
       
        
        analyzed = str(len(djtext))
                
        params = {'purpose':'Char Counter','analyzed_text':analyzed}
        djtext = analyzed 

    if spaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]=="" and djtext[index+1]==""):          
            
                analyzed = analyzed + char
                
        params = {'purpose':'Extra Space Remover','analyzed_text':analyzed}
        djtext = analyzed      
    
    
    if (removePunc!="on" and spaceremover!="on" and charcount!="on" and newlineremover!="on" and capfirst!="on"):
        return HttpResponse("Error, PLease Give Valid Inpus!!!")
        
    return render(request, "analyze.html", params)
        