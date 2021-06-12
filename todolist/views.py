from django.views import generic
from .models import TodoList

class IndexView(generic.ListView):
    template_name = 'todolist/index.html'
    context_object_name = 'todolist'
    def get_queryset(self):
        """Return all the todos."""
        return TodoList.objects.all()