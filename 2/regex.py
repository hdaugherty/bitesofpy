import re


def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    re_pattern = re.compile(r"(\d\d:\d\d)+")
    return re_pattern.findall(flask_course)


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    regex_list = []
    re_pattern_1 = re.compile(r"http://(\w)+.html")
    re_pattern_2 = re.compile(r"#(\w)+")
    regex_list.append(re_pattern_1.findall(tweet))
    regex_list.append(re_pattern_2.findall(tweet))
    return regex_list



def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    pass
