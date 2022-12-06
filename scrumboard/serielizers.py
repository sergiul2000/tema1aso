# from rest_framework import serializers
# from scrumboard.models import List,Card
#
# class CardSerielizers(serializers.ModelSerializer):
#     class Meta:
#         model = Card
#         fields = '__all__'
#
# class ListSerializer(serializers.ModelSerializer):
#     cards = CardSerielizers(read_only=True, many=True)
#
#     class Meta:
#         model = List
#         fields = '__all__'
