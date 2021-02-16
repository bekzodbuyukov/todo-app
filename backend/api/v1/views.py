from django.http.response import HttpResponse
from rest_framework import generics
from .serializers import TodoSerializer
from todos.models import Todo


# Create your views here.
def show_index_page(request):
    style_attribute = 'style="font-family: Sans-serif;"'
    align_attribute = 'align="center"'
    url_response = f'<h1 {style_attribute} {align_attribute}>API</h1>'
    return HttpResponse(url_response)


class TodoListViewSet(generics.ListAPIView):
    ''' View Class for Todo Model '''
    queryset = Todo.objects.all().order_by('-created_date')
    serializer_class = TodoSerializer


class TodoDetailViewSet(generics.RetrieveAPIView):
    ''' View Class for Certain Todo Detail '''
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
