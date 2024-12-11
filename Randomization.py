import random
import json

# List of team members with their aliases
team_members = [
    ("Dhruv", "dhruvkmr"),
    ("Raghu", "sastry"),
    ("Aamir", "sofiaami"),
    ("Abhishek Gupta", "aabhgup"),
    ("Abhinav Sharma", "abhinew"),
    ("Ishant Arora", "aroish"),
    ("Arun Jaladi", "arujalad"),
    ("Sankalp", "talwarsa"),
    ("Anupam Kashyap", "kaanupam"),
    ("Deeksha", "shukdeek"),
    ("Abhinav Relan", "arrelan"),
    ("Abhishek Kumar", "kmarqab"),
    ("Akul Jain", "akuljain"),
    ("Arun Saraswat", "arsarasw"),
    ("Bharath Raj", "bharja"),
    ("Bilal Khan", "khanvbil"),
    ("Gaurav Tiwari", "qtiwarig"),
    ("Geerthana Murali", "imgeer"),
    ("Gopikrishna K", "gopikrif"),
    ("Harshi Sharma", "harshixs"),
    ("Jahnavi Potdar", "potdhjah"),
    ("Joseph Plammoottil", "plammojo"),
    ("Mihir Gupta", "mihgupt"),
    ("Mohit Sharma", "msmohit"),
    ("Nakul Pradeep", "nakulpr"),
    ("Nitesh Gautam", "nitegaut"),
    ("Rahul Raturi", "raturir"),
    ("Ritik Chopde", "ritikgc"),
    ("Shiva Jain", "jnshiva"),
    ("Shubham Gupta", "shubhfet"),
    ("Shubham Kundu", "kucshubh"),
    ("Shubham Sharma", "shbhsh"),
    ("Shweta Tiwari", "ftiwarsh"),
    ("SWAPNIL SARKAR", "sarkswap")
]

# Generate secret Santa pairings
def generate_pairings():
    random.shuffle(team_members)
    pairings = list(zip(team_members, team_members[1:] + [team_members[0]]))
    pairing_dict = {}
    for (gifter, gifter_alias), (recipient, recipient_alias) in pairings:
        pairing_dict[gifter_alias] = recipient_alias
    return pairing_dict

# Generate and save pairings
pairings = generate_pairings()
with open('pairings.json', 'w') as f:
    json.dump(pairings, f, indent=2)

print("Pairings have been generated and saved to 'pairings.json'")
