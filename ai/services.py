import openai
import google.generativeai as genai
import requests
import os
import json

openai.api_key = os.environ.get('OPENAI_API_KEY')
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
OLLAMA_URL = os.environ.get('OLLAMA_URL')

def generate_description(product_name, category):
    prompt = f"""
    Write engaging e-commerce product description for:
    Product: {product_name}
    Category: {category} (power tools/electrical equipment)
    
    Include: features, benefits, use cases, safety info
    100-150 words, SEO friendly, persuasive
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response.choices[0].message.content
    except:
        return "Auto-generated description unavailable."

def analyze_orders(orders_data):
    context = json.dumps(orders_data, indent=2)
    prompt = f"""
    Analyze Wilko Power sales data and provide:
    1. Top selling products
    2. Revenue trends  
    3. Customer insights
    4. Business recommendations
    
    Data: {context}
    """
    
    resp = requests.post(OLLAMA_URL, json={
        'model': 'mistral',
        'prompt': prompt,
        'stream': False
    })
    return resp.json()['response']
