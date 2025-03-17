from rest_framework import serializers
from .models import AmazoneDataScrape

class AmazonScraperSerializer(serializers.ModelSerializer):
    product_image = serializers.SerializerMethodField()

    class Meta:
        model = AmazoneDataScrape
        fields = ['id', 'product_name', 'product_price', 'product_time', 'product_image']

    def get_product_image(self, obj):
        if obj.product_image:
            return obj.product_image.url.lstrip('/')
        return None
