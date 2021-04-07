#!/usr/bin/env/python

#imports
import os
import time as t
from flask import Flask, render_template, request, flash
import scraping_details
from city_info import get_places
from send_emails improt send_all_mails
from lists import *
from city_scraping import city_places

global last_country_data
global israel_data
global glo_data
global time_checked
global top_countries
app = Flask(__name__)

def remove_comas(num):
    new_num = ''
    for i in num:
        if i != ',':
            new_num += i
    return int(new_num)

def update_data(ip):
    global last_country_data
    global israel_data
    global glo_data
    global top_countries
    global time_checked
    first_time = False
    try:
        glo_data[ip]
    except (KeyError, NameError):
        first_time = True

    if first_time or t.time() - time_checked[ip] > 600:
        da = scraping_details.coronatime('')
        last_country_data[ip] = da

        israel_data[ip] = last_country_data[ip]
        glo_data[ip] = scraping_details.glo()
        top_countries[ip] = scraping_details.getop()
        time_checked[ip] = t.time() 