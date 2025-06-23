
# create a list of all the subjects you take at SHC
subjects = ["11ART","11CSC","11PSY"]

# print out each subject in the list
for subject in subjects:
    print(subject)


# get input via keyboard for a new subject and change it to title case and then add to
new_subject = input("Enter a new subject: ")
subjects.append(new_subject)


# sort the subjects in alphabetic order and print out
subjects.sort()
print("Subjects print in alphabetical order and print out: ")

for subject in subjects:
    print(subject)
