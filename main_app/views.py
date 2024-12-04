from django.shortcuts import render

class Coffee:
    def __init__(self, name, brand, description, rating):
        self.name = name
        self.brand = brand
        self.description = description
        self.rating = rating

coffees = [
    Coffee('Peppermint Mocha', 'Starbucks', 'A chocolate-y treat seasonally made with peppermint.', 2),
    Coffee('Black Cat Classic Espresso', 'Cometeer Coffee', 'With notes of dark chocolate, raw sugar, and marshmallow.', 4),
    Coffee('The Daily', 'Cometeer Coffee', 'With notes of chocolate, caramel, and molasses.', 5),
    Coffee('Mocha Java', 'Cometeer Coffee', 'With notes of dark chocolate, almond, and berry.', 3)
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coffee_index(request):
    return render(request, 'coffee/index.html', {'coffees': coffees})