from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Item
import stripe
import proj_payments.settings

# Секретный ключ stripe.api_key, полученный из дашборда облачной службы stripe
stripe.api_key = proj_payments.settings.STRIPE_SECRET_KEY
    # 'sk_test_51Mc50PDwyS9nSQ0XQ8Q2FUnS8ZyBwxuJv1kowV9y8tWPy6nks7YydlrL2pYhrdgYFjbtdZmpmDc58UC3hT5xRvaT009WZZqbhZ'

#Представление для вызова формы покупки checkout, встроенной в сам облачный сервис
def buy_item(request, item_id):
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.price * 100),
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
#Endpoint's для вызова функций представления в случае успешной оплаты или отмены
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',

    )
    return JsonResponse({'sessionId': session.id})

#Отрисовка детальной информации по выбранному товару с кнопкой "Оплатить"
def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item_detail.html', {'item': item})

#Отрисовка главной страницы со всеми товарными позициями
#Надо добавить чекбокс для мультивыбора (выбора нескольких товарных позиций)
def index(request):
    item = Item.objects.all()
    return render (request, 'index.html', {'items': item})

#Ответ от сервера в случае удачной оплаты
#Пока простенько, надо доработать
def success(request):
    return render(request, 'success.html')
    # return HttpResponse('<center><h1>Поздравляем! Платеж прошел успешно.</h1></center>')

#Ответ от сервера в случае отмены оплаты: всякие форс-мажоры, денег нет на карте и т.д.
def cancel(request):
    return render(request, 'cancel.html')
    # return HttpResponse('<center><h1>К сожалению, платеж не прошел. Деньги с карты не списались</h1></center>')