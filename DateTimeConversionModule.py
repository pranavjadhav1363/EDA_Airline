monthmap = {
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
      "December": 12,
  }

def ConvertAndDivideInDaysMonthsAndYear(date):
    dict ={}
    splitdate = date.split(' ')
    if len(splitdate[0])>3:
        dict['day']=splitdate[0][:2]
    else:
        dict['day'] =splitdate[0][:1]
    dict['month']=monthmap[splitdate[1]]
    dict['year'] =splitdate[2]
    return dict
        