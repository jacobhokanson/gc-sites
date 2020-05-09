from django.shortcuts import render
from django.http import HttpResponse
from turtle_words.svg_turtle import svg_image
import random
import requests
from turtle_words.forms import SearchWord, SignUp
from turtle_words.models import TurtleBrand, turtle_calls, TurtleBrandSignup

def make_color():
    color_hex = ""
    for c in range(0, 6):
        color_hex = color_hex + random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"])
    return "#" + color_hex

# part_of_speech_dict = {"n":"Noun", "v":"Verb", "adv":"Adverb", "adj":"Adjective"}

def index(request):
    url = 'https://api.datamuse.com/words?rel_trg=turtle&md=d'
    response = requests.get(url)
    # above line should have a 'requests' get from the provided API with parameters
    word_list = random.choices(response.json(), k=10)
    turt = svg_image(make_color(), make_color())
    turt2 = svg_image(make_color(), make_color())
    my_turtle_data = {"turtle_1": turt, "turtle_2": turt2 , "turtle_words": word_list}
    turtle_call = turtle_calls(request_url=url)
    turtle_call.save()
    return render(request, 'turtle_words/index.html', context=my_turtle_data)

def turtle_brand(request):
    url_word = request.GET.get('word', 'turtle')
    try:
        response = requests.get('https://api.datamuse.com/words?rel_jjb=' + url_word)
        ideas_list = response.json()
    except:
        ideas_list = {"word":"nothing"}
        # above line should have a 'requests' get from the provided API with parameters

    brand_color = make_color()
    turt = svg_image(brand_color, "#000000")
    brand_dictionary = {"brand_idea":random.choice(list(ideas_list)), "brand_color":brand_color, "turtle_1": turt}
    return render(request, 'turtle_words/turtle_brand.html', context=brand_dictionary)

def turtle_brand_search(request):
    if request.method == 'POST':
        my_form = SearchWord(request.POST)
        if my_form.is_valid():
            my_data = my_form.cleaned_data
            try:
                response = requests.get('https://api.datamuse.com/words?rel_jjb=' + my_data['your_search'])
                ideas_list = response.json()
            except:
                ideas_list = {"word":"nothing"}
            # above line should have a 'requests' get from the provided API with parameters

            brand_color = make_color()
            turt = svg_image(brand_color, "#000000")
            chosen_word = random.choice(list(ideas_list))
            tb = TurtleBrand(name = chosen_word, color = brand_color, seed_word = my_data['your_search'])
            tb.save()
            brand_dictionary = {"brand_idea":chosen_word, "brand_color":brand_color, "turtle_1": turt}

            return render(request, 'turtle_words/turtle_brand.html', context=brand_dictionary)
    else:
        new_form = SearchWord()

    return render(request, 'turtle_words/turtle_brand_search.html', {'form': new_form})

def turtle_brand_signup(request):
    if request.method == 'POST':
        my_form = SignUp(request.POST)
        if my_form.is_valid():
            my_data = my_form.cleaned_data

            tbs = TurtleBrandSignup(first_name=my_data['first_name'], last_name=my_data['last_name'], source=my_data['where_did_you_hear'])
            tbs.save()

            return render(request, 'turtle_words/turtle_brand_thanks.html', context={'votername':my_data['first_name']})
    else:
        new_signup_form = SignUp()

    return render(request, 'turtle_words/turtle_brand_signup.html', {'signup_form': new_signup_form})
