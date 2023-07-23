def main():
    print ("Input date in the format 9/9/1636 or September 8, 2004!")
    date = input("What's today's date? ").title()

    day, month, year = check_date(date)
    print (f"{year}-{month:02}-{day:02}")
    
def check_date(date):

    months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
    }

    try:
        if '/' in date:
            day, month, year = date.split('/')
            #print (f"1. {day} {month} {year}")

        elif ',' in date:
            first, year = date.split(',')
            month_1, day = first.split(' ')
            #print (f"2. {day}-{month_1}-{year}")

            if month_1 in months:
                month = months[month_1]
                #print (f"3. {day} {month} {year}")
 
        day, month, year = int(day), int(month), int(year)
    
    except (UnboundLocalError, ValueError):
        exit("Invalid format!")

    return day, month, year


main()