import random
from tkinter import *
import pygame
import random
pygame.init()
white=(255,250,255)
yellow=(255,255,0)
grey=(100,100,100)
font = pygame.font.SysFont("comicsansms", 20)
#this is accually a list of vectors, each will be called a gene
list_of_all_possible_genes=[[0,2],[1,2],[2,2],[2,1],[3,1],[3,0],[3,-1],[2,-1],[2,-2],[1,-2],[0,-2],[-1,-2],[-2,-2],[-2,-1],[-3,-1],[-3,0],[-3,1],[-2,1],[-2,2],[-1,2]]

# records some data for as to analyze
class mainstatus():
    def __init__(self):
        self.gen=0
        self.best=0
        self.last_best=0
        self.counter=400
        self.number_of_fitters_last_gen=0
        self.best_number_of_fitters=0
        self.food_pos=0
main_stats=mainstatus()
main_stats.food_pos=(random.randint(100,900),random.randint(100,700) )
print(main_stats.food_pos)


#shows the data on the screen

def status(screen):
    status_to_present=("genaration:"+str(main_stats.gen)+"      best eater:"+str(main_stats.best) +  "   (gen "+str(int(main_stats.gen-1))+" best eater was: " +str(main_stats.last_best)+")")
    eaters_string=( "number of eaters:         last gen:  "+ str(main_stats.number_of_fitters_last_gen)+ "and best record for number of eaters is: "+ str(main_stats.best_number_of_fitters))
    eaters_stats=font.render(eaters_string,True,yellow)
    text = font.render(status_to_present, True, white)
    time_to_present=font.render("time "+ str(main_stats.counter),True,white)
    screen.blit(text, (150, 150))
    screen.blit(eaters_stats, (150, 175))
    screen.blit(time_to_present, (100, 100))
#genarates an agent, takes a genome (set of vectors) as input ; -1a- [ [x1,y1], [x2,y2]...[xn,yn]]
#records x and y position, fitness



class agent(pygame.sprite.Sprite):
    def __init__(self,genome):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.image.fill(grey)
        self.rect = self.image.get_rect()
        self.positionx=505
        self.positiony=700
        self.genome=genome
        self.eat=0
# this function iterate (time as a variable for iterator) the set of vectors (genome) and changes the xpos and ypos (linear addition) according to the current vector (gene))

    def move(self,time):
        #print(main_stats.food_pos)
        #stops moving and adding to the fitness of the agent

        if main_stats.food_pos[0]<self.positionx<main_stats.food_pos[0]+30:
            if main_stats.food_pos[1]>self.positiony>main_stats.food_pos[1]-40 :
                self.eat+=1
                return




        self.positionx+=self.genome[time][0]
        self.positiony += self.genome[time][1]

        self.rect.center= (self.positionx,self.positiony)



#records parents genome, essential for the induction of first fitness test . possibly theres an option to delete this class and put the information elsewhere for esthetic reasons

class parents_calss:
    def __init__(self,parent_one,parent_two):
        self.parent_one=parent_one
        self.parent_two=parent_two




# function to create mutations, take a an inpus: a) list of genomes as following=(will be called genome) -2a- [   [ [x1,y1], [x2,y2]...[xn,yn] ]1 ,[x1,y1], [x2,y2]...[xn,yn] ]2 .. [x1,y1], [x2,y2]...[xn,yn] ]n ]
                                                # b) a mutation rate, where the user shall pick a number from 0 to 1000. choosing 1 will give each gene a chance to be changed by using the function 1/1000.
def creating_mutation(list_of_genomes,mutation_rate):
    def create_single_mutation(rate):

        # decides wither a mutation would accour
        var = random.randint(0, 1000)
        if rate > var:
            return True
        else:
            return False


    new_list_of_genomes=[]
    for genome in list_of_genomes:
        new_genome = []

        for gene in genome:

            chance_to_mutate=create_single_mutation(mutation_rate)
            if chance_to_mutate:
                #creates randlomly a vector(gene) from all possible genes
                new_mutat_gene=list_of_all_possible_genes[random.randint(0,19)]
                #scaling the vector allows larger segments of movement for each time point.
                scaledx = new_mutat_gene[0] * random.randint(10, 20)
                scaledy = new_mutat_gene[1] * random.randint(10, 20)

                new_genome.append([scaledx,scaledy])
            else:
                new_genome.append(gene)
        new_list_of_genomes.append(new_genome)

    return new_list_of_genomes
# function to compare fitness, takes a list of agents as following- [agent1,agent2 ... agentn]
#and returns the genomes of the 2 most succsessfull agents

def fitness_evaluation(list_of_agents):
    #list that keeps track of all ftiness rates and thier corresponding genome as following: [ [eating_rate1,[genome]1]1, [eating_rate2,[genome]2]2..]

    fitness_rates = []
    number_of_fitters=0
    for agent in list_of_agents:
        if agent.eat > 0:
            number_of_fitters+=1
            fitness_rates.append([agent.eat, agent.genome])

    first = 0
    second = 0

    for i in fitness_rates:
        if i[0] > first:
            first = i[0]
            main_stats.last_best=first
        else:
            if i[0] > second:
                second = i[0]
    if first>main_stats.best:
        main_stats.best=first
    #parents will now be selected by choosing the 2 best fitters
    genome_one = []
    genome_two = []
    for i in fitness_rates:
        if i[0] == first:
            genome_one = i[1]
        else:
            if i[0] == second:
                genome_two = i[1]
    #this is just for esthetics, to record data and pretsnt on screen
    main_stats.number_of_fitters_last_gen=number_of_fitters
    if main_stats.best_number_of_fitters<number_of_fitters:
        main_stats.best_number_of_fitters=number_of_fitters
    #so does function basiclly returns a list of the best 2 genomes
    return([genome_one,genome_two])
# this function is used to genarate the first genaration, takes number of individuales to create as input and its output is list of genomes

def genrarate_genomet(genome_length):
    genome = []

    scaled_genes = []
    for possible_gene in list_of_all_possible_genes:
        # scaling the vector(gene) allows larger segments of movement for each time point.
        scaledx=possible_gene[0]*random.randint(10,20)
        scaledy=possible_gene[1]*random.randint(10,20)
        scaled_genes.append([scaledx,scaledy])
    #choosing a random gene from the scaled genes list
    for i in range(0, genome_length):
        randomize_gene = random.randint(0, 19)
        genome.append(scaled_genes[randomize_gene])
    return genome
genome=genrarate_genomet(1000)

# takes input two genomes and amount of offsprings wanted, genarates offsprings with recombinated genome [switching vectors from the n vector to the k vector, where n and k are chosen randomly]
def mate(genome_one,genome_two,offsprings):
    all_offsprings = []

    for i in range(0,offsprings):
        recombinate=genome_one.copy()
        #randomize the recombintaed segments length
        lucos_to_recombinate_lnegth=random.randint(1,len(genome_one)-1)
        #randomizing where the segment of recombinated dna would start
        lucos_to_recombinate_start=random.randint(1,len(genome_one)-lucos_to_recombinate_lnegth)
        #takes the recombinated segment from genome two and replaces it in genome one
        segment_from_genome_two=genome_two[lucos_to_recombinate_start:lucos_to_recombinate_lnegth+lucos_to_recombinate_start]
        recombinate[lucos_to_recombinate_start:lucos_to_recombinate_lnegth+lucos_to_recombinate_start]=segment_from_genome_two
        all_offsprings.append(recombinate)

    return all_offsprings

#takes a list of agents and simulates thir fitness according to genome,returns a list of the 2 best genomes
def simulation(list_of_agents):
    main_stats.gen+=1
    #starts a screen for simulation
    screena = pygame.display.set_mode((1000, 900))

    def draw_food_on_screen():

        pygame.draw.circle(screena, yellow, main_stats.food_pos, 10, 10)

    counter=0
    running = True
 #starts the simulation, that ends when counter reaches 200
    while running:
        draw_food_on_screen()

        #stats for showing on screen
        main_stats.counter=400-counter
        status(screena)


        if counter>400:
            main_stats.counter=400
            running=False

        for agent in list_of_agents:
            #moves the agent, function is in detailes in agent class
            agent.move(counter)
            #method to record the agents class (pygames "sprite")
            all_sprites.add(agent)
        #draws  all agents(sprites) on screen
        all_sprites.draw(screena)
        #this for loop firstly is essential to run pygame screens, also i added options to interact with the ptogram as following
        for event in pygame.event.get():
            #if key is pressed
            if event.type == pygame.KEYDOWN:
                    #q is pressed then the program stops
                if event.unicode == "q":
                    pygame.display.quit()
                        # if n is pressed the current simulation will end and the next will start
                if event.unicode == "n":
                    counter=399


        pygame.display.flip()
        pygame.time.wait(70)
        screena.fill([0,0,0])
        counter+=1


    most_fit=fitness_evaluation(list_of_agents)
    parents=[most_fit[0],most_fit[1]]
    return parents

#records all agents, will be erased each simulation
all_sprites =pygame.sprite.Group()

#creating first genaration
list_of_subjects=[]
for i in range(0,200):
    list_of_subjects.append(agent(genrarate_genomet(1000)))

#simulating first genaration
first_parents=simulation(list_of_subjects)

#indection for the rest of the simulations
while True:
    main_stats.food_pos=(random.randint(100,900),random.randint(100,700))
    all_sprites.empty()

    print(f" genaration: {main_stats.gen-1}")
    print(f" best eater: {main_stats.last_best}")
    print(f" number_of_fitters {main_stats.number_of_fitters_last_gen}")
    #takes the last parents the were recorded
    parents=parents_calss(first_parents[0],first_parents[1])

    list_of_agentst = []
    #mate between parents, takes as input parents and number of offsprings, returns list of genoms
    all_offsprings = mate(parents.parent_one, parents.parent_two, 40)
    #create mutations, takes as input list of genomes and mutation rate
    all_offsprings = creating_mutation(all_offsprings,50)

    #create agents for next simulation according to mutated genomes
    for genome in all_offsprings:
        list_of_agentst.append(agent(genome))
    #starts the simulation, takes as input list of agents and its output will be the new parents
    new_parents = simulation(list_of_agentst)











