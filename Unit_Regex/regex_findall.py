import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#zero or one groups means that findAll returns string list of instances
resume = '''555-423-5842, alksjdf;lads, asldfldsa, as;dflj 523-455-9073,
al;jdslfkjaa;lsjfdlk lajsd;fk, 555-333-4528'''
oneNum = phoneRegex.search(resume)
print(str(oneNum))
allNum = phoneRegex.findall(resume) #Returns a list w/ all instances
print(allNum)

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#Divided into two or more groups
allNum = phoneRegex.findall(resume)
#returns list of tuples w/ strings
print(allNum)

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
#Makes the entire thing a group, returns big group, then sub-groups in order
#left to right
allNum = phoneRegex.findall(resume)
print(allNum)



