from random import choice
from game_data import data
from art import logo
from art import vs

def add_used(data):
  for term in data:
    term['Used']='No'

def print_term(term):
  print(term['name'])
  print(term['description'])
  print(term['country'])

def is_term_available():
  available=False
  for term in data:
    if term['Used']=='No':
      available = True
  return available

def checker(term1,term2,chosen):
  if term1["follower_count"]>term2["follower_count"] and chosen ==1:
    return True
  elif term1["follower_count"]<term2["follower_count"] and chosen ==2:
    return True
  else:
    return False

def pick_term():
  chosen_term={}
  decision_needed=True
  if is_term_available == False:
    return chosen_term
    
  while decision_needed:
    chosen_term=choice(data)
    if chosen_term['Used']=='No':
      decision_needed=False
      index=data.index(chosen_term)
      data[index]['Used']='Yes'
  return chosen_term    
  



###main code

print(logo)
add_used(data)

game_on = True
score =0
term1=pick_term()
term2=pick_term()
while game_on == True:
  print_term(term1)
  print(vs)
  print_term(term2)
  chosen = int(input("\nWhich has higher follers?(1 or 2)"))
  game_on=checker(term1,term2,chosen)
  if game_on == True:
    print("You survive")
    term1=term2
    term2={}
    term2=pick_term()
    if len(tern2)==0:
      print("You Win")
      game_on = False
    score += 1
  else:
    print(f"You lost with a score of {score}")
