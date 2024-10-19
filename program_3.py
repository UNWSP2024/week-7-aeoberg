# Program #3: US_Population
from multiprocessing.managers import value
from select import select


def main():
    # Have the user input (using a loop) various information that contains three pieces of data:
    # year, name of state, and population.
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    count = 0
    numberOfInputs = int(input('How many times would you like to add information? '))

    while count < numberOfInputs:
        ynp = [0, 1, 2]
        ynp[0] = int(input("Enter year: "))
        ynp[1] = input('Enter a state name: ')
        ynp[2] = int(input(f'Enter a the population of {ynp[1]} in {ynp[0]}: '))
        count += 1
        all_entered_values.append(ynp)
        # print(all_entered_values)

    # Now have the user enter a year.
    selectedYear = input("Which year would you like the population of? ")

    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    totalPop = sum_population_for_year(all_entered_values, selectedYear)
    print(f'The total population in {selectedYear} is {totalPop}.')

def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year. 
    # e.g. for the list on line 7 the total would be 8,860,637 if the user entered 2010 for the year to sum,
    # or 3,421,988 if they entered 2011 for the year to sum.
    total = 0
    mylist = []

    for mylist in all_entered_values:
        if int(year_to_sum) == mylist[0]:
            total += mylist[2]

    return total
    # print the totalled population

# Call the main function.
main()