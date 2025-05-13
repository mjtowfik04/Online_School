from rest_framework import serializers
from order.models import Cart, CartItem, Order, OrderItem
from courses.models import Course
from courses.serializers import CourseSerializer
from order.services import OrderService

class EmptySerializer(serializers.Serializer):
    pass

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'price']

class AddCartItemSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'course_id', 'quantity']

    def validate_course_id(self, value):
        if not Course.objects.filter(pk=value).exists():
            raise serializers.ValidationError(f"Course with id {value} does not exist")
        return value

    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        course_id = self.validated_data['course_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, course_id=course_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)

        return self.instance

class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']

class CartItemSerializer(serializers.ModelSerializer):
    course = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'course', 'quantity', 'total_price']

    def get_total_price(self, cart_item):
        return cart_item.quantity * cart_item.course.price

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
        read_only_fields = ['user']

    def get_total_price(self, cart):
        return sum([item.course.price * item.quantity for item in cart.items.all()])

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart found with this id')
        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Cart is empty')
        return cart_id

    def create(self, validated_data):
        user_id = self.context['user_id']
        cart_id = validated_data['cart_id']
        try:
            order = OrderService.create_order(user_id=user_id, cart_id=cart_id)
            return order
        except ValueError as e:
            raise serializers.ValidationError(str(e))

    def to_representation(self, instance):
        return OrderSerializer(instance).data

class OrderItemSerializer(serializers.ModelSerializer):
    course = SimpleProductSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'course', 'price', 'quantity', 'total_price']

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'items']
