from rest_framework import generics,mixins
from rest_framework.permissions import IsAuthenticated

from . import serializers
from ..models import Course

class CourseListView(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
            return Course.objects.filter(university=self.kwargs['university'])
