import sys
import pygame
import winsound

user_input = " "
y = True
Y = True
n = False
N = False

pygame.init()
pygame.mixer.init()
pygame.mixer.init()

Cyndaquil = "C://Users//6378b_000//Desktop//Cyndaquil.wav"
Chikorita = "C://Users//6378b_000//Desktop//Chikorita.wav"
Totodile = "C://Users//6378b_000//Desktop//Totodile.wav"
Psyduck = "C://Users//6378b_000//Desktop//Psyduck.wav"
Charizard = "C://Users//6378b_000//Desktop//006_Charizard_Cry.wav"
Firered = "C://Users//6378b_000//Desktop//102-opening-demo.wav"

print "Play a Pokemon sound!\n\n Press \"Y\" to continue or \"N\" to exit."

yes_play = input()


while yes_play == y or yes_play == Y:

    print "\tA key for Cyndaquil\n\tS key for Chikorita\n\tD key for Totodile\n\tF key for Psyduck\n\tZ key for Charizard\n\tQ key for Opening Theme for Pokeomn Fire Red\n\n"


    while 1:
       char = sys.stdin.read(1)
       user_input = user_input + char
       

       if char == 'a'or char =='A' :
           print "You choose Cyndaquil!\n"
           winsound.PlaySound(Cyndaquil,winsound.SND_FILENAME|winsound.SND_ALIAS)
           

       elif char == 's' or char == 'S' :
           print "You choose Chikorita!\n"
           winsound.PlaySound(Chikorita,winsound.SND_FILENAME|winsound.SND_ALIAS)
           

       elif char == 'd' or char == 'D' :
           print "You choose Totodile!\n"
           winsound.PlaySound(Totodile,winsound.SND_FILENAME|winsound.SND_ALIAS)

       elif char == 'z' or char == 'Z':
           print "You choose Charizard!\n"
           winsound.PlaySound(Charizard,winsound.SND_FILENAME|winsound.SND_ALIAS)

       elif char == 'f' or char == 'F' :
           print "You choose Psyduck!\n"
           winsound.PlaySound(Psyduck,winsound.SND_FILENAME|winsound.SND_ALIAS)

       elif char == 'q' or char == 'Q' :
           print "Opening to Pokemon Fire Red"
           winsound.PlaySound(Firered,winsound.SND_FILENAME|winsound.SND_ALIAS)
           
 # how to make it so that any other output prints error but still goes through the loop       
       else:
           print "Would you like to play another sound?\n\t'Y' or 'N'?"
           yes_play = input()
           break

else:
    print "Bye! Have a nice day!"

 
