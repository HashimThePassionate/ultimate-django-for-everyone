from django.urls import path
from store import views
# from rest_framework.routers import SimpleRouter, DefaultRouter
from store.views import ProductViewSet, CollectionViewSet, ReviewViewSet, CartViewSet, CartItemViewSet, CustomerViewSet
from rest_framework_nested import routers
# from pprint import pprint
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

# pprint(router.urls)
urlpatterns = router.urls + products_router.urls + carts_router.urls
# urlpatterns = [
#     # path('products/', views.product_list),
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     # path('products/<int:id>/', views.product_detail),
#     # path('collections/', views.collection_list),
#     path('collections/', views.CollectionList.as_view()),
#     # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')
#     path('collection/<int:pk>/', views.CollectionDetail.as_view())
# ]
