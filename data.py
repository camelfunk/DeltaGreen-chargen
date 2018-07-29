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

skills = {'Accounting': 10, 'Alertness': 20, 'Anthropology': 0, 'Archeology': 0, 'Art (Type)': 0, 'Athletics': 30,
          'Artillery': 0, 'Bureaucracy': 10, 'Computer Science': 0, 'Craft (Type)': 0, 'Criminology': 10,
          'Demolitions': 0, 'Disguise': 10, 'Dodge': 30, 'Drive': 20, 'Firearms': 20, 'First Aid': 10,
          'Foreign Language (Type)': 0, 'Forensics': 0, 'Heavy Machinery': 10, 'Heavy Weapons': 0, 'History': 10,
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

