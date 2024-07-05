from rest_framework import generics
from .serializers import PaymentSerializer
from .models import Payment


#pour les opérations de liste/création dune instance paiement
class PaymentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

