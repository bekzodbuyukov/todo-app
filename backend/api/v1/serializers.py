from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    ''' Serializer for Todo Model '''
    class Meta:
        ''' Meta Class for Todo Serializer '''
        model = Todo
        fields = ['id', 'title', 'description',
                  'created_date', 'deadline_date']
