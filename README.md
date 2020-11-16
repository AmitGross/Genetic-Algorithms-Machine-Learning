# Genetic-Algorithms-Machine-Learning
the code learns the best technique to track a desired object in a random position in 2D space. The code uses an aproach that theoretically derieves from evolutionary biology. ("genetic Algorithms") 

this code may present a poulation of animals (for example mice), (aka generation one) that searches for food, the 2 mice that would find food first will produce new offsprings, containing the genetic data (list of random Vectors).
then all the x offsprings of these two mice ( generation 2  ) would once again be put in a scene where the two fastes to reach the food (object) would reproduce and thier "offsprings" would be the 3rd generation.

therefore-
In this code, x number of agents (mice) , are given a list of y random amount of vectors (aka genetic data). the agent moves each iteration, accordingly to the random vector assigned to that iteration (V1 for first iteration, v2 for second iteration..)
Also an object is located in the 2D space randomly .
the agents(mice) would move randomly until reaching the object(food). once an agent(mouse) is on the object(food) it will stay there(eat..).  The duration of the agent(mouse) on the object (food)  will be calculated and documented.
after z time the scene will stop (end of generation) and the 2 agents(mice) with the highest score(ate the most) will exchange thier vectors(genetic data) randomly and reaching a new population of x agents(offsprings), that would proceed to the next scene(generation), where an object(food) will be randomly positioned in the 2D space once again.

additionally a mutant might occour in indeviduals.

controlling the factors of the mutation rates and **amount or length of sections of vectors to exchange** would impact the learning and behaviour of the agents.
**that is if two agents exchanges a short segment of thier v4-v8 vectors with one another or a long segment of v4-v500 (aka genetic recombination, that is replacing segments of each of the parents coorisponding chromosomes) **  - Also they may do many of those exchanges or few 

Also changing some of the factors could change the behaviour, such as multiple food sources.
