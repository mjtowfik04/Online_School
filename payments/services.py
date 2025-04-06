from payments.models import Cart, CartItem,Purchase,PurchaseItem
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError


class OrderService:
    @staticmethod
    def create_order(user_id, cart_id):
        with transaction.atomic():
            cart = Cart.objects.get(pk=cart_id)
            cart_items = cart.items.select_related('product').all()

            total_price = sum([item.product.price *
                               item.quantity for item in cart_items])

            purchase = Purchase.objects.create(
                user_id=user_id, total_price=total_price)

            purchase_items = [
                PurchaseItem(
                    purchase=purchase,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                    total_price=item.product.price * item.quantity
                )
                for item in cart_items
            ]
            PurchaseItem.objects.bulk_create(purchase_items)

            cart.delete()

            return purchase

    @staticmethod
    def cancel_order(purchase, user):
        if user.is_staff:
            purchase.status = Purchase.CANCELED
            purchase.save()
            return purchase

        if purchase.user != user:
            raise PermissionDenied(
                {"detail": "You can only cancel your own order"})

        if purchase.status == Purchase.DELIVERED:
            raise ValidationError({"detail": "You can not cancel an order"})

        purchase.status = Purchase.CANCELED
        purchase.save()
        return purchase
