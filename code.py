#this is our main code
average_yards = 4613

passing_yards = input("Enter an amount of passing yards for the 2017-2018 NFL Season.")

if int(passing_yards) >= average_yards:
    print("Ben Roethlisberger 5,129 yrds", "Patrick Mahomes 5,097 yrds", "Matt Ryan 4,924 yrds", "Jared Goff 4,688 yrds")
elif int(passing_yards) <= average_yards:
    print("Andrew Luck 4,493 yrds", "Aaron Rodgers 4,442 yrds", "Tom Brady 4,395 yrds", "Phillip Rivers 4,308 yrds", "Eli Manning 4,299 yrds", "Kirk Cousins 4,298 yrds") 
else:
    print("Try Again")
