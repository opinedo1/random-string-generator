from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


# logic for generating a random string and keeping a count
# uses redirect to avoind resubmission alert
def random(request):
    # checks to see that count isnt stored already then we increment if it is
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    # define our random string, then store it in session variable
    randomString = get_random_string(length=14)
    request.session['str'] = randomString
    print("Count: " + str(request.session['count']) + "String: " + request.session['str'])

    return redirect('/random_word_redirect')

# renders our html template
def random_word(request):
    return render(request, 'random_word.html')


# resets the count for random strings
def reset(request):
    if request.method == 'GET':
        return redirect('/')
    request.session.flush()
    return redirect("/random_word")
