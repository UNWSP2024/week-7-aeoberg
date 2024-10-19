# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

if __name__ == '__main__':
    totalRainfallInput = []

    for nbr in range (1,13):
        rainfallInput = int(input('What was the rainfall for month ' + str(nbr) +'? '))
        totalRainfallInput.append(rainfallInput)

    totalRainfall = sum(totalRainfallInput)
    averageRainfall = totalRainfall/12
    minimum = str(min(totalRainfallInput))
    maximum = str(max(totalRainfallInput))

    print()
    print('Average Monthly Rainfall:',round(averageRainfall,2))
    print('Total Rainfall:',totalRainfall)
    print('Minimum:', minimum)
    print('Maximum:', maximum)