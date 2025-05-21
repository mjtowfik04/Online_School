from rest_framework import generics, permissions
from .models import Enroll
from .serializers import EnrollSerializer

class EnrollCreateView(generics.CreateAPIView):
    serializer_class = EnrollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
