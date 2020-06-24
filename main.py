import pandas as pd
import numpy as np
from city import City
from region import Region
from cromossome import Cromossome
from genetic_algorithm import GeneticAlgorithm
import argparse
import os

parse = argparse.ArgumentParser(description="Using GA to solve the Traveling Salesman Problem Arguments")

parse.add_argument("-file_name", action="store", required=True, help="path of region of cities", dest="file_name")
parse.add_argument("-population_size", action="store", required=True, help="size of population", dest="population_size")
parse.add_argument("-mutation_probability", action="store", required=True, help="mutation rate", dest="mutation_probability")
parse.add_argument("-num_iteration", action="store", required=True, help="number of iterations", dest="num_iteration")

def get_dataset(file_name):

    df = pd.read_csv(file_name, header=None, index_col=False)
    array = df.to_numpy()
    
    return array

if __name__ == "__main__":

    arguments = parse.parse_args()

    file_name = arguments.file_name
    population_size = int(arguments.population_size)
    mutation_probability = float(arguments.mutation_probability)
    num_iteration = int(arguments.num_iteration)


    # cities = get_dataset("./input/48-capitals-us.csv")
    cities = get_dataset(file_name)
    region = Region()

    for i in cities:
        region.add(City(i[1], i[2]))

    crOp = Cromossome(region)
    genetic = GeneticAlgorithm(region=region, cromossomeOperation=crOp, populationSize=population_size,
                               mutationProbability=mutation_probability,  numIteration=num_iteration, pcross=region.getNumOfCities()//2)

    genetic.run()



    


