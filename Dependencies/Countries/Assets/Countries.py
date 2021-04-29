import json

with open("ISO2_to_capital.json", encoding="utf-8") as file:
    ISO2_to_capital = json.load(file)
with open("ISO2_to_currency.json", encoding="utf-8") as file:
    ISO2_to_currency = json.load(file)
with open("ISO2_to_ISO2_continents.json", encoding="utf-8") as file:
    ISO2_to_ISO2_continents = json.load(file)
with open("ISO2_to_ISO3.json", encoding="utf-8") as file:
    ISO2_to_ISO3 = json.load(file)
with open("ISO2_to_names.json", encoding="utf-8") as file:
    ISO2_to_names = json.load(file)
with open("ISO2_to_phone.json", encoding="utf-8") as file:
    ISO2_to_phone = json.load(file)

countries: dict = {}


def get_continent(iso2_continent: str):
    """Returns full continent name based on ISO continent code
    """
    if iso2_continent == "EU":
        return "Europe"
    elif iso2_continent == "AS":
        return "Asia"
    elif iso2_continent == "AF":
        return "Africa"
    elif iso2_continent == "OC":
        return "Oceania"
    elif iso2_continent == "NA":
        return "North America"
    elif iso2_continent == "SA":
        return "South America"
    elif iso2_continent == "AN":
        return "Antarctica"
    else:
        raise ValueError


for name, capital, continent, currency, phone, ISO3 in zip(ISO2_to_names, ISO2_to_capital, ISO2_to_ISO2_continents,
                                                           ISO2_to_currency, ISO2_to_phone, ISO2_to_ISO3):
    countries[ISO2_to_names[name].rstrip().lstrip()] = {
        "Capital": ISO2_to_capital[name].rstrip().lstrip(),
        "Continent": get_continent(ISO2_to_ISO2_continents[name].rstrip().lstrip()),
        "ISO2_Continent": ISO2_to_ISO2_continents[name].rstrip().lstrip(),
        "Currency": ISO2_to_currency[name].rstrip().lstrip(),
        "Phone": ISO2_to_phone[name].rstrip().lstrip(),
        "ISO2": name.rstrip().lstrip(),
        "ISO3": ISO2_to_ISO3[name].rstrip().lstrip()
    }

countries_list: list = list(countries.keys())
longest_name_length: int = 0
longest_name: str = ""
position: int = 0

for country in countries:
    if len(countries[country]["Capital"]) > longest_name_length:
        longest_name = countries[country]["Capital"]
        longest_name_length = len(countries[country]["Capital"])

print(longest_name, longest_name_length)

# with open("Countries.json", "w", encoding="utf-8") as file:
#     json.dump(countries, file, indent=2, sort_keys=True)
