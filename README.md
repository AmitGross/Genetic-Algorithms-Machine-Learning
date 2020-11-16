# Genetic-Algorithms-Machine-Learning
the code learns the best technique to track a desired object in a random position in 2D space. The code uses an aproach that theoretically derieves from evolutionary biology. ("genetic Algorithms") 

this code mimics a poulation of mice that searches for food, the 2 mice that would find food first will produce new offsprings, containing the genetic data (Vectors).
then all the offsprings of generation 2 would once again ut in a scene where the two fastes to reach the food (object) would reproduce and thier "offsprings" would be the 3rd generation.

therefore-
In this code, x number of agents , are given a list of y random amount of vectors. the agent moves each iteration, accordingly to the random vector assigned to that iteration (V1 for first iteration, v2 for second iteration..)
Also an object is located in the 2D space randomly .
the agents would move randomly until reaching the object. once an agent is on the object it will stay there and the time the agent was there will be docyumented.
after z time the scene will stop and the 2 agents with the highest score will exchange thier vectors randomly and reaching a new population of x agents, that would proceed to the next scene, where an object will be randomly positioned in the 2D space once again.

additionally a mutant might occout in indeviduals.

controlling the factors of the mutation rates and **amount or length of sections of vectors to exchange** would impact the learning and behaviour of the agents.
**  that is if two agents can exchane thier v4-v8 with one another or v4-v500, Also they may do many  of those exchanges or few  **

Also changing some of the factors could change the behaviour, such as multiple food sources.
