from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'client_screens/index.html')


@csrf_exempt
def get_target_num(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            list_numbers = data.get('array', [])
            target = data.get('target', 0)
            
            # Validación de los datos
            if not isinstance(list_numbers, list) or not isinstance(target, (int, float)):
                return JsonResponse({'error': 'El formato del JSON es incorrecto.'}, status=400)
            
            list_numbers = list(map(int, list_numbers))
            
            max_length = 0
            subarray = []
            
            for start in range(len(list_numbers)):
                current_sum = 0
                for end in range(start, len(list_numbers)):
                    current_sum += list_numbers[end]
                    
                    if current_sum == target:
                        current_length = end - start + 1
                        
                        if current_length > max_length:
                            max_length = current_length
                            subarray = list_numbers[start:end + 1]

            result = subarray if max_length > 0 else []
            return JsonResponse({'subarray': result}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'El cuerpo de la solicitud no es un JSON válido.'}, status=400)
    
    return JsonResponse({'error': 'Método no permitido. Use POST.'}, status=405)