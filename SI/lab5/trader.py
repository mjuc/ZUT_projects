import numpy as np
import random
import math
import matplotlib.pyplot as mpl

MUTATION_RATE = 1
MUTATION_REPEAT_COUNT = 2
CROSSOVER_RATE = 70
THRESHOLD = 850

avg=[]
best=[]
best_so_far=[]

cityCoordinates = [[5, 80], [124, 31], [46, 54], [86, 148], [21, 8],
                   [134, 72], [49, 126], [36, 34], [26, 49], [141, 6],
                   [124, 122], [80, 92], [70, 69], [76, 133], [23, 65]]

citySize = len(cityCoordinates)

class Genome():
    chromosomes = []
    fitness = 9999

def CreateNewPopulation(size):
    population = []
    for x in range(size):
        newGenome = Genome()
        newGenome.chromosomes = random.sample(range(1, citySize), citySize - 1)
        newGenome.chromosomes.insert(0, 0)
        newGenome.chromosomes.append(0)
        newGenome.fitness = Evaluate(newGenome.chromosomes)
        population.append(newGenome)
    return population

def distance(a, b):
    dis = math.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    return np.round(dis, 2)

def Evaluate(chromosomes):
    calculatedFitness = 0
    for i in range(len(chromosomes) - 1):
        p1 = cityCoordinates[chromosomes[i]]
        p2 = cityCoordinates[chromosomes[i + 1]]
        calculatedFitness += distance(p1, p2)
    calculatedFitness = np.round(calculatedFitness, 2)
    return calculatedFitness

def findBestGenome(population):
    allFitness = [i.fitness for i in population]
    bestFitness = min(allFitness)
    return population[allFitness.index(bestFitness)]

def TournamentSelection(population, k):
    selected = [population[random.randrange(0, len(population))] for i in range(k)]
    bestGenome = findBestGenome(selected)
    return bestGenome

def Reproduction(population):
    parent1 = TournamentSelection(population, 10).chromosomes
    parent2 = TournamentSelection(population, 6).chromosomes
    #while parent1 == parent2:
    #    parent2 = TournamentSelection(population, 6).chromosomes
    
    if random.randrange(0, 100)<CROSSOVER_RATE:
        return OrderOneCrossover(parent1, parent2)
    else:
        return CopyChromosomes(parent1,parent2)

def CopyChromosomes(parent1,parent2):
    size = len(parent1)
    child = [-1] * size
    
    for i in range(size):
        if random.randrange(0,1)==0:
            child[i]=parent1[i]
        else:
            child[i]=parent2[i]
    
    if random.randrange(0, 100) < MUTATION_RATE:
        child = SwapMutation(child)
    
    newGenome = Genome()
    newGenome.chromosomes = child
    newGenome.fitness = Evaluate(child)
    return newGenome

def OrderOneCrossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size

    child[0], child[size - 1] = 0, 0

    point = random.randrange(5, size - 4)

    for i in range(point, point + 4):
        child[i] = parent1[i]
    point += 4
    point2 = point
    while child[point] in [-1, 0]:
        if child[point] != 0:
            if parent2[point2] not in child:
                child[point] = parent2[point2]
                point += 1
                if point == size:
                    point = 0
            else:
                point2 += 1
                if point2 == size:
                    point2 = 0
        else:
            point += 1
            if point == size:
                point = 0

    if random.randrange(0, 100) < MUTATION_RATE:
        child = SwapMutation(child)

    newGenome = Genome()
    newGenome.chromosomes = child
    newGenome.fitness = Evaluate(child)
    return newGenome


def SwapMutation(chromo):
    for x in range(MUTATION_REPEAT_COUNT):
        p1, p2 = [random.randrange(1, len(chromo) - 1) for i in range(2)]
        while p1 == p2:
            p2 = random.randrange(1, len(chromo) - 1)
        log = chromo[p1]
        chromo[p1] = chromo[p2]
        chromo[p2] = log
    return chromo

def map(generation, allBestFitness, bestGenome, cityLoc):   
    startPoint = None
    for x, y in cityLoc:
        if startPoint is None:
            startPoint = cityLoc[0]
            mpl.scatter(startPoint[0], startPoint[1], c="green", marker=">")
            mpl.annotate("Origin", (x + 2, y - 4))
        else:
            mpl.scatter(x, y, c="black")

    xx = [cityLoc[i][0] for i in bestGenome.chromosomes]
    yy = [cityLoc[i][1] for i in bestGenome.chromosomes]

    for x, y in zip(xx, yy):
        mpl.text(x + 2, y - 2, str(yy.index(y)), color="green", fontsize=10)

    mpl.plot(xx, yy, color="red", linewidth=1.75, linestyle="-")
    mpl.show()

def GeneticAlgorithm(popSize, maxGeneration):
    population = CreateNewPopulation(popSize)
    generation = 0

    while generation < maxGeneration:
        generation += 1

        for i in range(int(popSize / 2)):
            population.append(Reproduction(population))

        for genom in population:
            if genom.fitness > THRESHOLD:
                population.remove(genom)

        averageFitness = round(np.sum([genom.fitness for genom in population]) / len(population), 2)
        bestGenome = findBestGenome(population)
        avg.append(averageFitness)
        best.append(bestGenome.fitness)
        tmp=best[0]
        for b in best:
            if b < tmp:
                tmp=b
        best_so_far.append(tmp)
        
        print("\n" * 5)
        print("Generation: {0}\nPopulation Size: {1}\t Average Fitness: {2}\nBest Fitness: {3}"
              .format(generation, len(population), averageFitness,
                      bestGenome.fitness))
        if generation==1 or generation==150 or generation==maxGeneration:
            map(generation,best_so_far,bestGenome,cityCoordinates)
    return generation

g=GeneticAlgorithm(popSize=100, maxGeneration=300)
x=np.arange(0,g,1)
mpl.plot(x,best)
mpl.show()
mpl.plot(x,avg)
mpl.show()
mpl.plot(x,best_so_far)
mpl.show()