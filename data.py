import random


def anthroskillreplacement():
    skills.update(anthropologistSkills)
    skills.update(random.sample(list(anthropologistOptionalSkills.items()), 2))
    # 4bonds


def historianskillreplacement():
    skills.update(historianSkills)
    skills.update(random.sample(list(historianOptionalSkills.items()), 2))
    # 4bonds


def compsciskillreplacement():
    skills.update(computerScientistSkills)
    skills.update(random.sample(list(computerScientistOptionalSkills.items()), 4))
    # 3bonds


def fagentskillreplacement():
    skills.update(federalAgentSkills)
    skills.update(random.sample(list(federalAgentOptionalSkills.items()), 1))
    # 3bonds


def physicianskillreplacement():
    skills.update(physicianSkills)
    skills.update(random.sample(list(physicianOptionalSkills.items()), 2))
    # 3bonds


def scientistskillreplacement():
    skills.update(scientistSkills)
    skills.update(random.sample(list(scientistOptionalSkills.items()), 3))
    # 4bonds


def specopskillreplacement():
    skills.update(specOpSkills)
    # 2bonds


def criminalskillreplacement():
    skills.update(criminalSkills)
    skills.update(random.sample(list(criminalOptionalSkills.items()), 2))
    # 4bonds


def firefighterskillreplacement():
    skills.update(firefighterSkills)
    # 3bonds


def fsoskillreplacement():
    skills.update(fsoSkills)
    # 3bonds


def ianalystskillreplacement():
    skills.update(iAnalystSkills)
    # 3bonds


def icoskillreplacement():
    skills.update(icoSkills)
    # 2bonds


def lawyerskillreplacement():
    skills.update(lawyerSkills)
    skills.update(random.sample(list(lawyerOptionalSkills.items()), 4))
    # 4bonds


def mediaspecialistskillreplacement():
    skills.update(mediaSpecialistSkills)
    skills.update(random.sample(list(mediaSpecialistOptionalSkills.items()), 5))
    # 4bonds


def nurseskillreplacement():
    skills.update(nurseSkills)
    skills.update(random.sample(list(nurseOptionalSkills.items()), 2))
    # 4bonds


def pilotskillreplacement():
    skills.update(pilotSkills)
    skills.update(random.sample(list(pilotOptionalSkills.items()), 2))
    # 3bonds


def policeskillreplacement():
    skills.update(policeSkills)
    skills.update(random.sample(list(policeOptionalSkills.items()), 1))
    # 3bonds


def progmgrskillreplacement():
    skills.update(progMgrSkills)
    skills.update(random.sample(list(progMgrOptionalSkills.items()), 1))
    # 4bonds


def soldierskillreplacement():
    skills.update(soldierSkills)
    skills.update(random.sample(list(soldierOptionalSkills.items()), 3))
    # 4bonds


def marineskillreplacement():
    skills.update(marineSkills)
    skills.update(random.sample(list(marineOptionalSkills.items()), 3))
    # 4bonds


num_sides = 6  # 6-sided die
num_dice = 4  # number of dice to roll
num_smallest = int()  # smallest roll
num_final = int()  # added dice rolls together

stats = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'POW': 0, 'CHA': 0}
factor = []

sex = ['Male', 'Female']

profession = ['Anthropologist', 'Historian', 'Computer Scientist', 'Engineer', 'Federal Agent', 'Physician',
              'Scientist', 'Special Operator', 'Criminal', 'Firefighter', 'Foreign Service Officer',
              'Intelligence Analyst', 'Intelligence Case Officer', 'Lawyer', 'Business Executive', 'Media Specialist',
              'Nurse', 'Paramedic', 'Pilot', 'Sailor', 'Police Officer', 'Program Manager', 'Soldier', 'Marine']

# base stats for skills


skills = {'Accounting': 10, 'Alertness': 20, 'Anthropology': 0, 'Archeology': 0, 'Art (Type)': 0, 'Artillery': 0,
          'Athletics': 30, 'Bureaucracy': 10, 'Computer Science': 0, 'Craft (Type)': 0, 'Criminology': 10,
          'Demolitions': 0, 'Disguise': 10, 'Dodge': 30, 'Drive': 20, 'Firearms': 20, 'First Aid': 10,
          'Forensics': 0, 'Heavy Machinery': 10, 'Heavy Weapons': 0, 'History': 10,
          'HUMINT': 10, 'Law': 0, 'Medicine': 0, 'Melee Weapons': 30, 'Military Science (Type)': 0,
          'Navigate': 10, 'Occult': 10, 'Persuade': 20, 'Pharmacy': 0, 'Pilot (Type)': 0, 'Psychotherapy': 10,
          'Ride': 10, 'Science (Type)': 0, 'Search': 20, 'SIGINT': 0, 'Stealth': 10, 'Surgery': 0,
          'Survival': 10, 'Swim': 20, 'Unarmed Combat': 40, 'Unnatural': 0}

strProfession = [profession[7], profession[8], profession[9], profession[20], profession[22], profession[23]]

dexProfession = [profession[5], profession[8], profession[9], profession[18], profession[19]]

conProfession = [profession[4], profession[7], profession[9], profession[4], profession[20], profession[22],
                 profession[23]]

intProfession = [profession[0], profession[1], profession[2], profession[3], profession[5], profession[6],
                 profession[10], profession[11], profession[12], profession[13], profession[14], profession[15],
                 profession[16], profession[17], profession[18], profession[19], profession[21]]

powProfession = [profession[4], profession[5], profession[7], profession[12], profession[16], profession[17],
                 profession[20]]

chaProfession = [profession[4], profession[10], profession[12], profession[13], profession[14], profession[15],
                 profession[16], profession[17], profession[21]]

professionGenerate = ()

# Updated over base skills after profession generated

anthropologistSkills = {'Anthropology': 50, 'Bureaucracy': 40, 'History': 60, 'Occult': 40, 'Persuade': 40,
                        'Foreign Language (choose first)': 50, 'Foreign Language (choose second)': 40}
anthropologistOptionalSkills = {'Archeology': 40, 'HUMINT': 50, 'Navigate': 50, 'Ride': 50, 'Search': 60,
                                'Survival': 50}

historianSkills = {'Archeology': 50, 'Bureaucracy': 40, 'History': 60, 'Occult': 40, 'Persuade': 40,
                   'Foreign Language (choose first)': 50, 'Foreign Language (choose second)': 40}
historianOptionalSkills = {'Anthropology': 40, 'HUMINT': 50, 'Navigate': 50, 'Ride': 50, 'Search': 60,
                           'Survival': 50}

computerScientistSkills = {'Computer Science': 60, 'Craft (Electrician)': 30, 'Craft (Mechanic)': 30,
                           'Craft (Microelectronics)': 40, 'Science (Mathematics)': 40, 'SIGINT': 40}
computerScientistOptionalSkills = {'Accounting': 50, 'Bureaucracy': 50, 'Craft (choose one)': 40,
                                   'Foreign Language (choose one)': 40, 'Heavy Machinery': 50, 'Law': 40,
                                   'Science (choose one)': 40}

federalAgentSkills = {'Alertness': 50, 'Bureaucracy': 40, 'Criminology': 50, 'Drive': 50, 'Firearms': 50,
                      'Forensics': 30, 'HUMINT': 60, 'Law': 30, 'Persuade': 50, 'Search': 50, 'Unarmed Combat': 60}
federalAgentOptionalSkills = {'Accounting': 60, 'Computer Science': 50, 'Foreign Language (choose one)': 50,
                              'Heavy Weapons': 50, 'Pharmacy': 50}

physicianSkills = {'Bureaucracy': 50, 'First Aid': 60, 'Medicine': 60, 'Persuade': 40, 'Pharmacy': 50,
                   'Science (Biology)': 60, 'Search': 40}
physicianOptionalSkills = {'Forensics': 50, 'Psychotherapy': 60, 'Science (choose one)': 50, 'Surgery': 50}

scientistSkills = {'Bureaucracy': 40, 'Computer Science': 40, 'Science (choose first)': 60,
                   'Science (choose second)': 50, 'Science (choose third)': 50}
scientistOptionalSkills = {'Accounting': 50, 'Craft (choose one)': 40, 'Foreign Language (choose one)': 40,
                           'Forensics': 40, 'Law': 40, 'Pharmacy': 40}

specOpSkills = {'Alertness': 60, 'Athletics': 60, 'Demolitions': 40, 'Firearms': 60, 'Heavy Weapons': 50,
                'Melee Weapons': 50, 'Military Science (Land)': 60, 'Navigate': 50, 'Stealth': 50,
                'Survival': 50, 'Swim': 50, 'Unarmed Combat': 60}

criminalSkills = {'Alertness': 50, 'Criminology': 60, 'Dodge': 40, 'Drive': 50, 'Firearms': 40, 'Law': 40,
                  'Melee Weapons': 40, 'Persuade': 50, 'Stealth': 50, 'Unarmed Combat': 50}
criminalOptionalSkills = {'Craft (Locksmithing)': 40, 'Demolitions': 40, 'Disguise': 50,
                          'Foreign Language (choose one)': 40, 'Forensics': 40, 'HUMINT': 50, 'Navigate': 50,
                          'Occult': 50, 'Pharmacy': 40}

firefighterSkills = {'Alertness': 50, 'Athletics': 60, 'Craft (Electrician)': 40, 'Craft (Mechanic)': 40,
                     'Demolitions': 50, 'Drive': 50, ' First Aid': 50, 'Forensics': 40, 'Heavy Machinery': 50,
                     'Navigate': 50, 'Search': 40}

fsoSkills = {'Accounting': 40, 'Anthropology': 40, 'Bureaucracy': 60, 'Foreign Language (choose first)': 50,
             'Foreign Language (choose second)': 50, 'Foreign Language (choose third)': 40, 'History': 40,
             'HUMINT': 50, 'Law': 40, 'Persuade': 50}

iAnalystSkills = {'Anthropology': 40, 'Bureaucracy': 50, 'Computer Science': 40, 'Criminology': 40,
                  'Foreign Language (choose first)': 50, 'Foreign Language (choose second)': 50,
                  'Foreign Language (choose third)': 40, 'History': 40, 'HUMINT': 50, 'SIGINT': 40}

icoSkills = {'Alertness': 50, 'Bureaucracy': 40, 'Criminology': 50, 'Disguise': 50, 'Drive': 40, 'Firearms': 40,
             'Foreign Language (choose first)': 50, 'Foreign Language (choose second)': 40, 'HUMINT': 60,
             'Persuade': 60, 'SIGINT': 40, 'Stealth': 50, 'Unarmed Combat': 50}

lawyerSkills = {'Accounting': 50, 'Bureaucracy': 50, 'HUMINT': 40, 'Persuade': 60}
lawyerOptionalSkills = {'Computer Science': 50, 'Criminology': 60, 'Foreign Language (choose one)': 50, 'Law': 50,
                        'Pharmacy': 50}

mediaSpecialistSkills = {'Art (choose one)': 60, 'History': 40, 'HUMINT': 40, 'Persuade': 50}
mediaSpecialistOptionalSkills = {'Anthropology': 40, 'Archeology': 40, 'Art (choose second)': 40, 'Bureaucracy': 50,
                                 'Computer Science': 40, 'Criminology': 50, 'Foreign Language (choose one)': 40,
                                 'Law': 40, 'Military Science (choose one)': 40, 'Occult': 50,
                                 'Science (choose one)': 40}

nurseSkills = {'Alertness': 40, 'Bureaucracy': 40, 'First Aid': 60, 'HUMINT': 40, 'Medicine': 40, 'Persuade': 40,
               'Pharmacy': 40, 'Science (Biology)': 40}
nurseOptionalSkills = {'Drive': 60, 'Forensics': 40, 'Navigate': 50, 'Psychotherapy': 50, 'Search': 60}

pilotSkills = {'Alertness': 60, 'Bureaucracy': 30, 'Craft (Electrician)': 40, 'Craft (Mechanic)': 40, 'Navigate': 50,
               'Pilot (choose one)': 60, 'Science (Meteorology)': 40, 'Swim': 40}
pilotOptionalSkills = {'Foreign Language (choose one)': 50, 'Pilot (choose second)': 50, 'Heavy Weapons': 50,
                       'Military Science (choose one)': 50}

policeSkills = {'Alertness': 60, 'Bureaucracy': 40, 'Criminology': 40, 'Drive': 50, 'Firearms': 40, 'First Aid': 30,
                'HUMINT': 50, 'Law': 30, 'Melee Weapons': 50, 'Navigate': 40, 'Persuade': 40, 'Search': 40,
                'Unarmed Combat': 60}
policeOptionalSkills = {'Forensics': 50, 'Heavy Machinery': 60, 'Heavy Weapons': 50, 'Ride': 60}

progMgrSkills = {'Accounting': 60, 'Bureaucracy': 60, 'Computer Science': 50, 'Criminology': 30,
                 'Foreign Language (choose one)': 50, 'History': 40, 'Law': 40, 'Persuade': 50}
progMgrOptionalSkills = {'Anthropology': 30, 'Art (choose one)': 30, 'Craft (choose one)': 30,
                         'Science (choose one)': 30}

soldierSkills = {'Alertness': 50, 'Athletics': 50, 'Bureaucracy': 30, 'Drive': 40, 'Firearms': 40, 'First Aid': 40,
                 'Military Science (Land)': 40, 'Navigate': 40, 'Persuade': 30, 'Unarmed Combat': 50}
soldierOptionalSkills = {'Artillery': 40, 'Computer Science': 40, 'Craft (choose one)': 40, 'Demolitions': 40,
                         'Foreign Language (choose one)': 40, 'Heavy Machinery': 50, 'Heavy Weapons': 40, 'Search': 60,
                         'SIGINT': 40, 'Swim': 60}

marineSkills = {'Alertness': 50, 'Athletics': 50, 'Bureaucracy': 30, 'Drive': 40, 'Firearms': 40, 'First Aid': 40,
                'Military Science (Sea)': 40, 'Navigate': 40, 'Persuade': 30, 'Unarmed Combat': 50}
marineOptionalSkills = {'Artillery': 40, 'Computer Science': 40, 'Craft (choose one)': 40, 'Demolitions': 40,
                        'Foreign Language (choose one)': 40, 'Heavy Machinery': 50, 'Heavy Weapons': 40, 'Search': 60,
                        'SIGINT': 40, 'Swim': 60}

profSkillReplacement = {profession[0]: anthroskillreplacement, profession[1]: historianskillreplacement,
                        profession[2]: compsciskillreplacement, profession[3]: compsciskillreplacement,
                        profession[4]: fagentskillreplacement, profession[5]: physicianskillreplacement,
                        profession[6]: scientistskillreplacement, profession[7]: specopskillreplacement,
                        profession[8]: criminalskillreplacement, profession[9]: firefighterskillreplacement,
                        profession[10]: fsoskillreplacement, profession[11]: ianalystskillreplacement,
                        profession[12]: icoskillreplacement, profession[13]: lawyerskillreplacement,
                        profession[14]: lawyerskillreplacement, profession[15]: mediaspecialistskillreplacement,
                        profession[16]: nurseskillreplacement, profession[17]: nurseskillreplacement,
                        profession[18]: pilotskillreplacement, profession[19]: pilotskillreplacement,
                        profession[20]: policeskillreplacement, profession[21]: progmgrskillreplacement,
                        profession[22]: soldierskillreplacement, profession[23]: marineskillreplacement}
