from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True) # works anywhere
    an_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    ) # The HyperLinkedIdentityField only works on a model Serializer
    class Meta:
        model = Product
        fields = [
            'an_url',
            'url',
            'edit_url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
        ]
        # fields = '__all__'


    def get_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None

        return reverse(viewname='product-detail', kwargs={'pk': obj.pk}, request=request)


    def get_edit_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None

        return reverse(viewname='product-edit', kwargs={'pk': obj.pk}, request=request)

    def get_an_url(self, obj):
            request = self.context.get('request')

            if request is None:
                return None

            return reverse(viewname='product-detail', kwargs={'pk': obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, Product):
            return None

        return obj.get_discount()
