from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "This is about us",
        "my_number": 10,
        "my_boolean": True,
        "my_list": [123, 456, 789, 'abc'],        
    }
    return render(request, "about.html", my_context)
