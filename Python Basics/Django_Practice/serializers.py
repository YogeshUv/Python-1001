from rest_framework import serializers

class ExampleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

# Serialization
data = {"name": "John", "age": 30}
serializer = ExampleSerializer(data)
print(serializer.data)  # JSON-like structure

# Deserialization
serializer = ExampleSerializer(data=data)
if serializer.is_valid():
    valid_data = serializer.validated_data
