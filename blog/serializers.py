from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(max_length=115)

    class Meta:
        model = Category
        fields = ('id', 'category_name')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.category_name = validated_data.get('category_name', instance.category_name)

        instance.save()

        return instance