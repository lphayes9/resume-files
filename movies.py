     #Lily Hayes
# Class:         CSC 110 - Fall 2023
# Assignment:    Programming Project Design
# Due Date:      October 27, 2023

# Program Title: Movies Data

# Project Description:
# --------------------
# This program will ask the user to select from 6 options and then
# display movie data based on the selection. The code will take data
# from a large data file of movies and will use different functions
# to display the data the user wants. The program will run until the
# user indicates otherwise.


#This function with get all of the data from the file and put it into lists separating it
def getData():
    #Initializes the lists of data
    titleList = []
    genreList = []
    directorList = []
    yearList = []
    runList =[]
    revenueList = []

    #User input for the file with exception handling
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            newFile = open(fname, "r")
            goodFile = True
        except IOError:
            print("Invalid file name try again ...")

    
    #Appending all data too new lists
    newFile.readline()

    for line in newFile:
        
        title, genre, director, year, runTime, revenue = line.split(",")
        line.strip()
        titleList.append(title)
        genreList.append(genre)
        directorList.append(director)
        yearList.append(int(year))
        runList.append(int(runTime))
        revenueList.append(float(revenue))
    
    return(titleList, genreList, directorList, yearList, runList, revenueList)



#This function will print the user choices and then ask for an input to return
def getChoice():
    #Printing all choice options
    print("\nPlease choose one of the following options:")
    print("1 -- Find all films made by a specified director")
    print("2 -- Find the highest grossing film made in a specific year")
    print("3 -- Find all films made in a given year range in a specified genre")
    print("4 -- Search for a film by title")
    print("5 -- Find average runtime of films with higher revenue than specified value")
    print("6 -- Sort all lists by revenue and write the results to a new file")
    print("7 -- Quit")
    #Making sure the choice is an int and in correct range
    temp = False
    while temp == False:
        choice = input("Choice ==> ")
        try:
            choice = int(choice)
            if choice >= 1 and choice <=7:
                temp = True
            else:
                print("Choice must be between 1 and 7")
                
        except ValueError:
            print("Invalid entry - Try again")
    
    print("")

    return choice



#This function will get all of the films made by a director from the user input
def getDirectorFilms(titleList, genreList, directorList, yearList, runList, revenueList):
    director = ""
    temp = False
    #Getting the director input with exception handling
    while temp == False:
        director = input("Enter director: ")
        if director in directorList:
            temp = True
        else:
            print("Invalid entry - Try again")
    completeList = []

    #Finding the director in the list and appending the information about that director to the return list
    for i in range(len(directorList)):
        if director == directorList[i]:
            completeList.append([titleList[i], genreList[i],director, yearList[i],runList[i],revenueList[i]])

    return(completeList)



#This function will display the information about the highest grossing film made in the year the user selects
def highGrossingFilm(titleList, genreList, directorList, yearList, runList, revenueList):
    #Initialize the year variable as a string and temp variable
    year = ""
    temp = False

    #While loop that will go until the year that is entered is entered correctly and in the range
    while temp == False:

        #This try statement will make sure the year input is an integer 
        year = input("Enter year: ")
        temp2 = False
        try:
            year = int(year)
            temp2 = True
        except ValueError:
            print("Invalid entry - Try again")

        #This will make sure the year is in the correct range and is in the yearList  
        if temp2 == True:
            if year >= 2006 and year <= 2016:
                if year in yearList:
                    temp = True
                else:
                    print("Invalid entry - Try again")
            else:
                print("Year out of range, must be between 2006 and 2016")

    #Initializes the list that will store a list of all information about the highest grossing      
    highestGrossingList = []

    #This for loop makes a list of all the revenues of the given year
    revenuesOfYear = []
    for i in range(len(yearList)):
        if year == yearList[i]:
            revenuesOfYear.append(revenueList[i])

    #For loop that will find the highest revenue index from the revenueOfYear list
    highestRevenue = revenuesOfYear[0]
    for i in range(1, len(revenuesOfYear)):
        if revenuesOfYear[i] > highestRevenue:
            highestRevenue = revenuesOfYear[i]

    #Finds index of highest revenue and append all information to the final list
    revenueIndex = revenueList.index(highestRevenue)
    highestGrossingList.append([titleList[revenueIndex], genreList[revenueIndex], directorList[revenueIndex], year, runList[revenueIndex], str(highestRevenue)])

    return(highestGrossingList)



#This function will display all of the films made in a specific year range prompted by the user
def yearRangeFilms(titleList, genreList, directorList, yearList, runList, revenueList):
    year1 = ""
    year2 = ""
    temp = False
    print("Enter year range to search (oldest year first)")

    #While loop to run until the the user inputs are valid
    while temp == False:

        #Making sure the input for the first year is an int
        year1 = input("Year1: ")
        tryTemp = False
        try:
            year1 = int(year1)
            tryTemp = True
        except ValueError:
            print("Invalid entry - Try again")

        #If statements that make sure the first input is valid 
        if tryTemp == True:
            if year1 >= 2006 and year1 <= 2016:
                if year1 in yearList:
                    tempYear2 = False
                    #To run until year 2 is valid
                    while tempYear2 == False:
                        
                        #Making sure the second year is an int
                        year2 = input("Year2: ")
                        tryTemp2 = False
                        try:
                            year2 = int(year2)
                            tryTemp2 = True
                        except ValueError:
                            print("Invalid entry - Try again")
                                    
                        #If the second year entry in valid 
                        if tryTemp2 == True:
                            if year2 > year1 and year2 <= 2016:
                                if year2 in yearList:
                                    temp = True
                                    tempYear2 = True

                                #Else if the second year is not in the yearLIst
                                else:
                                    print("Invalid Entry - Try again")

                            #Else is the second year is not in the year range
                            else:
                                print("Second year should be after first year - try again")
                                break

            #Else if the first year is not in the year range
            else:
                print("Year out of range, must be between  2006 and 2016")

    #Thi while loop will get the user entry for genre    
    genre = ""
    tempGenre = False
    while tempGenre == False:
        genre = input("Enter genre: ")
        if genre in genreList:
            tempGenre = True
        else:
            print("Invalid entry - Try again")

    #This for loop appends the index of the horror movie to a list
    indexList = []
    for i in range(len(genreList)):
        tempList = genreList[i].split(";")
        
        #If the movie is in the year range
        if yearList[i] >= year1 and yearList[i] <= year2:
            for j in range(len(tempList)):
                if tempList[j] == genre:
                    indexList.append(i)

        
    #This for loop append all the information about the horror movie to a list of lists        
    yearRangeList = []
    for i in range(len(indexList)):
        index = indexList[i]
        yearRangeList.append([titleList[index], genreList[index], directorList[index], yearList[index], runList[index], revenueList[index]])
        
                  
    return(yearRangeList)



#This function will find all of the information about a film chosen by the user by name
def searchFilm(titleList, genreList, directorList, yearList, runList, revenueList):
    title = ""
    temp = False
    
    #Getting the title input with exception handling
    while temp == False:
        title = input("Enter title: ")
        if title in titleList:
            temp = True
        else:
            print("\nNo such film exists.")
            temp = True

    #Finding the film in the film list and appending the film to the return list
    searchFilmList =[]
    for i in range(len(titleList)):
        if titleList[i] == title:
            searchFilmList.append([title, genreList[i], directorList[i], yearList[i], runList[i], revenueList[i]])
       
    
    return(searchFilmList)



#This function will find the average runtime of films with a higher revenue than the user given threshold
def aveRunTime(runList, revenueList):
    threshold = ""
    temp = False

    #Getting the user input with exception handling
    while temp == False:
        threshold = input("Enter revenue limit (millions): $")
        try:
            threshold = int(threshold)
            temp = True
        except ValueError:
            print("Invalid Entry - Try again")

    #Finding the highest revenue in the list and putting it in a variable to make sre the threshold isn't higher
    highestRevenue = 0
    for i in range(len(revenueList)):
        if revenueList[i] > highestRevenue:
            highestRevenue = revenueList[i]
   
    averageRunTime = 0
    counter = 0

    #If the threshold is greater than the highest it will return nothing
    if threshold > highestRevenue:
        print("No films have revenue higher than $", "{:.2f}".format(threshold), "million.")
    #Else it will add the average runtime of each revenue and keep track of counter for average
    else:
        for i in range(len(revenueList)):
            if revenueList[i] > threshold:
                averageRunTime = averageRunTime + runList[i]
                counter += 1
    #Will do the math for average than print the final average if the threshold is valid
    if threshold < highestRevenue:
        averageRunTime = averageRunTime / counter
        finalAverage = "{:.2f}".format(averageRunTime)
        print("The average runtime for films with revenue higher than $", "{:.2f}".format(threshold), "million is", finalAverage,"minutes.")

        
    return


#This function will sort all of the data by revenue and add it to a new file
def sortLists(titleList, genreList, directorList, yearList, runList, revenueList):
    #Initializes the file and opens to write
    fileName = "movies-sorted-rev.csv"
    fname = open(fileName, "w")

    #Uses the bubble sort method t rearrange the items in each of the lists by revenue
    revenueLength = len(revenueList)
    for i in range(revenueLength - 1):
       for j in range(0, revenueLength - i - 1):
           if revenueList[j] > revenueList[j+1]:
               titleList[j], titleList[j+1] = titleList[j+1], titleList[j]
               genreList[j], genreList[j+1] = genreList[j+1], genreList[j]
               directorList[j], directorList[j+1] = directorList[j+1], directorList[j]
               yearList[j], yearList[j+1] = yearList[j+1], yearList[j]
               runList[j], runList[j+1] = runList[j+1], runList[j]
               revenueList[j], revenueList[j+1] = revenueList[j+1], revenueList[j]

    #Writes the new lists into the file
    for i in range(len(revenueList)):
        line = (f"{titleList[i]}, {genreList[i]}, {directorList[i]}, {yearList[i]}, {runList[i]}, {revenueList[i]}\n")    
        fname.write(line)

    #Closes file and print the confirmation it has been written
    fname.close()
    print("Sorted data has been written to the file: movies-sorted-rev.csv.") 
    
    
    return()


#This function will print the results
def printResults(completeList):
    
    #If there is noting in the complete list it will return nothing
    if len(completeList) == 0:
        return
    #If the complete list lenth is 1 it will do the same but change the initial print statement slightly
    elif len(completeList) == 1:
        print("\nThe film that meets your criteria is:\n")

        #Initializes new list since the parameter is a list of lists
        titleList = []
        genreList = []
        directorList = []
        yearList = []
        runList = []
        revenueList = []

        #For the lists in the complete List it will take the elements in the sublist and append it to the new lists for printing
        for subList in completeList:
            titleList.append(subList[0])
            genreList.append(subList[1])
            directorList.append(subList[2])
            yearList.append(subList[3])
            runList.append(subList[4])
            revenueList.append(subList[5])

        #Prints the category lines
        print("\nTITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))

        #Print out all of the information
        for i in range(len(titleList)):
            print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))
    #This else does the same thing as above but changes the first print statement slightly when the parameter list has more than one sublist
    else:
        #This is changed
        print("\nThe films that meet your criteria are:")

        titleList = []
        genreList = []
        directorList = []
        yearList = []
        runList = []
        revenueList = []

        for subList in completeList:
            titleList.append(subList[0])
            genreList.append(subList[1])
            directorList.append(subList[2])
            yearList.append(subList[3])
            runList.append(subList[4])
            revenueList.append(subList[5])

        print("\nTITLE".ljust(45), "GENRE".ljust(35), "DIRECTOR".ljust(24), "YEAR".ljust(8), "RUNTIME".ljust(8), "REVENUE(mil)".rjust(12))
        for i in range(len(titleList)):
            print(titleList[i].ljust(45), genreList[i].ljust(35), directorList[i].ljust(24), str(yearList[i]).ljust(8), str(runList[i]).ljust(8), ("$"+str(revenueList[i])).rjust(12))

    return


#Main Function
def main():
    #Gets all the data from the file and initializes choise
    titleList, genreList, directorList, yearList, runList, revenueList = getData()
    choice = 0

    #Will run until the choice is 7 
    while choice != 7:
        choice = getChoice()
        if choice == 1:
            fullDirectorList = getDirectorFilms(titleList, genreList, directorList, yearList, runList, revenueList)
            printResults(fullDirectorList)
        elif choice == 2:
            highestGrossingList = highGrossingFilm(titleList, genreList, directorList, yearList, runList, revenueList)
            printResults(highestGrossingList)
        elif choice == 3:
            yearRangeList = yearRangeFilms(titleList, genreList, directorList, yearList, runList, revenueList)
            printResults(yearRangeList)
        elif choice == 4:
            searchFilmList = searchFilm(titleList, genreList, directorList, yearList, runList, revenueList)
            printResults(searchFilmList)
        elif choice == 5:
            aveRunTime(runList, revenueList)
        elif choice == 6:
            sortLists(titleList, genreList, directorList, yearList, runList, revenueList)
        elif choice == 7:
            print("Good-bye")
        

        
    




