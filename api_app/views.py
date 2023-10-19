from rest_framework import viewsets
from .models import CEO
from .serializers import CEOSerializer

# Create your views here.
class CEOViewSet(viewsets.ModelViewSet):
    queryset = CEO.objects.all().order_by('-first_year_active')
    serializer_class = CEOSerializer