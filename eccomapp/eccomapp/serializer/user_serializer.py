from rest_framework.serializers import ModelSerializer
from eccomapp.models import User, ShippingAddress

class CreateShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ["street", 'city', 'state', 'zip_code', 'country']


class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"


class UserSerializer(ModelSerializer):
    shipping_addresses = ShippingAddressSerializer(many=True, read_only=True) # read-only true means spping addres be get request not post request
    default_shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = "__all__"