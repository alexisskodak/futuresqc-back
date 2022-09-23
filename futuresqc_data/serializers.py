from rest_framework import serializers


class FsqcTableLastRecordInputSerializer(serializers.Serializer):
    table_id = serializers.CharField()
    product_id = serializers.CharField()
    machine_id = serializers.CharField()
    station_id = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class FsqcTableLastRecourdOutputSerializer(serializers.Serializer):
    table_id = serializers.CharField()
    product_id = serializers.CharField()
    machine_id = serializers.CharField()
    station_id = serializers.CharField()
    datetime = serializers.DateTimeField()
    turn = serializers.IntegerField()
    operator = serializers.CharField()
    features = serializers.JSONField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
