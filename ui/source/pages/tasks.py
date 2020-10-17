from celery import shared_task
from pages.models import Task

@shared_task
def name_of_your_function(objectId):
    task = Task.objects.get(pk=objectId)
    print(tasks.input)
    print(tasks.script)
    
    cp = subprocess.run(tasks.input,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,cwd=cwd,env=tasks.script)

    context = {
       'path':path,
       'output': cp.stdout.decode(),
    }
    print(context['output'])
    return(context['output'])
  
