from django.urls import include, path
from .views import index, random, GetTenPizzasView
from .routes import router

urlpatterns = [
    path('<int:pid>', index, name='pizza'),
    path('random', random),
    path('', index),
    path('ten', GetTenPizzasView.as_view()),
 ]


