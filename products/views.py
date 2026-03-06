from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from ai.services import generate_description

@api_view(['POST'])
def generate_description(request):
    product_id = request.data['product_id']
    product = Product.objects.get(id=product_id)
    
    desc = generate_description(product.name, product.category.name)
    product.description = desc
    product.ai_generated = True
    product.save()
    
    return Response({'description': desc})
