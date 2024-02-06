from rest_framework import viewsets
from .models import Team
from .serializer import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    serializers_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(sel, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()