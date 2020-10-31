from rest_framework import serializers


class SentenceResultSerializer(serializers.Serializer):
    conf = serializers.FloatField()
    end = serializers.FloatField()
    start = serializers.FloatField()
    word = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class SentenceTextSerializer(serializers.Serializer):
    result = SentenceResultSerializer(required=True, many=True)
    text = serializers.CharField(required=True, allow_blank=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
