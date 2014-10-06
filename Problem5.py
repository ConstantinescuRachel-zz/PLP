"""
Problem 5:

Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:

Use list[index] notation to get a element from a list.
"""



subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)): #Parcurgem subjectul
    for j in range(len(verbs)): #Parcurgem verbs
        for k in range(len(objects)): #Parcurgem Objects
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k]) # Creare lista
            print sentence #Printare lista


