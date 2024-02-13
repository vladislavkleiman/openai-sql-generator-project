import json
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

@csrf_exempt
def generate_sql(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query_description = data.get('queryDescription', '')

            response = openai.Completion.create(
                model='gpt-3.5-turbo-instruct',
                prompt=f"Convert the following natural language description into a SQL query:\n\n{query_description}",
                max_tokens=150
            )

            sql_query = response.choices[0].text.strip() if response.choices else ''

            return JsonResponse({'sqlQuery': sql_query})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
