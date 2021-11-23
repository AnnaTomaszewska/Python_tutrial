from typing import SupportsRound


story = "once upon a time"

print(story.capitalize()) #pierwsza litera robi się duża
print(story.title()) #wszystkie pierwsze litery robią się duże
print(story.upper()) #capslock
print("HELLO".lower()) #pomniejsza litery
print("AbCdE".swapcase()) #zmienia wielkosc liter
print("ANNA TOMASZEWSKA".lower().title())

story = story.title()
print(story)