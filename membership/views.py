from django.shortcuts import render
from Infinitube.settings import STRIPE_PUB_KEY
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView
from .models import Membership, UserMembership, Subscription
import stripe


# Create your views here.

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    user_subscrition_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request)
    )
    if user_subscrition_qs.exists():
        user_subscrition = user_subscrition_qs.first()
        return user_subscrition
    return None


def get_selected_membership(request):
    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type
    )
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


class MembershipSelectView(ListView):
    model = Membership

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request):
        selected_membership_type = request.POST.get('membership_type')
        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)

        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type
        )

        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()
            '''
            ==============
            validation
            =============
            '''
        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, "you already have this membership. Your \
                                      next payement is due {}".format('ger this value from stripe'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # assign session
        request.session['selected_membership_type'] = selected_membership.membership_type
        return HttpResponseRedirect(reverse('membership:payment'))


def PaymentView(request):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    publishkey = STRIPE_PUB_KEY
    context = {
        'publishkey': publishkey,
        'selected_membership': selected_membership
    }
    return render(request, 'Membership/membership_payment.html', context)
