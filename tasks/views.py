from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Task
from .serializers import TaskSerializer

#create a read-write endpoint that lists all available Tasks instances
class TasksList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TasksDetail(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#  RetrieveUpdateDestroyAPIView for a read-write-delete endpoint for each individual Tasks.
