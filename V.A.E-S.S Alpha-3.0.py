''' Rainworld Sim  rainmland'''
#necessary
import time
import random
#intro
print('__          __  _ ')                         
print('\ \        / / | |')                        
print(" \ \  /\  / /__| | ___ ___  _ __ ___   ___") 
print("  \ \/  \/ / _ \ |/ __/ _ \|  '_ ` _ \/ _ \ ")
print('   \  /\  /  __/ | (_| (_) | | | | | |  __/')
print('    \/  \/ \___|_|\___\___/|_| |_| |_|\___|')
time.sleep(1)
print('   _           ')
print('  | |       	  ')	
print('  | |_ ___     ')
print('  | __/ _ \    ')
print('  | || (_) |   ')
print('   \__\___/    ')
time.sleep(1)
print('  _ ')
print(' (_)')
time.sleep(1)    
print('       _ ')
print('      (_)')
time.sleep(1)    
print('             _ ')
print('            (_)') 
time.sleep(1.25)          
print('__      __         ______        _____   _____   _  ')  #Very Accurate Eco-System Simulator
print('\ \    / / /\     |  ____|      / ____| / ____| | | ')
print(' \ \  / / /  \    | |__  ______| (___  | (___   | | ')
print('  \ \/ / / /\ \   |  __||______|\___ \  \___ \  | | ')
print('   \  / / ____ \ _| |____ _   _ ____) | ____) | |_| ')
print('    \(_)_/    \_(_)______(_) (_)_____(_)_____/  (_) ')
time.sleep(0.75)
print('A.K.A Very Accurate Eco-System Simulator (ALPHA-2.0)')
print()
#patch notes
time.sleep(2)
print('Alpha 1.0 has introduced:')
print('-Simulation is much more accurate and random now, due to being rewritten to be percentage based along with many other balancing changes.')
print('-Added fully functional seasons with side-effects')
print('-Added year counter')
print('-Added nuke and actual functioning radiation (lol)')
print("-Added alot more events, making it more interesting compared to the Pre-Alpha's singular event...")
print('-Polished intro and edited alot of text.')
print('-Prey population growth now scales based on the number of plants (Used to be completely flat growth number)')
print('-Added congratulatory message each time your ecosystem survives a year (You should probably follow the default numbers the first go around...)')
print("-Made the ending message less cancer with actual stats (It's only a single stat)")
print('-Overhauled climate change completely, percentage based, extra mode, more polished.')
print('-Added snarky code comments and under the hood changes you will never see')
print('-Made everything easier to understand for the player.')
print('-Made exit less sudden (and now with added coolness)')
print('-Added event based on the options you selected at the start! (More soon to come!)')
print('-General polish everywhere.')
print('-Added patch notes (bruh)')
print()
time.sleep(1)
print('Alpha 1.5 has introduced:')
print('Everything (Besides events) is now percentage based!')
print('Major balancing changes. (simulation can last more than 6 years!)')
print('New predator control event.')
print('Removed cuss words')
print('Changed file name to the actual name (bruh)')
print()
time.sleep(1)
print('Alpha 2.0 has introduced:')
print('Weather system has been implemented')
print('More events have been added')
print('Overhauled radiation completely.')
print('Alot of improvements to print and output code along with general polish')
time.sleep(1)
print('Alpha 3.0 has introduced')
print('New species!!! The scavengers, which feast upon prey and plants now help balance out the simulation.')
print('More events!')
print('Alot of balancing changes.')
print('Small predator hunting overhaul.')
print()
print('P.S, it is recommended that you play this through python itself (It looks like a terminal). Everything is case sensitive, type EXACTLY what it tells you to. Besides the predators, prey and plants! Those are all yours :)')
print()
time.sleep(3)
print()
game = input('Play or Exit?-')          #menu
if game == 'Exit':
    print('Bye bye!')
    time.sleep(1.5)
    print('jerk...')
    time.sleep(0.25)
    exit()



#setup
predator = int(input('Enter the amount of predators (Should not be very high) (25)-'))
prey = int(input('Enter the amount of prey (Should be many times higher than predators) (1000)-'))
plants = int(input('Enter the amount of plants (Should be alot more than prey) (10000)-'))
scavenger = int(input('Enter the amount of scavengers (Should be inbetween prey and predators) (300)-'))

climatechange = input('Is there climate change? YES/NO (Answer in all caps)')


ccmild = 0      #climate modifiers
ccmoderate = 0
cchigh = 0
cckillme = 0
                 


if climatechange == 'YES':																	#climate change modifier
    climatemode = input('What mode of climate change? Mild, Moderate, High or are you a Bad Person?-')
    if climatemode == 'Mild':
         ccmild = 1
         print('Climate change is mild')
    elif climatemode == 'Moderate':
        ccmoderate = 1
        print('Climate change is moderate')
    elif climatemode == 'High':
        cchigh = 1
        print('Climate change is high')
    elif climatemode == 'Bad Person':
        cckillme = 1
        print('Bad boy ;3')

predatortype = input('What type of predators are we dealing with? (Regular, Fast Breeder, Fast Hunter.)-')

ptregular = 0
ptfb = 0
ptfh = 0

if predatortype == 'Regular':              #predator modifiers
    ptregular = 1
elif predatortype == 'Fast Breeder':
    ptfb = 1
elif predatortype == 'Fast Hunter':
    ptfh = 1

season = 0     #summer = 1-3 , autumn = 4-6, winter = 7-9, spring = 10-12
years_survived = 0          #stat to display at ecosystem collapse

radiation = 0           #random buffs and debuffs
    
#simulation start, rewrite nearly done 
print()
print("Every 1 equals 10, so 100 is actually equal to 1000, that's why there are decimals. TLDR SCALE 1/10")
print('Each tick is 1 month')
print()
if ccmild == 1 or ccmoderate ==1 or cchigh == 1:
    print('Climate change will heavily affect the already fragile and damaged ecosystem...')
if cckillme == 1:
    print("This simulation won't last very long will it...")
print()

while True:     #somehow works idk, dont touch too much
    #plant code
    if plants >= 1:
        plants += plants * 0.075    #plant growth
          
        if season>=1 and season <=3:     #summer
            plants += plants * 0.075
        elif season>=4 and season <=6:   #autumn
            plants -= plants * 0.04
        elif season>=7 and season <=9:   #winter
            plants -= plants * 0.1
        elif season>=10 and season <=12: #spring
            plants += plants * 0.25
            
        if ccmild == 1:     #climate change debuffs
            plants -= plants * 0.005
        elif ccmoderate == 1:
            plants -= plants * 0.01
        elif cchigh == 1:
            plants -= plants * 0.05
        elif cckillme == 1:
            plants -= plants * 0.1
            
    #prey code
    if plants > 0 and prey >= 2:
        plants -= prey // 1.25   #prey plant eating
        if plants > 6000:        #prey reproduction
           prey += prey * 0.025        #scales based on plant population
        if plants <= 3500:           #wtf why is it based on an arbitrary number :skull_emoji:
           prey -= prey * 0.02
        if plants<=999:
           prey -= prey * 0.08
           
        if season>=1 and season <=3:   #summmer    #prey percentage reproduction
            prey+= prey * 0.012
        if season>=4 and season <=6:   #autumn
            prey-=prey * 0.001
        if season>=7 and season <=9:   #winter 
            prey-=prey * 0.025
        if season>= 10 and season <=12:#spring
            prey+=prey * 0.027
           
    
    
    #scav code
    scavenger_rate = 1                   #change if balancing eating
    if scavenger >= 1:                  
        prey -= prey * 0.002 * scavenger_rate         #scav eating
        plants -= plants * 0.001 * scavenger_rate

                     #scav reproduction
        if season>=1 and season <=3:   #summmer    #scav percentage reproduction
            scavenger+= scavenger * 0.05
        if season>=4 and season <=6:   #autumn
            scavenger-=scavenger * 0.01
        if season>=7 and season <=9:   #winter 
            scavenger-=scavenger * 0.025
        if season>= 10 and season <=12:#spring
            scavenger+=scavenger * 0.075
    
    
    
    
    
    
    
    #pred code
    predator_rate = 1
    if prey > 0 and predator >= 2:
        prey -= predator // 2  #predator hunting
        scavenger -= scavenger * 0.001 * predator_rate
        if ptfh == 1:
            prey-= predator //5
            scavenger -= predator//1.5
            
        predator += plants * 0.0001            #predator reproduction
        if ptfb == 1:
            predator += predator * 0.0002
        
   
    #starvation code
    if prey<1 and predator>1:  #no food :(   (predator)
        predator *= 0.8
        
    if prey>1 and plants<1:   #no food 2 (prey)
        prey *= 0.8
        
    if scavenger>1 and plants<1 and prey<1:  #no food 3 (scav)
        scavenger *= 0.8
        
    if predator>prey:   #not enough food (predator)
        predator-=1
        
    if prey>plants:   #not enough  food2 (prey)
        prey-=5
        
        
        
    if predator>1:   #natural predator death idk
        predator-=0.5
        
    #numbers wont go into negatives
    plants = max(plants, 0)
    prey = max(prey, 0)
    predator = max(predator, 0)
    
    
    #events
    
    
    if random.randint(0,6) == 1:    #increases plant pop sometimes
        plants = plants+1250
        print()
        print('----------------------------------------------')
        print('Bloom! (Plant pop increases)')
        
    if random.randint(0,10) == 5:
        prey = prey+100
        print()
        print('----------------------------------------------')
        print('Irruptive growth in prey population!')   #sudden prey growth
        
    if random.randint(0,25) == 10:              #helps manage prey and plant pop
        prey = prey-300
        plants = plants-1000
        predator = predator+5
        print()
        print('----------------------------------------------')
        print('A drought has massacred the prey population, predators feast on their corpses as plants wilt away!')
        
    if random.randint(0,1250) == 500:    #ecosystem killer
        plants = plants-7500
        prey = prey-650
        predator = predator-27.5
        print()
        print('----------------------------------------------')
        print('Ultra Large Meteorite! Plant and animal populations are devastated!')
        
    if random.randint(0,1000) == 250:   #uh oh
        plants = plants-5000
        prey = prey-400
        predator = predator-15.75
        radiation = 1
        print()
        print('----------------------------------------------')
        print('An untouched, abandoned nuclear device has suddenly detonated! Radiation has contaminated the land!')
        
    if random.randint(0,25) == 8:        #plant control
        plants = plants-4000
        prey = prey-50
        predator = predator-1
        print()
        print('----------------------------------------------')
        print('A forest fire has devastated plant life in the area, and to an extent animal life aswell.')
        
    if ccmoderate == 1 or cchigh == 1 or cckillme == 1:       #climate consequence
        if random.randint(0,10) == 3:
            plants = plants-2500
            prey = prey-100
            predator = predator-3
            print()
            print('----------------------------------------------')
            print('Acid rain, corrosive and hurts! (alot)')
            
            
    if predator>=100 and random.randint(0,7) == 3:                   #predator control
        predator = predator-50
        print()
        print('----------------------------------------------')
        print('There is too much competition for food! Predator populations drop...')
        
    if random.randint(0,45) == 20:        #natural disaster, make affected by climate change later
        print()
        print('----------------------------------------------')
        print("There's a natural disaster! All populations are affected!")       
        predator = predator - 10
        plants = plants - 2500
        prey = prey - 200
        
        
        
    if random.randint(0,10) == 5:                            #predator increases population
        print()
        print('----------------------------------------------')
        print('What a bountiful hunt for the predators!')
        predator = predator + 2.5
        prey = prey - 100
        
        
    if random.randint(0,20) == 10:                            #invasive species
        print()
        print('----------------------------------------------')
        print('An invasive species has entered the ecosystem!')
        prey-750
        plants-1500
        
    if random.randint(0,50) == 25:                             #gotta put radiation in someway without it being ultra rare and for nothing...
        print()
        print('----------------------------------------------')
        print('An ancient nuclear plant has suddenly started leaking... Radiation spreads!')
        radiation = 1
        
        
    if random.randint(0,15) == 5:                              #scav boost
        print()
        print('----------------------------------------------')
        print('Scavenger populations have been very lucky with their finds... (Scav pop increases.)')
        scavenger = scavenger + 50
        
        
        
        
        
        
    
    print()
    print('----------------------------------------------')
    print(f"Plants: {plants:.2f}, Prey: {prey:.2f}, Scavengers: {scavenger:.2f}, Predators: {predator:.2f}")  #stat display, rounds to 2 decimal points
    print()
    
    
    weather = random.randint(0,5)   #weather
    
    stormy = 0
    clear = 0
    sunny = 0
    cloudy = 0
    raining = 0
    windy = 0
    
    if weather == 0:                    #scuffed but works, no need for rework
        print('The weather is stormy!')
        stormy = 1
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 1:
        print('The weather is clear!')
        stormy = 0
        clear = 1
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 2:
        print('It is sunny!')
        stormy = 0
        clear = 0
        sunny = 1
        cloudy = 0
        raining = 0
        windy = 0
    if weather == 3:
        print('It is cloudy!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 1
        raining = 0
        windy = 0
    if weather == 4:
        print('It is raining!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 1
        windy = 0
    if weather == 5:
        print('It is windy!')
        stormy = 0
        clear = 0
        sunny = 0
        cloudy = 0
        raining = 0
        windy = 1
      
      
    if stormy == 1:                   #weather effects
        plants -= plants * 0.002
        prey -= prey * 0.001
        predator -= 0.1
        
    if clear == 1:
        plants += plants * 0.001
        prey += prey * 0.0025
        
    if sunny == 1:
        plants += plants * 0.002
        prey += prey * 0.004
    
    if cloudy == 1:
        plants -= plants * 0.001
        
    if raining == 1:
        plants += plants * 0.003
        
    if windy == 1:
        plants -= plants * 0.001
        
    
    #radiation system
    
    
    if radiation >= 1:
        radiation = radiation + 1
        print('Radiation plagues the land!')
    if radiation == 36:
        print('Most of the radiation has dissipated...')
        radiation = 0
        
    if radiation >= 1 and radiation <=12:          #rad effects
        plants -= plants * 0.075
    if radiation >=13 and radiation <=24:
        plants -= plants * 0.05
    if radiation >=25 and radiation <=30:
        plants -= plants * 0.005
    if radiation >= 31 and radiation <= 35:
        plants -= plants * 0.0025
        
        
        
        
        
        
        
        
    
    if plants<1:                               #game ending
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif predator<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif prey<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    elif scavenger<1:
        print('Ecosystem Collapse!')
        time.sleep(0.75)
        print(f"The ecosystem has survived: {years_survived} years!")
        time.sleep(5)
        exit()
    
    
    
    season +=1                            #Seasons
    
    if season>=1 and season<=3:
        print('Summer!')
    elif season>=4 and season <=6:
        print('Autumn!')
    elif season>=7 and season <=9:
        print('Winter!')
    elif season>=10 and season <=12:
        print('Spring!')
        
    if season == 13:                                          #year counter
        print('The ecosystem has survived a full year!')
        season = 1
        years_survived +=1
        print('Summer!')
        
    print('Month',season)
    time.sleep(3)
    
    
    
    