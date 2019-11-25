import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle
from country_codes import get_country_code


# Load the data onto a list
filename = "population_data.json"
f = open(filename)
pop_data = json.load(f)
f.close()

# Build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif 1000000000 > pop > 10000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop
# See how many countries are in each level
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm = World()
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2016, by Country'
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1b', cc_pop_3)

wm.render_to_file('world_population.svg')

