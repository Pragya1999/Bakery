from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import UserSerializer,OrderSerializer,BakeryItemSerializer
from .models import Order,BakeryItem
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        pint("Hello")
        if serializer.is_valid():
            print("Bye")
            order = serializer.save()
            print("Bye2")
            total_bill = sum(item.get_total for item in order.orderitem_set.all())
            return Response({'order_id': order.id, 'total_bill': total_bill}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
        # Deduct the quantities from inventory
            for item in order.items.all():
                for ingredient in item.bakery_item.ingredients.all():
                    ingredient.quantity -= item.quantity * (ingredient.bakeryitemingredient_set.get(bakery_item=item.bakery_item).quantity_percentage / 100.0)
                    ingredient.save()
            total_bill = sum(item.get_total for item in order.orderitem_set.all())
            return Response({'order_id': order.id, 'total_bill': total_bill}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(customer=user.id)


class BakeryItemList(generics.ListAPIView):
    serializer_class = BakeryItemSerializer
    queryset = BakeryItem.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `name` query parameter in the URL.
        """
        queryset = self.queryset
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset.all()