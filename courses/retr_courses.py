#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

def has_search_result(tag):
    """return true if the tag has class searchResult"""
    return tag.name == u'div' and tag.has_attr('class') and u'searchResult' in tag['class']

def has_course_number(tag):
    """return true if the tag has class courseNumber"""
    return tag.name == u'span' and tag.has_attr('class') and u'courseNumber' in tag['class']

def has_course_title(tag):
    """return true if the tag has class courseTitle"""
    return tag.name == u'span' and tag.has_attr('class') and u'courseTitle' in tag['class']

def has_course_description(tag):
    """return true if the tag has class courseDescription"""
    return tag.name == u'div' and tag.has_attr('class') and u'courseDescription' in tag['class']

def has_course_attributes(tag):
    """return true if the tag has class courseAttributes"""
    return tag.name == u'div' and tag.has_attr('class') and u'courseAttributes' in tag['class']

def parse_course_attributes(course_attributes):
    """parse course attributes and return information about term, units , instructors"""
    # TODO
    return None, None, None

def extract_info(html):
    """extract course information into an array"""
    soup = BeautifulSoup(html)
    all_divs = soup.find_all(has_search_result)
    info = []
    for div in all_divs:
        """use a pattern to match this tag"""
        print div
        course_number = div.find(has_course_number).contents[0]
        course_title = div.find(has_course_title).contents[0]
        try:
            course_description = div.find(has_course_description).contents[0]
        except:
            course_description = ''
        course_attributes = div.find(has_course_attributes).contents[0]
        term, units, instructors = parse_course_attributes(course_attributes)
        info.append({'course_number': course_number, 'course_title': course_title, 'course_description': course_description, 'course_attributes': course_attributes})
    return info

def get_courses_by_page_number(page_number):
    """make get request to fetch cs course information on a certain page"""

    payload = {'view': 'catalog', 'academicYear': '', 'page': page_number, 'q': 'CS', 'filter-departmentcode-CS': 'on', 'filter-coursestatus-Active': 'on'}
    # add headers to bypass robots.txt
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'}
    r = requests.get('https://explorecourses.stanford.edu/search', params=payload, headers=headers)

    return extract_info(r.text)

def get_courses():
    """fetch data from explorecoureses.stanford.edu to get course information"""
    page_number = 0
    courses = []
    while 1:
        result = get_courses_by_page_number(page_number)
        if result == []:
            return courses
        courses += result
        page_number += 1

def test():
    courses = get_courses()
    print courses

if __name__ == '__main__':
    test()
