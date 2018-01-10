# The 100worst.csv file contains the 100 worst singles over 25 years.
# Your task is to check which year produced the most.
# So create the necessary function(s).
# And print out the sentence below with the proper year.
#  `The year when the most worst songs came out is <year>.`

def count_years(filename):
    songs_by_year = dict()
    with open('100worst.csv','r') as file:
        lines = file.readlines()
        for line in lines:
            year = line.split(';')[-1]
            songs_by_year[year] = songs_by_year.get(year,0) + 1 # .get(year,0) ha nem találja a kulcsot, akkor visszadja a másik paramétert a 0-át, ha megtalálja, akkor hozzáad +1et            
    worst_year = max(songs_by_year.keys(),key=songs_by_year.get)
    # veszi a maximum ertek szerinti kulcsot
    return "The year when the most worst songs came out is {}.".format(worst_year)


print(count_years('100worst.csv'))