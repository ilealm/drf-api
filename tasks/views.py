from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Task
from .serializers import TaskSerializer

class TasksList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksDetail(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer