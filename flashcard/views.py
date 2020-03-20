from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def add(request):
    from random import randint

    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == 'POST':
        answer = request.POST['answer']
        old1 = request.POST['old1']
        old2 = request.POST['old2']

        # Error Handling for blank input
        if not answer:
            user_ans = "You didn't enter anything"
            color = 'warning'
            return render(request, 'add.html', {
                'answer': answer,
                'user_ans': user_ans,
                'num_1': num_1,
                'num_2': num_2,
                'color': color
            })

        correct_ans = int(old1) + int(old2)
        if int(answer) == correct_ans:
            user_ans = 'Correct ' + old1 + " + " + old2 + " = " + str(answer)
            color = 'success'
        else:
            user_ans = 'Incorrect ' + old1 + " + " + old2 + " = " + str(correct_ans) + " not " + str(answer)
            color = 'danger'

        return render(request, 'add.html', {
            'answer': answer,
            'user_ans': user_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

    return render(request, 'add.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def subtract(request):
    from random import randint

    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == 'POST':
        answer = request.POST['answer']
        old1 = request.POST['old1']
        old2 = request.POST['old2']

        # Error Handling for blank input
        if not answer:
            user_ans = "You didn't enter anything"
            color = 'warning'
            return render(request, 'subtract.html', {
                'answer': answer,
                'user_ans': user_ans,
                'num_1': num_1,
                'num_2': num_2,
                'color': color
            })

        correct_ans = int(old1) - int(old2)
        if int(answer) == correct_ans:
            user_ans = 'Correct ' + old1 + " - " + old2 + " = " + str(answer)
            color = 'success'
        else:
            user_ans = 'Incorrect ' + old1 + " - " + old2 + " is = " + str(correct_ans) + " not " + str(answer)
            color = 'danger'

        return render(request, 'subtract.html', {
            'answer': answer,
            'user_ans': user_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

    return render(request, 'subtract.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def multiply(request):
    from random import randint

    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == 'POST':
        answer = request.POST['answer']
        old1 = request.POST['old1']
        old2 = request.POST['old2']

        # Error Handling for blank input
        if not answer:
            user_ans = "You didn't enter anything"
            color = 'warning'
            return render(request, 'multiply.html', {
                'answer': answer,
                'user_ans': user_ans,
                'num_1': num_1,
                'num_2': num_2,
                'color': color
            })

        correct_ans = int(old1) * int(old2)
        if int(answer) == correct_ans:
            user_ans = 'Correct ' + old1 + " x " + old2 + " = " + str(answer)
            color = 'success'
        else:
            user_ans = 'Incorrect ' + old1 + " x " + old2 + " is = " + str(correct_ans) + " not " + str(answer)
            color = 'danger'

        return render(request, 'multiply.html', {
            'answer': answer,
            'user_ans': user_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

    return render(request, 'multiply.html', {
        'num_1': num_1,
        'num_2': num_2,
    })


def divide(request):
    from random import randint

    num_1 = randint(0, 9)
    num_2 = randint(0, 9)

    if request.method == 'POST':
        answer = request.POST['answer']
        old1 = request.POST['old1']
        old2 = request.POST['old2']

        # Error Handling for blank input
        if not answer:
            user_ans = "You didn't enter anything"
            color = 'warning'
            return render(request, 'divide.html', {
                'answer': answer,
                'user_ans': user_ans,
                'num_1': num_1,
                'num_2': num_2,
                'color': color
            })

        correct_ans = int(old1) / int(old2)
        if float(answer) == correct_ans:
            user_ans = 'Correct ' + old1 + " / " + old2 + " = " + str(answer)
            color = 'success'
        else:
            user_ans = 'Incorrect ' + old1 + " / " + old2 + " is = " + str(correct_ans) + " not " + str(answer)
            color = 'danger'

        return render(request, 'divide.html', {
            'answer': answer,
            'user_ans': user_ans,
            'num_1': num_1,
            'num_2': num_2,
            'color': color
        })

    return render(request, 'divide.html', {
        'num_1': num_1,
        'num_2': num_2,
    })
