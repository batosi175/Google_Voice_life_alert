#!/usr/bin/python
import pygvoicelib

#authorizations from google services and various data initializaiton
google_authorization = "r google master code goes here "
username = 'google email address'
auth_token = 'the token that you recieve after'
rnr_se = 'xM1Z8er0XNS4LIeumqbDYuH8Ano='

#creation of our google voice client to use in texting
client = pygvoicelib.GoogleVoice(username,google_authorization,auth_token,rnr_se)

#txtmsg info to send
txtmsg = 'first text message to send out'
txtmsg_contact_info = 'second text to send out'

#key phone numbers: me, mom, dad, cesar, google_me, googel cesar, not yet cindy vo, dad work
numbers = [] #here goes an array of different phone numbers that we will use

# for loop that texts all the numbers in the list

for i in range(0,len(numbers)):
	print "you have texted %d" %(number[i])
	client.sms(numbers[i],txtmsg)
	client.sms(number[si],txtmsg_contact_info)