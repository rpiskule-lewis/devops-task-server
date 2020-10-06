import os
import re
import subprocess
from django.shortcuts import render
from django.template import loader

# Create your views here.

# pages/views.py
from django.http import HttpResponse

def isBash(text):
    return text.endswith('.sh')

def tasks(request):
    path = request.GET.get('path','/')
    loadPath="/opt/scripts"+path
    if not isBash(path):
       return HttpResponse("Don't break my server")

    env=os.environ.copy()
    file1 = open(loadPath, 'r') 
    lines = file1.readlines()
    for line in lines:
        line=line.rstrip("\n")
        p = re.compile('#[ ]*input[ ]*([a-zA-Z0-9]*)[ ]*(.*)')
        m = p.fullmatch(line)
        if m:
            key=m.group(1)
            value=request.POST.get(key)
            pattern=m.group(2)
            p2 = re.compile(pattern)
            m2 = p2.fullmatch(value)
            if not m2:
                return HttpResponse("Value [" + value + "] for input [" + key + "] does not match regexp [" + pattern + "]")
            print("[" + value + "] matches [" + pattern + "]")
            env[key]=value

    end=loadPath.rindex('/')
    cwd=loadPath[0:end]
    env['PATH']=env['PATH']+":"+cwd
    cp = subprocess.run(loadPath,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd=cwd,env=env)
    context = {
       'path':path,
       'output': cp.stdout.decode(),
    }
    template = loader.get_template('pages/tasks.html')
    return HttpResponse(template.render(context, request))

def scripts(request):
    path = request.GET.get('path','/')
    loadPath="/opt/scripts"+path
    print(loadPath)

    if not isBash(path):
        return HttpResponse("Don't break my server")

    
    # Using readlines() 
    file1 = open(loadPath, 'r') 
    lines = file1.readlines() 

    # input myText a-zA-Z*
    inputs = []
    regexps = {}
    for line in lines:
        line=line.rstrip("\n")
        p = re.compile('#[ ]*input[ ]*([a-zA-Z0-9]*)[ ]*(.*)')
        m = p.fullmatch(line)
        if m:
            inputs.append(m.group(1))
            regexps[m.group(1)]=m.group(2)

    context = {
        'path':path,
        'inputs': inputs,
        'regexps': regexps,
    }
    template = loader.get_template('pages/scripts.html')
    return HttpResponse(template.render(context, request))

def folders(request):
    path = request.GET.get('path','/')
    loadPath="/opt/scripts"+path
    print(loadPath)

    if isBash(path):
        return HttpResponse("Don't break my server")

    items = os.listdir(loadPath)
    folders = []
    scripts = []
        
    for item in items:
        if not isBash(item):
            folders.append(item+"/")
        else:
            scripts.append(item)

    context = {
        'path':path,
        'folders': folders,
        'scripts': scripts,
    }
    
    template = loader.get_template('pages/folders.html')
    return HttpResponse(template.render(context, request))
        
