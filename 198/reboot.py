from datetime import datetime, timedelta
from string import ascii_letters
import re

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    # Set allowd characters and reassign reboots as only those allowed.
    allowed = set(ascii_letters + ' ' + '1' + '2' + '3' + '4' + '5' + '6' + '7' + '8' + '9' + '0' + ':')
    reboots = ''.join(letter for letter in reboots if letter in allowed)

    # Set the pattern to be removed from the list of date strings and remove it
    pattern = r'reboot                             '
    split_reboots = re.split(pattern, reboots)
    split_reboots.remove('')

    # Set date format, create formatted list of dates
    date_format = "%a %b %d %H:%M"
    formatted_dates_list = []
    for output in split_reboots:
        formatted_dates_list.append(datetime.strptime(output, date_format))

    # Sort dates list
    formatted_dates_list.sort()

    # Go through sorted dates and determine the uptime durations
    date_one = 0
    reboot_duration_list = []
    for idx, output in enumerate(formatted_dates_list):
        date_two = output

        if date_one == 0:
            date_one = output
            continue

        else:
            temp_date = (date_one - date_two).days
            date_one = date_two
            reboot_duration_list.append(temp_date)

    # Assign both the index and uptime duration to the proper variables
    max_duration = 0
    uptime_index = 0
    for idx, uptime in enumerate(reboot_duration_list):
        if abs(uptime + 1) > max_duration:
            max_duration = abs(uptime + 1)
            uptime_index = idx + 1
        else:
            continue

    # Return tuple of the uptime duration and date
    return max_duration, formatted_dates_list[uptime_index].strftime(f"{datetime.today().year}-%m-%d")


if __name__ == '__main__':
    calc_max_uptime(MAC1)
