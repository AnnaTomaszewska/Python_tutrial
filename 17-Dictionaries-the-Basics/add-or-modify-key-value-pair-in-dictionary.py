sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckam"]
}

sports_team_rosters["Pittsburgh Steelers"] = ["Antonio Brown", "Ben XYCVZHA"]
print(sports_team_rosters)

sports_team_rosters["New York Giants"] = ["Eli Manning"] # w tym momencie kasujemy pozostale wartosci
print(sports_team_rosters) 

sports_team_rosters = {}

sports_team_rosters["New England Patriots"] = ["Tom Brady", "Rob Gronkowski", "Julian Edelman"]
sports_team_rosters["New York Giants"] = ["Eli Manning", "Odell Beckam"]

print(sports_team_rosters) # można zapisać jak powyżej; tak też można zmieniać wartości

words = ["danger", "beware", "beware", "beware", "danger"]

def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_words(words))