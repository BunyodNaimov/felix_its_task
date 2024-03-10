from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Order, OrderItem
from products.serializers import OrderCreateSerializer, ProductListSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductOrderCreateView(APIView):

    @swagger_auto_schema(request_body=OrderCreateSerializer)
    def post(self, request, *args, **kwargs):
        data = {"result": []}
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        products_data = serializer.validated_data['products']
        for product_data in products_data:
            product_id = product_data['product_id']
            product = get_object_or_404(Product, pk=product_id)
            quantity = product_data['quantity']
            product_result = {"product_name": product.name, "product_qty": quantity, "materials": []}
            order_items = []
            for product_material in product.materials.all():
                material = product_material.material
                material_quantity = product_material.quantity * quantity
                print(material_quantity)
                warehouse = material.warehouse.filter(orders__isnull=True, remainder__gte=material_quantity).last()
                print(f"warehouse: {warehouse}")
                order_item = OrderItem.objects.create(warehouse=warehouse, quantity=material_quantity)
                order_items.append(order_item)
                product_result['materials'].append({
                    "warehouse_id": warehouse.id if warehouse else None,
                    "material_name": material.name,
                    "qty": material_quantity,
                    "price": warehouse.price if warehouse else None
                })

            order = Order.objects.create(product=product, quantity=quantity)
            order.items.add(*order_items)
            order.total_price = order.items.aggregate(
                total_price=Sum('price', default=0) * Sum('quantity')
            )['total_price']
            order.save(update_fields=['total_price'])
            data['result'].append(product_result)
        return Response(data, status=status.HTTP_201_CREATED)
