from django.urls import path
from store import views
# from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import ProductViewSet, CollectionViewSet, ReviewViewSet
from rest_framework_nested import routers
# from pprint import pprint
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet)
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet,
                         basename='product-reviews')
# pprint(router.urls)
urlpatterns = router.urls + products_router.urls
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
