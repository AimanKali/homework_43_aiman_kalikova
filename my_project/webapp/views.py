from django.shortcuts import render

def index_view(request):
    return render(request, 'calculator.html')

def calculate_view(request):
    data = request.POST
    try:
        first = float(data.get('firstNumber'))
        second = float(data.get('secondNumber'))
        operation = data.get('gridRadios')
        if operation == 'add':
            result = first + second
        elif operation == 'subtract':
            result = first - second
        elif operation == 'multiply':
            result = first * second
        else:
            result = first / second
        if result % 1 == 0:
            result = int(result)
    except ValueError:
        return render(request, 'calculator.html', context={
            'error': "Please enter correct numbers"
        })
    except Exception:
        return render(request, 'calculator.html', context={
            'error': "Division by zero"
        })

    return render(request, 'calculator.html', context={
        'result': result
    })
