from rest_framework import serializers
from .models import Student


# Serializer-level validation
# def check_val(value):
#     if value >= 200:
#         raise serializers.ValidationError('Seat Full')
#     return value

class StudentSerializer(serializers.ModelSerializer):
    # roll = serializers.IntegerField(validators=[check_val])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # validtion_roll = [check_val]

    def create(self, validat_data):
        return Student.objects.create(**validat_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Feild level validation

    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value

