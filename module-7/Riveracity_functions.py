# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a neatly formatted City, Country string."""
    if population and language:
        return f"{city.title()}, {country.title()} - population {population}, {language.title()}"
    elif population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

# Call the function at least three times
print(city_country("santiago", "chile"))
print(city_country("paris", "france", 2148000))
print(city_country("tokyo", "japan", 13960000, "japanese"))
