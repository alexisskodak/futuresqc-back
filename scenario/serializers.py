from core.serializers import BaseFsqcSerializer
from scenario.models import Scenario


class ScenarioSerializer(BaseFsqcSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"
