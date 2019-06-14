from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    split_date = date.split(' ')
	if len(split_date[1]) > 4:
	    check_spelling_index = split_date.pop(1)
	    check_word = []
	    for char in check_spelling_index:
		    check_word.append(char)
	    check_word.pop(3)
	    check_word = ''.join(check_word)
	    split_date.insert(1, check_word)
	    date = ' '.join(split_date)
	    converted_date = datetime.strptime(date, '%d %b, %Y')
	    return int(THIS_YEAR - converted_date.year)
	else:
		' '.join(split_date)
		converted_date = datetime.strptime(date, '%d %b, %Y')
		return int(THIS_YEAR - converted_date.year)


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    datetime_object = datetime.strptime(date, '%m/%d/%Y')
    return datetime_object.strftime('%d/%m/%Y')