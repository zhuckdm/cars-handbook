def get_filtered_by_registration_plate(cars, plate):
    return cars.filter(registration_plate=plate)


def get_filtered_by_make(cars, make):
    return cars.filter(make=make)


def get_filtered_by_model(cars, model):
    return cars.filter(model=model)


def get_filtered_by_color(cars, color):
    return cars.filter(color=color)


def get_filtered_by_manufacture_year(cars, year, operator=None):
    if operator == '>':
        return cars.filter(manufacture_year__gt=year)
    if operator == '<':
        return cars.filter(manufacture_year__lt=year)
    return cars.filter(manufacture_year=year)


def get_filtered_by_horsepower(cars, horsepower, operator=None):
    if operator == '>':
        return cars.filter(horsepower__gt=horsepower)
    if operator == '<':
        return cars.filter(horsepower__lt=horsepower)
    return cars.filter(horsepower=horsepower)


def get_filtered_by_mileage(cars, mileage, operator=None):
    if operator == '>':
        return cars.filter(mileage__gt=mileage)
    if operator == '<':
        return cars.filter(mileage__lt=mileage)
    return cars.filter(mileage=mileage)


def get_filtered_by_price(cars, price, operator=None):
    if operator == '>':
        return cars.filter(price__gt=price)
    if operator == '<':
        return cars.filter(price__lt=price)
    return cars.filter(price=price)


CARS_FILTERS = {
    'registration_plate': get_filtered_by_registration_plate,
    'make': get_filtered_by_make,
    'model': get_filtered_by_model,
    'color': get_filtered_by_color,
    'manufacture_year': get_filtered_by_manufacture_year,
    'horsepower': get_filtered_by_horsepower,
    'mileage': get_filtered_by_mileage,
    'price': get_filtered_by_price,
}
