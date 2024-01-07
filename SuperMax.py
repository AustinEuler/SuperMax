'''
github enabled!!!
This project simulates the card reader security on campus. The object of this application is to showcase how a 
CAU affiliate (student, faculty,staff) can access CAU's Athletic facilities based on their credentials.


Each type of credential has different privileges. If a credential does has access to a certain area,
then that access is further detailed by a specified time slot they can access the facility in question.
Credentials are as follows:

Athlete
General
Athletic Staff
Custodial


Facilities:
Stadium (Open between 4:00 am and 12:00 am. Custodial allowed 24h)
- Football Locker Room (Access - Open during stadium hours; "Student Athletes,Custodial,Athletic Staff")
- Weight Room (Open between 6:00 am and 5 pm; Access - "Student Athletes, Custodial (24h), Athletic Staff)
- Football Coaches' Offices (Open between 6 am and stadium close; Access - "Student Athletes, Custodial, Athletic Staff")
- Multipurpose Room ("Access - "Open during stadium hours"
- Front Parking Entrance
- Middle Tunnel
- Back Parking Entrance



    Facility Access is based on 4 facts:
    1. Must be affiliated with the school (has school ID)
    2. Affiliation type
    3. Time of day access based on affiliation 
    4. Internal entry points are more exclusive with access (based of specified times + affiliation type)

    For example,
    A person has a "General" affiliation with the University. The Stadium can be externally accessed with "General" affiliation
    during "general business hours", which is from 8:00 am to 5:00 pm. The person then tries to access the FB Locker Room, 
    but is unable to because it can only be accessed by FB players, Custodians, and Athletic Staff.
    '''

import time
import os
import random
import re


def clearScreen():
    name = os.name
    if name == "nt":
        os.system('cls')
    else:
        os.system('clear')

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

class Person:

    adminCreated = False
    people = [] #tracks all person objects created
    affiliationType = {'Athlete': ['Athlete','FB','MBB','BB','CC','WBB','SB','T','TF','VB'],'General':'General', 'AthleticStaff': 'AthleticStaff', 'Custodial': 'Custodial'}

    
    def __init__(self):
        
        if MainMenu.adminMode == False:
            clearScreen()
            print("---------------------------------------")
            print("     Welcome to Character Creation     ")
            print("---------------------------------------")

            #initializes the creation of a new person object, starting with the name
            validName = False
            if len(Person.people) > 0:
                names = []
                for character in Person.people:
                    names.append(character.fullName)
                while validName == False:
                    self.firstName = input("Enter first name: ")
                    self.lastName = input("Enter last name: ")
                    self.fullName = self.firstName + " " + self.lastName
                    if (self.fullName in names) == 0: #only makes name valid if it is not already present in the character database
                        validName = True
                    else:
                        print('ERROR - Name already present in character database. Please choose another.')
                        time.sleep(1)
                        clearScreen()
            else:
                if Person.adminCreated == False:
                    self.firstName = input("Enter first name: ")
                    self.lastName = input("Enter last name: ")
                    self.fullName = self.firstName + " " + self.lastName


            #set as list to reflect affiliations with multiple sub-affiliations, such as Athlete->Football
            self.affiliation = []

            self.defineAffiliation()
        else:
            #executes under the assuption that admin mode is turned on.
            #creates the admin character
            #if Person.adminCreated == False:
            self.firstName = 'Admin'
            self.lastName = ''
            self.fullName = self.firstName
            self.affiliation = ['Athlete','FB']
            self.id = "9001112222"
            Person.adminCreated = True
            




    #displays all available affiliations for the person object
    def displayAffiliationTypes(self):
        names = Person.affiliationType.keys()
        
        print("Available Affiliation Types:\n ")
        for name in names:
            if name == 'Athlete':
                print(f"{Person.affiliationType[name][0]}")
            else:
                print(Person.affiliationType[name])

    #sets the affiliation of the person object, then issues a school identification card (Pawcard)
    def defineAffiliation(self):
        clearScreen()
        self.displayAffiliationTypes()
        print("-----------------------")
        choice = input("Choose your affiliation [case sensitive]: ")
        names = Person.affiliationType.keys()
        if choice in names:
            if choice == 'Athlete':
                clearScreen()
                print("Sports Available:")
                print("---------------------")
                for sport in Person.affiliationType[choice]:
                    if sport == "Athlete":
                        pass #skips over the first element, which is 'Athlete'
                    else:
                        print(sport)
                print("---------------------")
                choice2 = input("Enter a sport from the list: ")
                if choice2 in Person.affiliationType[choice]:
                    index = Person.affiliationType[choice].index(choice2)
                    self.affiliation.append(Person.affiliationType[choice][0])
                    self.affiliation.append(Person.affiliationType[choice][index])
                    #issue pawcard here
                    self.issuePawcard()
                    self.describePerson()
                else:
                    print(f"Error - {choice2} is not a valid sport from the list provided. Restarting affiliation selection .... ")
                    time.sleep(1)
                    self.defineAffiliation()

            else:
                self.affiliation.append(choice)
                self.issuePawcard()
                self.describePerson()
        else:
            print("Error - please input a valid affiliation type [case sensitive].")
            time.sleep(1)
            self.defineAffiliation()

            
    #describes the person object with full name and affiliation
    def describePerson(self):
        if len(self.affiliation) == 1:
            print(f"Name: {self.fullName}\nAffiliation: {self.affiliation}")

        elif len(self.affiliation) > 1:
            count = 0
            print(f"Name: {self.fullName}\nAffiliation:")
            while count != len(self.affiliation):
                if count == 0:
                    print(f"{self.affiliation[count]}", end= " ")
                else:
                    print(f"-> {self.affiliation[count]}", end="\n")
                count += 1
        print(f"School ID: {self.id}\n")
    
    #issues the person object a pawcard with a unique 900 number
    def issuePawcard(self):

        #makes sure the id number issued is unique
        valid = False
        while valid == False:
            if len(Person.people) > 0:
                names = []
                for character in Person.people:
                    names.append(character.fullName)
 
                end = ""
                for number in range(7):
                    end = end + str(random.randint(0,9))

                self.id = "900" + end
                valid = True

            else:
                end = ""
                for number in range(7):
                    end = end + str(random.randint(0,9))

                self.id = "900" + end
                valid = True


            



    def getID(self):
        print(f"School ID Number: {self.id}")


    #person object attempts to use facility
    #compares affiliation and current simulated time to 
    def swipeCard():
        pass

    
    #lists all character profiles created
    def listPeople():
        clearScreen()
        count = 1
        if len(Person.people) > 0:
            for profile in Person.people:
                print(f"{count}.")
                print("------------------------",end="\n")
                profile.describePerson()
                print()
                print("------------------------",end="\n")
                count += 1
        else:
            print("There are currently no character profiles created!")


    #deletes a character profile from the class list
    def deleteCharacter(self):
        if len(Person.people) > 0:
            names = []
            for character in Person.people:
                names.append(character.id)
            Person.listPeople()
            choice = input("Enter the ID of the character profile you want to delete: ")
            if choice in names:
                for character in Person.people:
                    if choice == character.id:
                        Person.people.remove(character)
                        print(f"{character.fullName}'s profile has been deleted!")
                        #resets admin tracker if deleted
                        if choice == '900111222':
                            Person.adminCreated = False
                            print( "ALERT- this was the admin character profile.")

            else:
                print(f"Error - {choice} is not a valid name! Please enter a full name from the provided list of available characters.")
                time.sleep(1)
                self.deleteCharacter()
        else:
            print("There are currently no character profiles available to delete!")

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

class Campus:

    entered = False #monitors if a Facility has been entered through a scenario

    #universal timeslots templates
    timeslots = {"EarlyBusinessHours":[4,5,6,7,8,9,10,11,12,13,14,15,16,17],
                "BusinessHours":[6,7,8,9,10,11,12,13,14,15,16,17],
                "GeneralBusinessHours":[8,9,10,11,12,13,14,15,16,17],
                "ExtendedBusinessHours":[0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                "FullAccess": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
                "NoAccess": ["NA"]
                }
    

    #acts as security access rules for all facilities and their entry points
    accessTimes = {'Stadium': {"Athlete":
                                    {'FB': {"FBLockerRoom":timeslots["ExtendedBusinessHours"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'MBB':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'BB':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                        "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'CC':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'WBB':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'SB':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'T':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'TF':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']},
                                    'VB':{"FBLockerRoom":timeslots["NoAccess"],
                                            "WeightRoom":timeslots["BusinessHours"],
                                            "FBOffices":timeslots["BusinessHours"],
                                            "MultipurposeRoom":timeslots["BusinessHours"],
                                            "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                            "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                            "BackParkingEntrance":timeslots['ExtendedBusinessHours']}},
                                "General":{
                                    "FBLockerRoom":timeslots["NoAccess"],
                                    "WeightRoom":timeslots["NoAccess"],
                                    "FBOffices":timeslots["NoAccess"],
                                    "MultipurposeRoom":timeslots["NoAccess"],
                                    "FrontParkingEntrance":timeslots['GeneralBusinessHours'],
                                    "MiddleTunnel": timeslots['NoAccess'],
                                    "BackParkingEntrance":timeslots['NoAccess']

                                    
                                },
                                "Custodial":{
                                    "FBLockerRoom":timeslots["ExtendedBusinessHours"],
                                    "WeightRoom":timeslots["ExtendedBusinessHours"],
                                    "FBOffices":timeslots["ExtendedBusinessHours"],
                                    "MultipurposeRoom":timeslots["ExtendedBusinessHours"],
                                    "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                    "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                    "BackParkingEntrance":timeslots['ExtendedBusinessHours']
                                },
                                "AthleticStaff":{
                                    "FBLockerRoom":timeslots["ExtendedBusinessHours"],
                                    "WeightRoom":timeslots["ExtendedBusinessHours"],
                                    "FBOffices":timeslots["ExtendedBusinessHours"],
                                    "MultipurposeRoom":timeslots["ExtendedBusinessHours"],
                                    "FrontParkingEntrance":timeslots['ExtendedBusinessHours'],
                                    "MiddleTunnel": timeslots['ExtendedBusinessHours'],
                                    "BackParkingEntrance":timeslots['ExtendedBusinessHours']

                                }
 
                                        }}
    
    
    


    #central dictionary housing access information for all facility locations
    #this will be a dictionary which houses the different locations, their security status, and exterior and interior access points

    workingLocations = {"Stadium":[{"status":"off",
                                    "exteriorAccess":
                                    [
                                        "FrontParkingEntrance",
                                        "MiddleTunnel",
                                        "BackParkingEntrance"
                                    ],
                                    "interiorAccess":
                                    [
                                        "FBLockerRoom",
                                        "WeightRoom",
                                        "FBOffices",
                                        "MultipurposeRoom",   
                                    ],
                                    "accessTimes":accessTimes
                                    }]
                        }

    #displays the security status for all facility locations
    def checkStatus(self):
        clearScreen()
        print("Security status for all facilities:")
        names = Campus.workingLocations.keys()
        for facility in names:
            print(f"{facility}: {Campus.workingLocations[facility][0]['status']}")

    
    #Activates the security system for the selected facility
    def constructCampus(self):
        clearScreen()  
        #print(self.name)

        notActivated = []
        keys = Campus.workingLocations.keys()
        for facility in keys:
            if(Campus.workingLocations[facility][0]['status'] == 'off'):
                notActivated.append(facility)

        if MainMenu.adminMode == False:
            if len(notActivated) > 0:
                #Show list of available facilities to initialize
                print("Available Facilities:")
                for name in notActivated:
                    print(name)
                print()

                self.name = input("Enter a Facility name to initialize, or 'all' to initialize every location: ")

                #Constructs the virtual campus with the chosen facility, or request for the user to enter a valid facility name
                if self.name in Campus.workingLocations:
                    print(f"Initializing security framework for {self.name} ....")
                    Campus.workingLocations[self.name][0]["status"] = "on"
                    print(f"{self.name} security framework is online! ")
                elif self.name == "all":
                    print(f"Initializing security framework for all locations ....")
                    for facility in keys:
                        if(Campus.workingLocations[facility][0]['status'] == 'off'):
                            Campus.workingLocations[facility][0]['status'] = 'on'
                            print(f"{facility} security framework is online! ")

                else:
                    print(f"Sorry, configurations for '{self.name}' are unavaliable at this time. Please choose from one of the available facilities. ")
                    time.sleep(1)
                    Campus.constructCampus(self)
            else:
                print("All facility locations already activated!")
        else:
            if len(notActivated) > 0:
                for facility in keys:
                    if(Campus.workingLocations[facility][0]['status'] == 'off'):
                        Campus.workingLocations[facility][0]['status'] = 'on'
                        print(f"{facility} security framework is online! ")

            else:
                print("All facility locations already activated!")

    #turns off security settings for a facility location, making it unable to take part in scenarios
    def decommission(self):
        clearScreen()
        activated = [] #list of all activated locations
        names = Campus.workingLocations.keys()
        for facility in names:
            if(Campus.workingLocations[facility][0]['status'] == 'on'):
                activated.append(facility)
        
        if len(activated) > 0:
            print("Facilities with Activated Security: ")
            for facility in activated:
                print(facility)
            
            choice = input("Enter a location to decommission: ")
            if choice in activated:
                print(f"Decommissioning security framework for {choice} ....")
                Campus.workingLocations[choice][0]["status"] = "off"
                print(f"{choice} security framework is now offline! ")
            else:
                print(f"Sorry, configurations for '{choice}' are unavaliable at this time. Please choose from one of the available facilities. ")
                time.sleep(1)
                Campus.decommission(self)
        else:
            print("There are no activated locations at this time!")

##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

#create menu that allows you start similations or go through system settings (character and facility settings)
class MainMenu:
    adminMode = False
    menuTracker = None #notes what menu is currently being displayed
    processStarted = False #notes if a process has been started from the menu, and allows the user to go back after process completion

    #initially adds the admin profile unless it is already created. 
    #sets up all facilities and sets admin profile to chosen character for Scenarios
    def enableAdminMode(self):
        MainMenu.adminMode = True
        
        '''
        if len(Person.people) > 0:
            names = []
            for character in Person.people:
                names.append(character.fullName)
            if 'Admin ' in names:
                pass
            else:
                admin = Person()
                Person.people.append(admin)
        '''

        if Person.adminCreated == True:
            pass
        else:
            admin = Person()
            Person.people.append(admin)
        
        Campus.constructCampus(self)

        for character in Person.people:
            if character.fullName == 'Admin':
                Scenarios.chosenCharacter = character
        #Scenarios.chosenCharacter =  #sets admin profile for scenarios

        print("Admin mode enabled.")
        time.sleep(1)
        self.displayMenu()
 
    def disableAdminMode(self):
        clearScreen()
        MainMenu.adminMode = False
        print("Admin mode disabled.")
        time.sleep(1)
        self.displayMenu()

        

    def makeChoice(self):
        if MainMenu.processStarted == False:
            if MainMenu.menuTracker == 0:
                choice = input("Enter a choice from the menu numbers: ")
                if choice == "1":
                    print("Starting Security Scenario with Project SuperMax....")
                    time.sleep(1)
                    Scenarios.start(self)
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "2":
                    self.settingsMenu()
                elif choice == "3":
                    if MainMenu.adminMode == False:
                        MainMenu.enableAdminMode(self)
    
                    else:
                        MainMenu.disableAdminMode(self)

                else:
                    print("Error - Please enter one of the available number choices!")
                    time.sleep(1)
                    self.displayMenu()
            elif MainMenu.menuTracker == 1:
                choice = input("Enter a choice from the menu numbers: ")
                if choice == "1":
                    self.facilityMenu()
                elif choice == "2":
                    self.characterMenu()
                elif choice == "3":
                    self.displayMenu()
                else:
                    print("Error - Please enter one of the available number choices!")
                    time.sleep(1)
                    self.settingsMenu()
                
            elif MainMenu.menuTracker == 2:
                choice = input("Enter a choice from the menu numbers: ")
                if choice == "1":
                    Campus.checkStatus(self)
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "2":
                    Campus.constructCampus(self)
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "3":
                    Campus.decommission(self)
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "4":
                    self.settingsMenu()
                else:
                    print("Error - Please enter one of the available number choices!")
                    time.sleep(1)
                    self.facilityMenu()
            
            elif MainMenu.menuTracker == 3:
                choice = input("Enter a choice from the menu numbers: ")
                if choice == "1":
                    Person.listPeople()
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "2":
                    if MainMenu.adminMode == False:
                        character = Person()
                        Person.people.append(character) #adds new character to 'people' list in 'Person' class
                        print(f"New character added: {character.fullName}")
                        MainMenu.processStarted = True
                    else:
                        print("Unable to create new character profiles while in admin mode.")
                    self.makeChoice()
                elif choice == "3":
                    Person.deleteCharacter(self) #deletes a character's profile
                    MainMenu.processStarted = True
                    self.makeChoice()
                elif choice == "4":
                    self.settingsMenu()
                else:
                    print("Error - Please enter one of the available number choices!")
                    time.sleep(1)
                    self.characterMenu()



            else:
                print("Error - Please enter one of the available number choices!")
                time.sleep(1)
                self.displayMenu()
        
        else:
            print()
            choice = input("Enter 'exit' to go back to menu: ")
            if choice == "exit":
                if MainMenu.menuTracker == 0:
                    MainMenu.processStarted = False
                    self.displayMenu()
                elif MainMenu.menuTracker == 1:
                    MainMenu.processStarted = False
                    self.settingsMenu()
                elif MainMenu.menuTracker == 2:
                    MainMenu.processStarted = False
                    self.facilityMenu()
                elif MainMenu.menuTracker == 3:
                    MainMenu.processStarted = False
                    self.characterMenu()
                else:
                    MainMenu.processStarted = False
                    self.displayMenu()
            else:
                print("Error - Please enter 'exit' if you want to return to the menu. ")
                self.makeChoice()

    #initial menu on startup
    def displayMenu(self):
        MainMenu.menuTracker = 0
        clearScreen()
        if MainMenu.adminMode == False:
            print("-------------------------------------------")
            print("        Welcome to Project SuperMax               ")              
            print("-------------------------------------------")
            print("1 - Start Scenario \n2 - System Settings \n3 - Enable Admin Mode ")
            print("-------------------------------------------")
        else:
            print("-------------------------------------------")
            print("        Welcome to Project SuperMax               ")              
            print("-------------------------------------------")
            print("1 - Start Scenario \n2 - System Settings \n3 - Disable Admin Mode")
            print("-------------------------------------------")

        self.makeChoice()

    #menu for general settings
    def settingsMenu(self):
        MainMenu.menuTracker = 1
        clearScreen()
        print("-------------------------------------------")
        print("             System Settings             ")              
        print("-------------------------------------------")
        print("1 - Facility Information \n2 - Character Information \n3 - Back" )
        print("-------------------------------------------")

        self.makeChoice()

    #menu for facility settings
    def facilityMenu(self):
        MainMenu.menuTracker = 2
        clearScreen()
        print("-------------------------------------------")
        print("             Facility Information           ")              
        print("-------------------------------------------")
        print("1 - Check Facility Status \n2 - Initialize a Location \n3 - Decommission a Location \n4 - Back" )
        print("-------------------------------------------")

        self.makeChoice()


    #menu for character settings
    def characterMenu(self):
        MainMenu.menuTracker = 3
        clearScreen()
        print("-------------------------------------------")
        print("         Character Settings         ")              
        print("-------------------------------------------")
        print("1 - Check Character Info \n2 - Create New Character \n3 - Delete Character \n4 - Back" )
        print("-------------------------------------------")

        self.makeChoice()


##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

# 5-step process that creates a Scenario, using random 
class Scenarios:

    inProgress = False
    reRun = False
    chosenCharacter = None
    chosenFacility = None
    currentTime = None
    tempTime = None
    prompt = None
    accessPointsUsed = None
    results = []
    denied = []
    granted = []
    total = None
    conclusion = None

    '''
    hoursLegend = {
        "legend":
        0 - midnight
            1 [1,"am"]
            2 [2, "am"]
            3 - 3 am
            4 - 4 am
            5 - 5 am
            6 - 6 am
            7 - 7 am
            8 - 8 am
            9 - 9 am
            10 - 10 am
            11 - 11 am
            12 - 12 pm
            13 - 1 pm
            14 - 2 pm
            15 - 3 pm
            16 - 4 pm
            17 - 5 pm
            18 - 6 pm
            19 - 7 pm
            20 - 8 pm
            21 - 9 pm
            22 - 10 pm
            23 - 11 pm
    }
    '''

    def start(self):
        print("----------------------------------------------------------------")
        if Scenarios.inProgress == True:
            valid = False
            while valid == False:
                choice = input("Do you want to run another scenario? Enter 'yes' or 'no': ")
                if choice == 'yes':
                    valid = True 
                    Scenarios.reRun = True
                    clearScreen()
                elif choice == 'no':
                    valid = True
                    Scenarios.reRun = False
                    Scenarios.inProgress = False
                    clearScreen()
                else:
                    print("Error - Please enter 'yes' or 'no'! ")
            
            if Scenarios.reRun == True:
                valid2 = False
                while valid2 == False:
                    choice2 = input("Do you want to keep the same character? Enter 'yes' or 'no': ")
                    if choice2 == 'yes':
                        valid2 = True 
                        Scenarios.chooseTOD(self) #continues the scenario setup while skipping character selection
                    elif choice2 == 'no':
                        valid2 = True
                        Scenarios.chooseCharacter(self)    
                    else:
                        print("Error - Please enter 'yes' or 'no'! ")
                    

                    



        else:
            Scenarios.chooseCharacter(self)
            

    def chooseCharacter(self):
        Scenarios.inProgress = True
        if MainMenu.adminMode == False:
            if len(Person.people) > 0:
                names = []
                for character in Person.people:
                    names.append(character.id)
                Person.listPeople()
                choice = input("Enter the ID of the character you want to use: ")

                #sets the selected character profile object to "chosenCharacter" variable
                if choice in names:
                    for character in Person.people:
                        if choice == character.id:
                            Scenarios.chosenCharacter = character
                    print(f"Character loaded in: {Scenarios.chosenCharacter.fullName}")
                else:
                    print(f"Error - {choice} is not a valid ID! Please enter a ID from the provided list of available characters.")
                    time.sleep(1)
                    Scenarios.chooseCharacter(self)
            else:
                print("Error - There are currently no characters available to load.\nPlease create a new character profile or enter admin mode.")
        else:
            print(f"Character loaded in: {Scenarios.chosenCharacter.fullName}")
        
        Scenarios.chooseTOD(self)

    
    #start of a scenario
    
    #converts army time to a usable am/pm time
    def hourConverter(TOD):
        if (TOD > 0) and (TOD < 12):
            describer = "am"
        elif TOD > 11:
            describer = "pm"
        elif TOD == 0:
            describer = "midnight"
        else:
            describer = "ERROR"
        return describer


    def chooseTOD(self):

        #time of day
        TOD = random.randint(0,23)

        describer = Scenarios.hourConverter(TOD)



        if TOD == 0:
            Scenarios.tempTime = [12,describer]
        elif TOD > 12:
            Scenarios.tempTime = [(TOD - 12),describer]
        else:
            Scenarios.tempTime = [TOD,describer]


        Scenarios.currentTime = [TOD,describer] #set current time
        print("Time of day set ....")
        Scenarios.chooseFacility(self)

    
    def chooseFacility(self):

        activated = [] #list of all activated locations
        names = Campus.workingLocations.keys()
        for facility in names:
            if(Campus.workingLocations[facility][0]['status'] == 'on'):
                activated.append(facility)
        
        if len(activated) > 0:
            Scenarios.chosenFacility = random.choice(activated)
            print("Facility set ....")

            #randomly chooses what entry points will be used
            exterior = random.choice(Campus.workingLocations[Scenarios.chosenFacility][0]["exteriorAccess"])
            interior = random.choice(Campus.workingLocations[Scenarios.chosenFacility][0]["interiorAccess"])
            Scenarios.accessPointsUsed = [exterior,interior]
            Scenarios.total = len(Scenarios.accessPointsUsed)
            Scenarios.createPrompt(self)
            

        else:
            print("Scenario Terminated - There are no activated locations at this time! \n \
                  Please activate a facility through 'Facility Settings' to continue. ")

 


        
    def createPrompt(self):

        string = f"It is {Scenarios.tempTime[0]} {Scenarios.tempTime[1]} at Clark Atlanta University, and {Scenarios.chosenCharacter.fullName}" \
                f" attempts to access the {Scenarios.chosenFacility} through the {Scenarios.accessPointsUsed[0]}, then go to the {Scenarios.accessPointsUsed[1]} ...."

        Scenarios.prompt = string
        print("Prompt created ....")
        Scenarios.displayPrompt(self)

    #displays the prompt and a legend for the facility hours
    def displayPrompt(self):
        time.sleep(1)
        clearScreen()
        Scenarios.displayFacilityHours(self)
        print()
        print("----------------------------------------------------------------")
        print("                             Prompt                             ")
        print("----------------------------------------------------------------")
        print()
        print(Scenarios.prompt)
        Scenarios.calculateResults(self)


    #prints the hours for each affiliation
    def displayFacilityHours(self):
        tempAffiliations = Campus.accessTimes['Stadium'].keys()
        tempAccessPoints = Campus.accessTimes['Stadium']['General'].keys()
        tempAthleteNames = Campus.accessTimes['Stadium']['Athlete'].keys()
        accessPoints = []
        affiliations = []
        athleteNames = []
        #converts the view objects to a usable list
        for name in tempAccessPoints:
            accessPoints.append(name)
        for name in tempAffiliations:
            affiliations.append(name)
        for name in tempAthleteNames:
            athleteNames.append(name)

        '''
        describer = Scenarios.hourConverter(TOD)

        if TOD == 0:
            Scenarios.tempTime = [12,describer]
        elif TOD > 12:
            Scenarios.tempTime = [(TOD - 12),describer]
        else:
            Scenarios.tempTime = [TOD,describer]
        '''



        print("----------------------------------------------------------------")
        print("                         Facility Hours                         ")
        print("----------------------------------------------------------------")

        print(f" Facility Name: {Scenarios.chosenFacility}")
        print()
        for af in accessPoints:
            print("------------------")
            print(f"Access Point: {af} ")
            print()
            for ap in affiliations:
                if ap == "Athlete":
                    print(f"{ap}: Varied Facility and Sport-Specific Access" )
                    '''
                    for sport in athleteNames:
                        print(f"{sport}: {Campus.accessTimes['Stadium'][ap][sport][af]}")
                    '''
                else:
                    if Campus.accessTimes['Stadium'][ap][af][0] != 'NA':
                        start = Campus.accessTimes['Stadium'][ap][af][0]
                        end = Campus.accessTimes['Stadium'][ap][af][-1]
                        combo = [start,end]

                        timeframe = []
                        #there is too much going on here, but it works. Streamline Later
                        for num in combo:
                            describer = Scenarios.hourConverter(num)

                            if num == 0:
                                string = f"{str(12)} {describer}"
                                timeframe.append(string)
                            elif num > 12:
                                string = f"{str(num - 12)} {describer}"
                                timeframe.append(string)
                            else:
                                string = f"{str(num)} {describer}"
                                timeframe.append(string)
                        print(f"{ap}: {timeframe[0]} - {timeframe[1]}")
                    else:
                        print(f"{ap}: No Access")
                    

                    #print(f"{ap}: {Campus.accessTimes['Stadium'][ap][af]}")
            
        #print(Campus.accessTimes[Scenarios.chosenFacility])



    def calculateResults(self):
        affiliation = Scenarios.chosenCharacter.affiliation
        facility = Scenarios.chosenFacility
        currentTime = Scenarios.currentTime[0]
        aborted = False #triggers if unable to access the facility's outer entrances
        count = 1
        if affiliation[0] == "Athlete":
            for entryPoint in Scenarios.accessPointsUsed:
                if aborted != True: #checks for outer entrance access
                    outcome = None
                    if currentTime in Campus.workingLocations[facility][0]["accessTimes"][facility][affiliation[0]][affiliation[1]][entryPoint]:
                        outcome = "Access Granted"
                        Scenarios.granted.append(entryPoint)
                    else:
                        outcome = "Access Denied"
                        Scenarios.denied.append(entryPoint)
                        aborted = True
                else:
                    outcome = "Access Denied"
                    Scenarios.denied.append(entryPoint)

                Scenarios.results.append(outcome)
        else:
            for entryPoint in Scenarios.accessPointsUsed:
                if aborted != True: #checks for outer entrance access
                    outcome = None
                    if currentTime in Campus.workingLocations[facility][0]["accessTimes"][facility][affiliation[0]][entryPoint]:
                        outcome = "Access Granted"
                        Scenarios.granted.append(entryPoint)
                    else:
                        outcome = "Access Denied"
                        Scenarios.denied.append(entryPoint)
                        aborted = True
                else:
                    outcome = "Access Denied"
                    Scenarios.denied.append(entryPoint)

                Scenarios.results.append(outcome)
        

        if len(Scenarios.granted) == Scenarios.total:
            Scenarios.conclusion = f"{Scenarios.chosenCharacter.fullName} was granted access all to attempted entry points. "
        elif len(Scenarios.denied) == Scenarios.total:
            Scenarios.conclusion = f"{Scenarios.chosenCharacter.fullName} was denied access to the facility. "
        else:
            Scenarios.conclusion = f"{Scenarios.chosenCharacter.fullName} was granted access to the facility through {Scenarios.accessPointsUsed[0]} entrance. "\
                                    f"However, they were denied access to {Scenarios.accessPointsUsed[1]}."
                                    

        Scenarios.displayResults(self)

        
        




    def displayResults(self):
        print()
        print("----------------------------------------------------------------")
        print("                            Outcome                             ")
        print("----------------------------------------------------------------")
        print(f"Name: {Scenarios.chosenCharacter.fullName}")
        print(f"ID: {Scenarios.chosenCharacter.id}")
        print(f"Character Credentials: {Scenarios.chosenCharacter.affiliation}")
        print()
        counter = 0
        if (Scenarios.chosenCharacter.affiliation[0] == "General"):
            print(f"DISCLAIMER - All 'general' affiliations must enter through the Front Parking Entrance!")
        for result in Scenarios.results:
            print(f"{Scenarios.accessPointsUsed[counter]}: {result}")
            counter += 1

        print()
        print(Scenarios.conclusion)

        #clears the results to get ready for the next scenario
        Scenarios.results.clear() 
        Scenarios.granted.clear()
        Scenarios.denied.clear()

        Scenarios.start(self)


##########################################################################################################################################################
##########################################################################################################################################################
##########################################################################################################################################################

def main():
    menu = MainMenu()
    menu.displayMenu()

    #person = Person("Austin","Euler")
    

main()
