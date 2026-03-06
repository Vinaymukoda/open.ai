@api_view(['GET'])
def sales_insights(request):
    orders = Order.objects.filter(status='paid').values(
        'total', 'created_at', 'id'
    )[:100]
    
    insights = analyze_orders(orders)
    return Response({'insights': insights})
