from region import Region
import random
import numpy as np
from dataclasses import dataclass


@dataclass
class Child:

    def __init__(self, cromossome, parentIndex):
        self.cromossome = cromossome
        self.parentIndex = parentIndex

class Cromossome:


    def __init__(self, region):
        self.size = region.getNumOfCities()
        self.defaultCromossome = []
        self.region = region

        for i in range(0, self.size):
            self.defaultCromossome.append(i+1)

    
    # create objective Function Value
    def objectiveFunction(self, cromossome, region):
        result = 0.
        size = len(cromossome)

        for genIndex in range(0, size-1):
            result += region.getDistance(cromossome[genIndex],
                                         cromossome[genIndex+1])

        return result

    # print cromossome
    def printCromossome(self, cromossome, region):
        # print("ALL CROMOSSOMES (PATH)")
        for i in cromossome:
            print(i, end="-")
        print()    
        print("objective fuction value: {}".format(self.objectiveFunction(cromossome, region)))

    # return one cromossome
    def createRandomCromossome(self):
        # random.seed(0)
        copy = self.defaultCromossome.copy()
        random.shuffle(copy)
        return copy


    # mutation method
    # probability - [0, 1]
    def mutation(self, cromossome, probability):
        copy_cromossome = cromossome.copy()
        size = len(cromossome)

        for genIndex in range(0, size):

            value = random.uniform(0, 1)

            if value <= probability:
                indexChange = int((random.uniform(0, 1) * 100) % size)
                
                copy_cromossome[genIndex], copy_cromossome[indexChange] = copy_cromossome[indexChange], copy_cromossome[genIndex]

                if self.objectiveFunction(copy_cromossome, self.region) < self.objectiveFunction(cromossome, self.region):
                    cromossome = copy_cromossome


        return cromossome

                


    # crossover method between two cromossome
    def crossover(self, cromossomeA, cromossomeB, pcross):
        size = len(cromossomeA)
        child = np.zeros(size, dtype=np.int8)
        indexC = 0
        indexF = 0
        
        # before the cross point
        for indexP in range(0, pcross):
            child[indexC] = cromossomeA[indexP] 
            indexC += 1
            indexF = indexP

        indexF += 1
        # after the cross point
        while indexC < size:
            gen = cromossomeB[int(indexF % size)]
            
            if np.where(child == gen)[0].shape[0] is 0:
                child[indexC] = gen
                indexC += 1
            indexF += 1

        return child




