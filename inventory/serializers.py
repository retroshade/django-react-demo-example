from rest_framework import serializers
from .models import Location, Family, Product, Transaction

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location 
        fields = '__all__'

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ('sku','barcode', 'title', 'description','location','family')
        depth = 1

class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Transaction 
        fields = ('sku', 'barcode','product')