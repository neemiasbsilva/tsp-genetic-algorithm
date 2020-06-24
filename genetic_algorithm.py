from cromossome import Cromossome, Child
import numpy as np
import random


class GeneticAlgorithm:

    def __init__(self, region, cromossomeOperation, populationSize, mutationProbability, numIteration, pcross):
        self.region = region
        self.cromossomeOperation = cromossomeOperation # private attribute
        self.populationSize = populationSize  # private attribute
        self.population = [] # private attribute
        for i in range(0, self.populationSize):
            self.population.append(self.cromossomeOperation.createRandomCromossome())
        self.mutationProbability = mutationProbability  # private attribute
        self.numIteration = numIteration  # private attribute
        self.pcross = pcross  # private attribute
        self.best = [] # private attribute
        self.isChange = False    # private attribute

    def setBestCromossome(self):
        # initially the first one is the best
        bestIndex = 0
        size = self.populationSize
        for i in range(1, size):
            if self.cromossomeOperation.objectiveFunction(self.population[i], self.region) < self.cromossomeOperation.objectiveFunction(self.population[bestIndex], self.region):
                bestIndex = i
        
        if len(self.best) == 0 or self.cromossomeOperation.objectiveFunction(self.population[bestIndex], self.region) < self.cromossomeOperation.objectiveFunction(self.best, self.region):
            self.best = self.population[bestIndex]
            self.isChange = True

        else:
            self.isChange = False

    def createInitialPopulation(self):
        size = len(self.population)

        for i in range(0, size):
            self.population[i] = self.cromossomeOperation.createRandomCromossome()

        self.setBestCromossome()

    
    def mutation(self):
        for cromossome in self.population:
            self.cromossomeOperation.mutation(cromossome, self.mutationProbability)

    
    def crossover(self):
        childs = []
        size = self.populationSize
        
        # r andom.seed(0)
        random.shuffle(self.population)
        # generation of childs
        for i in range(0, size-1): 
            c = Child(self.cromossomeOperation.crossover(self.population[i], self.population[i+1], self.pcross), i)
            childs.append(c)

            c=Child(self.cromossomeOperation.crossover(self.population[i+1], self.population[i], self.pcross), i+1)
            childs.append(c)
    
        # check if the child can be replace the fathers
        for child in childs:
            if self.cromossomeOperation.objectiveFunction(child.cromossome, self.region) < self.cromossomeOperation.objectiveFunction(self.population[child.parentIndex], self.region):
                 self.population[child.parentIndex] = child.cromossome

    def run(self):
        iteration = 0
        while iteration < self.numIteration:
            self.crossover()
            self.mutation()
            self.setBestCromossome()
            self.printBestSolution()
            iteration += 1


    def printPopulation(self):
        print("POPULATION SIZE: {}".format(self.populationSize))
        print("ALL CROMOSSOME OF POPULATION")
        for i, cr in enumerate(self.population):
            print("Cromossome {}: {}".format(i+1, cr))

    
    def printBestSolution(self):
        if self.isChange:
            print("The best cromossome is", end=" ")
            self.cromossomeOperation.printCromossome(self.best, self.region)




            
