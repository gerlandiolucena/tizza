import random as rd
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Pizza
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View

def random(request):
    pizzaId = round(rd.uniform(1, 200))
    return index(request, pizzaId)

@login_required
def index(request, pid):
    try:
        if request.method == 'DELETE' and 'can_delete' in request.user.user_permissions:
            pizza = Pizza.objects.get(id=pid)
            pizza.delete()
            return HttpResponse(content={
                'id': pizza.id,
            })
        if request.method == 'POST':
            data = json.loads(request.body)
            new_pizza = Pizza.objects.create(
                title=data['title'],
                description=data['description'],
                creator=request.user,
            )
            new_pizza.save()
            return HttpResponse(content={
                'id': new_pizza.id,
                'title': new_pizza.title,
                'description': new_pizza.description
            })
        elif request.method == 'GET':
            pizza = Pizza.objects.get(id=pid)
            return HttpResponse(
                content={
                    'id': pizza.id,
                    'title': pizza.title,
                    'description': pizza.description
                }
            )
    except ObjectDoesNotExist:
        return HttpResponse(status=404, content={
            "status": "error",
            "message": "pizza not found"
        })


class GetTenPizzasView(View):
    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})
