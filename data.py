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

skills = ['Accounting', 'Alertness', 'Anthropology', 'Archeology', 'Art (Type)', 'Artillery', 'Athletics',
          'Bureaucracy', 'Computer Science', 'Craft', 'Criminology', 'Demolitions', 'Disguise', 'Dodge', 'Drive',
          'Firearms', 'First Aid', 'Foreign Language (Type)', 'Forensics', 'Heavy Machinery', 'History', 'HUMINT',
          'Law', 'Medicine', 'Melee Weapons', 'Military Science (Type)', 'Navigate', 'Occult', 'Persuade', 'Pharmacy',
          'Pilot (Type)', 'Psychotherapy', 'Ride', 'Science (Type)', 'Search', 'SIGINT', 'Stealth', 'Surgery',
          'Survival', 'Swim', 'Unarmed Combat', 'Unnatural']


# Anthropologist, recommended INT, Anthropology 50, Bureaucracy 40, Foreign language (1) 50, Foreign language (2) 40,
# History 60, Occult 40, Persuade 40
# Choose two of these you don't already have: Archeology 40, HUMINT 50,
# Navigate 50, Ride 50, Search 60, Survival 50
