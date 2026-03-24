from rest_framework.viewsets import VeiculoViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer


class VeiculoViewSet(VeiculoViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
