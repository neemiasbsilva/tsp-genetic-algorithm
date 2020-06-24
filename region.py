from city import City
import math

class Region:


    def __init__(self):
        self.mapCities = {}  # private attribute
    
    # create a method to clean the region
    def clean(self):
        self.mapCities.clear()

    # create a method to add city
    def add(self, City):
        id = self.getNumOfCities() + 1
        self.mapCities[id] = City
    

    # cal the distance between city A and B
    def getDistance(self, id_cityA, id_cityB):
        cityA = self.mapCities[id_cityA]
        cityB = self.mapCities[id_cityB]
        
        if cityA is None or cityB is None:
            print("Invalid City ID")
            return

        # euclidian distance           
        return math.sqrt((cityA.x - cityB.x)**2 + (cityA.y - cityB.y)**2)

    
    # number of Cities
    def getNumOfCities(self):
        return len(self.mapCities)


    # print the currentle city
    def printCurrentle(self):
        for k, v in self.mapCities.items():
            print("City {}: ({}, {})".format(k, v.x, v.y))



