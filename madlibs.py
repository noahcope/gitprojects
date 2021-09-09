def printRequest(request):
    results = []
    for x in (request):
        results.append(input("give me a " + x))
    return results

#main
print("Give us the following things for our Mad Lib!")
request = ["adjective: ", "animal: ", "vehicle: ", "verb: ", "color: ", "noun: ", "1st food: ", "2nd food: ", "person: ", "saying: "]
fillers = tuple(printRequest(request))

answer = "Today I went to my favorite Taco Stand called the %s %s. Unlike most food stands, they cook and prepare the food in a %s while you %s. The best thing on the menu is the %s %s. Instead of ground beef they fill the taco with %s, cheese, and top it off with a salsa made from %s. If that doesn't make your mouth water, then it's just like %s always says: %s!"
print (answer % fillers)
