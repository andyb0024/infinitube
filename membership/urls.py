from django.urls import path
from.views import MembershipSelectView,PaymentView
urlpatterns = [
    path('', MembershipSelectView.as_view(),name='select'),
    path('payment', PaymentView, name='payment'),
#     path('<int:pk>/<music_slug>', MusicDetail.as_view(), name='music_detail')
 ]