from django.db import models


# Create your models here.
class Todo(models.Model):
    ''' Todo Data Model '''
    title = models.CharField(max_length=100,
                            verbose_name='Todo title',
                            help_text='Write your todo title')
    description = models.TextField(verbose_name='Todo description',
                            help_text='Write your todo description')
    created_date = models.DateTimeField(auto_now=True,
                            verbose_name='Created Date',
                            help_text='Todo created date and time')
    deadline_date = models.DateTimeField(verbose_name='Deadline date and time',
                            help_text='Todo deadline date and time')
    
    class Meta:
        ''' Meta Class for Todo model '''
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    
    def __str__(self) -> str:
        ''' Default str function declaration '''
        return f'{self.title} until {self.deadline_date}'
