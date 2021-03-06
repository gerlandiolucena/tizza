from django.contrib.auth.models import User

from pizza.utils.producer import producer
from rest_framework import viewsets

from user.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):

        user = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        producer.produce(exchange='user',
                         body={'user_id': user.id},
                         routing_key='user.deleted'
                         )
        return response

