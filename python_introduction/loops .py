def dateofweeks(date):
 match date:
  case 1:
    return "Monday"
  case 2 | 3:
    return "Tuesday"
  case 4:
    return "Thursday"
  case 5:
    return "Friday"
  case 6:
    return "Saturday"
  case 7:
    return "Sunday"
  case _:
    return "Invalid day number, please enter a number between 1 and 7"
date = input("Enter a number between 1 and 7: ")
print(dateofweeks(int(date)))