import mechanize
import cookielib
import re

# Browser
br = mechanize.Browser()

cj = cookielib.LWPCookieJar()

br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.set_handle_equiv(True)

# Go to https://www.mshare.net/websurvey/app?gateway=PandaWebCSat
response = br.open('https://www.mshare.net/websurvey/app?gateway=PandaWebCSat')

# print response.read()

br.select_form(nr=0)
# print br.form
br.form['promptInput_69174'] = '2035'

response = br.submit()
# print response.read()

br.select_form(nr=0)
br.form['RadioGroup'] = ['0']

response = br.submit()
# print response.read()

# input check number
br.select_form(nr=0)
number = raw_input('Enter Check: ')
br.form['promptInput_82628'] = number
response = br.submit()

br.select_form(nr=0)
# select date (MM/dd/yyyy)
br.form['promptInput_76592'] = '09/20/2013'
# select what time of day did you visit us
br.form['RadioGroup'] = ['0']
# select how full were the majority of the trays on the steam table
br.form['RadioGroup_0'] = ['0']
response = br.submit()

br.select_form(nr=0)
# select my order type
br.form['RadioGroup'] = ['0']
response = br.submit()

br.select_form(nr=0)
# your overall satisfaction with your experience at this Panda
br.form['RadioGroup_0'] = ['1']
response = br.submit()

br.select_form(nr=0)
# what was the reason behind your rating?
br.submit()

br.select_form(nr=0)
# were your greeted when you arrived
br.form['RadioGroup'] = ['0']
br.form['RadioGroup_0'] = ['1']
br.form['RadioGroup_1'] = ['1']
br.submit()

br.select_form(nr=0)
# please rate your overall satisfaction with the ...
br.form['RadioGroup_2'] = ['1']
br.form['RadioGroup_2_0'] = ['1']
br.form['RadioGroup_2_1'] = ['1']
br.form['RadioGroup_2_2'] = ['1']
br.form['RadioGroup_2_3'] = ['1']
br.form['RadioGroup_2_4'] = ['1']
br.submit()

br.select_form(nr=0)
# please rate your satisfaction with the ...
br.form['RadioGroup_2'] = ['1']
br.form['RadioGroup_2_0'] = ['1']
br.form['RadioGroup_2_1'] = ['1']
br.form['RadioGroup_2_2'] = ['1']
br.form['RadioGroup_2_3'] = ['1']
br.submit()

br.select_form(nr=0)
# based on this visit what is the likelihood that you will ...
br.form['RadioGroup_0'] = ['0']
br.submit()

br.select_form(nr=0)
# did you experience a problem at any time during your visit
br.form['RadioGroup'] = ['1']
br.submit()

br.select_form(nr=0)
# did you have any other comments today?
br.submit()

br.select_form(nr=0)
# thanks for your feedback. the last few questions are for classification purposes only
# in a typical month, how many times do you visit a panda express
br.form['RadioGroup'] = ['3']
# what is your gender
br.form['RadioGroup_0'] = ['0']
# what is your age
br.form['RadioGroup_1'] = ['1']
# which of the following best describes your reason for your most recent visit to panda express
br.form['RadioGroup_2'] = ['0']
# would like to participate in surveys or receive special offers in the future?
br.form['RadioGroup_3'] = ['2']
response = br.submit()

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.read())
print soup.find(id='promptText_72474').span.text
