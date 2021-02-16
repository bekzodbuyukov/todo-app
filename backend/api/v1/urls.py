from django.urls import path
from .views import TodoListViewSet, TodoDetailViewSet
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from todo_dj import config
# from rest_framework.documentation import include_docs_urls


schema_view = get_schema_view(
                openapi.Info(
                    title=config.API_TITLE,
                    default_version=config.API_DEFAULT_VERSION,
                    description=config.API_DESCRIPTION,
                ),
                public=True,
                permission_classes=(permissions.AllowAny,))


urlpatterns = [
    path('todos/', TodoListViewSet.as_view(), name='todo_list'),
    path('todos/<int:pk>', TodoDetailViewSet.as_view(), name='todo_detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='openapi_schema'),   
    # path('docs/',
    #     include_docs_urls(title=API_TITLE,
    #                     description=API_DESCRIPTION),
    #     name='api_docs'),
]
