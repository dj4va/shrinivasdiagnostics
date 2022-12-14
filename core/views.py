from django.conf import settings
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from django.http import HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from accounts.models import *
from shop.models import *
from .models import *
from .forms import *

import razorpay
# razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZORPAY_SECRET_KEY))

# Create your views here.
def homepage(request):
	is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
	page_title = _('Check the Best Blood Test &amp; Pathology Lab in India with Shrinivas Diagnostics Labs')
	user_id = request.user.is_authenticated
	user_order = Order.objects.filter(user=user_id).count()
	# member = Profile.objects.get(email=request.user)
	# get_status = Profile.objects.filter(email=request.user).values_list('is_active', flat=True).first()
	# currency = 'INR'
	# amount = 20000
	# razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

	# order id of newly created order.
	# razorpay_order_id = razorpay_order['id']
	# callback_url = 'paymenthandler/'

	initial_dict = {
		# 'ticker_code': get_ticker_id,
	}
	
	form = ProductForm(initial=initial_dict)
	
	# if is_ajax:
	# 	get_board_id = request.GET.get('get_board_id')
	# 	get_ticker_code = MarketDetail.objects.filter(id=get_ticker_id).values_list('ticker_code', flat=True).first()
	# 	cache.set('get_board_id', get_board_id, 30)

	# 	get_ticker_id = cache.get('get_ticker_id')

	# 	context = {
	# 		'page_title': page_title,
	# 		'get_qs': get_qs,
	# 		'get_ticker_id': get_ticker_id,
	# 		'get_sector_id': get_sector_id,
	# 		'get_board_id': get_board_id,
	# 	}
	# 	return JsonResponse(context)

	# if request.method == "POST":
	# 	form = ProductForm(request.POST or None)
	# 	get_ticker_id = request.POST.get('get_ticker_id')
	# 	cache.set('get_ticker_id', get_ticker_id, 30)
	# 	get_ticker_id = cache.get('get_ticker_id')

	# 	context = {
	# 		'page_title': page_title,
	# 		# 'form': form,
	# 		# 'chart': dump,
	# 		# 'get_ticker_name': get_ticker_name,
	# 		'get_ticker_name': json.dumps(get_ticker_name),
	# 	}
	# 	return render(request, 'chart/index.html', context)
	# else:
	# 	if get_status == "expired":
	# 		messages.warning(request, "You're Package is expired. Please choose the package to continue.")
	# 		return redirect('subscription:subscription')
	# 	else:
	# 		form = ProductForm(initial=initial_dict, instance=request.user)

	context = {
		# 'razorpay_order_id': razorpay_order_id,
		# 'razorpay_merchant_key': settings.RAZOR_KEY_ID,
		# 'razorpay_amount': amount,
		# 'currency': currency,
		# 'callback_url': callback_url,
		'page_title': page_title,
		'form': form,
		'user_order': user_order,
		# 'get_ticker_name': get_ticker_name,
	}
	return render(request, 'core/home.html', context)


def show(request):
	product = get_object_or_404(Product, id=pk, available=True)

	context = {
		'product': product,
	}

	return render(request,'header.html')
