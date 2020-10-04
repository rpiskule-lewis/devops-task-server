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

def run(request):
    path = request.GET.get('path','/')
    loadPath="/opt/scripts"+path
    print(loadPath)
    if not isBash(path):
       return HttpResponse("Don't break my server")

    env=os.environ.copy()
    file1 = open(loadPath, 'r') 
    lines = file1.readlines()
    for line in lines:
        print(line)
        p = re.compile('#[ ]*input[ ]*([a-zA-Z0-9]*)[ ]*(.*)')
        m = p.match(line)
        if m:
            key=m.group(1)
            value=request.POST.get(key)
            pattern=m.group(2)
            p2 = re.compile(pattern)
            m2 = p2.match(value)
            if not m2:
                return HttpResponse("Value [" + value + "] for input [" + key + "] does not match regexp [" + pattern + "]")
            env[key]=value

    print(loadPath);
    print(loadPath.rindex('/'));
    end=loadPath.rindex('/')
    cwd=loadPath[0:end]
    env['PATH']=env['PATH']+":"+cwd
    print(cwd)
    print(os.listdir(cwd))
    print(env)
    print("["+loadPath+"]")
    #capture_output=True,
    cp = subprocess.run(loadPath,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd=cwd,env=env)
    context = {
       'path':path,
       'output': cp.stdout.decode(),
    }
    template = loader.get_template('pages/run.html')
    return HttpResponse(template.render(context, request))
    
def index(request):
    path = request.GET.get('path','/')
    loadPath="/opt/scripts"+path
    print(loadPath)

    if isBash(path):
        # Using readlines() 
        file1 = open(loadPath, 'r') 
        lines = file1.readlines() 

        # input myText a-zA-Z*
        inputs = []
        regexps = {}
        for line in lines:
            p = re.compile('#[ ]*input[ ]*([a-zA-Z0-9]*)[ ]*(.*)')
            m = p.match(line)
            if m:
                inputs.append(m.group(1))
                regexps[m.group(1)]=m.group(2)

        context = {
            'path':path,
            'inputs': inputs,
            'regexps': regexps,
        }
        template = loader.get_template('pages/input.html')
        return HttpResponse(template.render(context, request))
    else:
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
        
        template = loader.get_template('pages/index.html')
        return HttpResponse(template.render(context, request))
        
