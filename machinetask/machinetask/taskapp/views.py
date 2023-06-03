from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class OrderViewSet(APIView):

  def get(self, request):
    order_list = Order.objects.all()
    serializer = OrderSerializer(order_list , many = True) 
    return Response(serializer.data)


  def post(self , request) :
    serializer = OrderSerializer(data=request.data) 
    if serializer.is_valid():              
      serializer.save()  
      return Response("Order Succesfull")  
    else:
      return Response(serializer.errors)


class order_edit(APIView):

  def get(self, request,pk):
    order = Order.objects.get(order_id=pk)
    serializer = OrderSerializer(order)    
    return Response(serializer.data)


  def delete(self, request,pk):
    order = Order.objects.get(order_id=pk)
    order.delete()
    return Response("order is successfully delete") 


  def put(self, request, pk, format=None):
    order = Order.objects.get(order_id=pk)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
