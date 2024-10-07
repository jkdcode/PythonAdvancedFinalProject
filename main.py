"""
This script generates a graph showing the number of internet users per continent over time,
using real data from a csv file.
"""

import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  """
  Generate population dictionary from csv file
  Return a dictionary that follows this structure:
  {
    "Africa": { population: [100, 200, 300, ...], year: [2000, 2001, 2002, ...]},
    "Asia": { population: [100, 200, 300, ...], year: [2000, 2001, 2002, ...]},
    ...
  }
  """
  output = {}

  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
      continent = line['continent']
      year = line['year']
      population = line['population']

      if continent not in output:
        output[continent] = {'population': [], 'year': []}

      output[continent]['population'].append(int(population))
      output[continent]['year'].append(int(year))

  return output
  
def generate_population_plots_from_dictionary(population_dictionary):
  """
  Generate population plots from population dictionary
  One plot per continent + world total
  IBM Design Library color palette: https://davidmathlogic.com/colorblind/#%23648FFF-%23785EF0-%23DC267F-%23FE6100-%23FFB000
  """
  color_dictionary = {
    # Color palette is colorblind accessible (IBM Design Library)
      "Africa": "#332288",
      "Asia": "#785EF0",
      "Europe": "#DC267F",
      "North America": "#FE6100",
      "South America": "#FFB000",
      "World": "black"
  }
  
  for continent in population_dictionary:
    year = population_dictionary[continent]['year']
    population = population_dictionary[continent]['population']
    
    if continent == "World":
      plt.plot(year, population, label=continent, color=color_dictionary[continent], linestyle="--")
    else:
      plt.plot(year, population, label=continent, marker="o", color=color_dictionary.get(continent, 'blue'), markersize=3)

  

  plt.title("Internet Users Per Continent", 
    fontdict={'fontsize': 20, 'fontweight': 'bold', 'family': 'sans-serif'}, 
    pad=20)
  plt.xlabel("Year", fontdict={'fontsize': 14, 'family': 'sans-serif'})
  plt.ylabel("Internet Users (in Billions)", fontdict={'fontsize': 14, 'family': 'sans-serif'})
  plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
  plt.tight_layout()
  plt.grid(True, which='both', linewidth=0.5, alpha=0.5)
  plt.show()

filename = 'data.csv'

"""
Display the population plots
"""
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)