from collections import OrderedDict

from rest_framework import serializers


class BaseFsqcSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret: OrderedDict = super().to_representation(instance)
        ret.update({key: val.rstrip() for (key, val) in ret.items() if isinstance(val, str)})
        return ret
