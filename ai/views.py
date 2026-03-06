from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order
from analytics.services import analyze_orders_data
from ai.services import generate_description, analyze_orders

@api_view(['GET'])
def support_chat(request):
    order_id = request.GET.get('order_id')
    query = request.GET.get('query', '')
    
    if order_id:
        order = Order.objects.get(id=order_id)
        context = f"Order #{order.id}: ₹{order.total}, Status: {order.status}"
    else:
        context = "General Wilko Power support"
    
    prompt = f"{context}\nCustomer: {query}"
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    
    return Response({'reply': response.text})
