# Follow the instructions in the tab to the right
# Write your mad libs program here
import gtts
import random
print("Welcome to Mad libs choose some words to make a silly story")
persons_name = input("Enter the name of your school mate: ")
school_name =input("Enter the name of the school you met: ")
adjective = input("Enter an adjective: ")
first_session = input("Enter the name of the first session you had: ")
school_name = input("Enter the name of school: ")
total_studygroups = input("Enter the total number of the study groups: ")
group_name = input ("Enter your group's names: ")
project_name = input("Enter the name of the project: ")
group_name =input("Enter the group's name: ")
persons_name = input("Enter the name of your school mate: ")
print() 
title =("HOW WE MET")
story = f" {persons_name} recently met on {school_name} program . The first {adjective} session where we were officially welcomed and introduced to the {school_name} official team. After the first session, we were grouped into {total_studygroups} study groups and we happened to fall under {group_name} . After settling into our respective study groups, we were assigned a project work called {project_name}. From the list of our names, we decided to have teams of three and that is how {persons_name} met."
print(title)
print(story)
tts = gtts.gTTS(story)
tts.save(adjective + ".mp3")