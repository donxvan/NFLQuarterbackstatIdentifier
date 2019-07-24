#this is our main code
average_yards = 4613

passing_yards = input("Enter an amount of passing yards for the 2017-2018 NFL Season.")

if int(passing_yards) >= average_yards:
    print("Ben Roethlisberger 5,129 yrds", "Patrick Mahomes 5,097 yrds", "Matt Ryan 4,924 yrds", "Jared Goff 4,688 yrds")
    print()
elif int(passing_yards) <= average_yards:
    print("Andrew Luck 4,493 yrds", "Aaron Rodgers 4,442 yrds", "Tom Brady 4,395 yrds", "Phillip Rivers 4,308 yrds", "Eli Manning 4,299 yrds", "Kirk Cousins 4,298 yrds") 
    print()
else:
    print("Try Again")

average_int = 10

interception = input("Enter an amount of interceptions for the 2017-2018 NFL Season.")

if int(interception) >= average_int:
    print("Ben Roethlisberger 16 int", "Andrew Luck 15 int", "Patrick Mahomes 12 int", "Phillip Rivers 12 int", "Jared Goff 12 int", "Tom Brady 11 int", "Eli Manning 11 int")
    print()
elif int(interception) <= average_int:
    print("Matt Ryan 7 int", "Aaron Rodgers 2 int", "Kirk Cousins 10 int") 
    print()
else:
    print("Try Again")

average_comp = 395

completion = input("Enter an amount of completions for the 2017-2018 NFL Season.")

if int(completion) >= average_comp:
    print("Ben Roethlisberger 452 completions", "Andrew Luck 430 completions", "Kirk Cousins 425 completions", "Matt Ryan 422")
    print()
elif int(completion) <= average_comp:
    print("Patrick Mahomes 383 completions", "Jared Goff 364 completions", "Aaron Rodgers 372 completions", "Tom Brady 375 completions", "Phillip Rivers 347 completions", "Eli Manning 380 completions") 
    print()
else:
    print("Try Again")

average_td = 32.7

touchdown = input("Enter an amount of touchdowns for the 2017-2018 NFL Season.")

if int(touchdown) >= average_td:
    print("Patrick Mahomes 50 TD's" "Jared Goff 32 TD's", "Ben Roethlisberger 34 TD's", "Andrew Luck 39 TD's", "Matt Ryan 35 TD's")
    print()
elif int(touchdown) <= average_td:
    print("Aaron Rodgers 25 TD's", "Tom Brady 29 TD's", "Phillip Rivers 32 TD's",  "Eli Manning 21 TD's", "Kirk Cousins 20 TD's") 
    print()
else:
    print("Try Again")

average_qbr = 101.1

qbr = input("Enter a quarterback rating for the 2017-2018 NFL Season.")

if int(qbr) >= average_qbr:
    print("Jared Goff 101.1", "Phillip Rivers 105.5", "Matt Ryan 108.1", "Patrick Mahomes 113.8")
    print()
elif int(qbr) <= average_qbr:
    print("Ben Roethlisberger 96.5", "Andrew Luck 98.7", "Aaron Rodgers 97.6",  "Eli Manning 92.4", "Tom Brady 97.7", "Kirk Cousins 99.7") 
    print()
else:
    print("Try Again")
