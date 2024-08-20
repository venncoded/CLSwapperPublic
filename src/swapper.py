from datetime import date
def monthify(target_date):
    match target_date.month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6: 
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9: 
            return "September"
        case 10: 
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"

def dayify(target_date):
    match target_date.day:
        case 1 | 21 | 31:
            return str(target_date.day)+"st"
        case 3 | 23:
            return str(target_date.day)+"rd"
        case 2 | 22:
            return str(target_date.day)+"nd"
        case _:
            return str(target_date.day)+"th"
        
def datify(uncondate):
    return monthify(uncondate)+" "+dayify(uncondate)+", "+str(uncondate.year)
        
company=input("What is the name of the company you are applying to? ")
position=input("What is the title of the position being applied for? ")
today=datify(date.today())
file_path=position+company+today+".txt"
with open(file_path, 'w') as file:
    with open("draft.txt",'r') as draft:
        content = str(draft.read())
        content=content.replace("$",company)        
        content=content.replace("%",position)
        content=content.replace("#",today)
        file.write(content)
print("You are applying to a "+position+" position at "+company+" on "+today+".")

