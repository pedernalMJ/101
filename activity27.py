print("Adding Data to dictionary")
print("============================")
t = True
empty_dictionary = {}


def print_anime():
  for i,j in empty_dictionary.items():
    print(f"code = {i}  title = {j}")

def search_anime(key):
    print("Searching anime in dictionary")
    print(f"result shows{empty_dictionary[key]}")
  

while t == True:
  keys = input("keys for this anime --->")
  value = input("eneter the anime title--->")
  
  empty_dictionary[keys]= value

  choice = input("what would you like to continue adding\n y = yes \n n = no \n p = print anime\n s = serach --->").lower()

  if choice == 'y':
    print('continue')
    continue

  elif choice == "n":
    print("existing")
    break
  
  elif choice == "p":
    print_anime()
    continue
  elif choice == "s":
    search_anime(keys)
    continue
   
  
  else:
    print("invalid input")
    
