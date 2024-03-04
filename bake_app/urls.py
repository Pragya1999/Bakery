from django.urls import path
from .views import CreateUserView, MyTokenObtainPairView,OrderCreateView,OrderHistoryView,BakeryItemList
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/order/', OrderCreateView.as_view(), name='create_order'),
    path('api/order/history/', OrderHistoryView.as_view(), name='order_history'),
    path('api/products/', BakeryItemList.as_view(), name='product_list'),
]