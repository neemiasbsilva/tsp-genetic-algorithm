import pandas as pd
import numpy as np
from city import City
from region import Region
from cromossome import Cromossome
from genetic_algorithm import GeneticAlgorithm


def get_dataset(file_name):

    df = pd.read_csv(file_name, header=None, index_col=False)
    print(df.head())
    array = df.to_numpy()
    return array

if __name__ == "__main__":

    cities = get_dataset("./input/48-capitals-us.csv")

    region = Region()

    for i in cities:
        region.add(City(i[1], i[2]))

    # region.add(City(0, 0))
    # region.add(City(8.3, 16))
    # region.add(City(16, 12.8))
    # region.add(City(2.23, 15))
    # region.add(City(9, 7.87))
    # region.add(City(6.7, 12))

    crOp = Cromossome(region)

    genetic = GeneticAlgorithm(region=region, cromossomeOperation=crOp, populationSize=500, mutationProbability=0.1, numIteration=50, pcross=24)

    genetic.run()



    


