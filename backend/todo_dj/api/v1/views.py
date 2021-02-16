from rest_framework import generics
from ...todo_dj import settings
from .serializers import TodoSerializer


# Create your views here.
class TodoList(generics.ListAPIView):
    ''' View Class for Todo Model '''
    queryset = settings.Todo.objects.all('-created_date')
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    ''' View Class for Certain Todo Detail '''
    queryset = settings.Todo.objects.all()
    serializer_class = TodoSerializer