from rest_framework import routers
from .viewsets import PizzaViewSet, LikesViewSet, PizzeriaViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/pizzas', PizzaViewSet)
router.register(r'api/v1/likes', LikesViewSet)
router.register(r'api/v1/pizzerias', PizzeriaViewSet)
