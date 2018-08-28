from itertools import chain
import jinja2
import pickle
import subprocess

import data_plot


FILENAME = 'histogram'
command_line = f'povray  +i{FILENAME}.pov  +o{FILENAME}.png +fn +D +P +w800 +h600 +a0.9'

POV_COLORS = ['LightBlue', 'LimeGreen', 'Maroon', 'MediumAquamarine', 'MediumBlue', 'MediumForestGreen', 'MediumGoldenrod', 'MediumOrchid', 'MediumSeaGreen', 'MediumSlateBlue', 'MediumSpringGreen', 'MediumTurquoise', 'MediumVioletRed', 'MidnightBlue', 'Navy']



def main():
    data = pickle.load(open("aquaresources.pickle", "rb"))
    data = data[:10]

    data_points = []
    for country in data:
        for year in country[1]:
            if not year.isdigit():
                continue
            data_points.append(country[1][year])
    normalizer = data_plot.NormalIter(data_points, scale=10)
    normalizer.offset = 0

    output = {
        'years': None,
        'position': None,
        'color': 'rgb <1, 1, 0>',
    }

    countries = []

    for i, (country, color) in enumerate(zip(data, POV_COLORS)):
        v = output.copy()
        v['position'] = i
        v['color'] = color
        v['name'] = country[0]
        year_data = []
        for key in sorted(country[1].keys()):
            if not key.isdigit():
                continue
            year_data.append(normalizer.single(country[1][key]))

        v['years'] = year_data
        countries.append(v)

    templ = jinja2.Template(open("histogram.templ.pov").read())
    open('histogram.pov', 'wt').write(templ.render(countries=countries, length=len(countries) ))

    subprocess.call(command_line, shell=True)


main()

