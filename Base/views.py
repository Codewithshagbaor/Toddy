from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . models import Todo
import uuid
from django.contrib import messages
# Create your views here.
def index(request):
  todos = Todo.objects.all()
  response_data = {}

  if request.POST.get('action') == 'post':
    todo = request.POST.get('todo')
    uid = str(uuid.uuid4())[:5]

    response_data['todo'] = todo
    response_data['uid'] = uid

    Todo.objects.create(
      todo=todo,
      uid=uid
    )
    return JsonResponse(response_data)
  context = {
    'todos':todos
  }
  return render(request, 'index.html', context)

def delete_view(request, uid):
  todo = get_object_or_404(Todo, uid=uid)

  if request.method == 'POST':
    todo.delete()
    messages.info(request, "Deleted")
    return redirect('index')
  context = {
    'todo':todo
  }

  return render(request, 'delete.html', context)