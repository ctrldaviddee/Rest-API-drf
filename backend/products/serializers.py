from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer

from .models import Product
from .validators import validate_title_no_hello, unique_product_title


class ProductInlineSerializer(serializers.Serializer):
    an_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)  # works anywhere
    an_url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )  # The HyperLinkedIdentityField only works on a model Serializer

    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    class Meta:
        model = Product
        fields = [
            'owner',
            'an_url',
            'url',
            'edit_url',
            # 'email',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
            'discount',
           'related_products',
        ]
        # fields = '__all__'

    #    def validate_title(self, value):
    #        qs = Product.objects.filter(title__iexact=value)
    #        if qs.exists():
    #            raise serializers.ValidationError('This title has already been used.')
    #        return value

    # not really practical
    # def create(self, validated_data):
    # return Product.objects.create(**validated_data)
    # email = validated_data.pop('email')
    #    obj = super().create(validated_data)
    # print(email, obj)
    #    return obj

    # def update(self, instance, validated_data):
    #    email = validated_data.pop('email')
    # instance.title = validated_data.get('title')
    # return instance
    #    return super().update(instance, validated_data)

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

        return None if not isinstance(obj, Product) else obj.get_discount()
