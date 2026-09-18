import time

def print_pause(text, delay=1.0): #def (define) declares a function
 print(text)
 time.sleep(delay)

def play_game():
 # 1. INITIALIZING THE LIST: Start with an empty inventory
 inventory = []


 print_pause("--- Welcome to the Dragon's Keep ---") #print_pause delays the print_
 print_pause("You stand before a dark, ancient castle.")
 print_pause ("Your goal is to defeat the dragon inside, but you are empty-handed.")
 # First Area: The Outpost
 print_pause("\n[Area 1: The Outpost]")
 print_pause("You see a shiny Sword resting on a stone pedestal.")

 choice1 = input("Do you want to pick up the sword? (yes/no): ").lower().strip()
 if choice1 == "yes":
 # 2. ADDING TO A LIST: Using .append() to add an item
  inventory.append("Sword")
  print_pause("✨ You added a Sword to your inventory!")
 else:
   print_pause("You decide to leave the sword behind.")
 # 3. READING FROM A LIST: Showing current inventory items
 print(f"\n🎒🎒 Current Inventory: {inventory}")
 time.sleep(1)
 # Second Area: The Guard Tower
 print_pause("\n[Area 2: The Guard Tower]")
 print_pause("A heavy wooden door blocks your path. It is locked tight.")   
 print_pause("You look around and find a rusty Key hidden under a rug.")

 choice2 = input("Do you want to pick up the key? (yes/no): ").lower().strip()
 if choice2 == "yes":
     inventory.append("Key")
     print_pause("✨ You added a Key to your inventory!")
 # 4. CHECKING A LIST: Using 'in' to see if an item is present
 if "Key" in inventory:
   print_pause("\n🔓🔓 You use the Key from your inventory to unlock the heavy door and pass through!")
 # 5. REMOVING FROM A LIST: Using .remove() because the key was consumed
   inventory.remove("Key")
 else:
     if "Sword" in inventory:
      print_pause("\n💥💥 The door is locked. You try to kick it down, making lots of noise!")
      print_pause("The noise alerts a goblin guard! You are forced fight it off Breaking your sword in the process!")
      inventory.remove("Sword")
     else:
         print_pause("\n💥💥 The door is locked. You try to kick it down, making lots of noise!")
         print_pause("\n The noise alerts a goblin guard! You are forced fight it off with nothing but your fists! as he comes around the corner you assume your fighting stance! Only to be stabbed in the gut by a spear. Naturally you Die! GAME OVER")
         return
 print(f"\n🎒🎒 Current Inventory: {inventory}")
 time.sleep(1)
 # Third Area: The Lair
 print_pause("\n[Area 3: The Dragon's Lair]")
 print_pause("The massive red dragon wakes up and roars, blowing fire everywhere!")

 # 6. CONDITIONAL GAME OUTCOME BASED ON LIST STATE
 if "Sword" in inventory:
  print_pause("\n⚔ You draw your Sword from your inventory!")
  print_pause("With a heroic strike, you defeat the dragon and save the kingdom!")
  print_pause("🏆🏆 CONGRATULATIONS, YOU WIN!")
 else:
  print_pause("\n🔥🔥 You have no weapons to defend yourself!")
  print_pause("The dragon breathes a wave of fire. You were roasted like a marshmallow.")
  print_pause("💀💀 GAME OVER.")
# Run the game
if __name__ == "__main__":
    play_game()