# -*- coding: utf-8 -*-
"""
Uses scraper to get job details from glassdoor
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "D:/Projects/Salary Scraper/chromedriver"

df = gs.get_jobs('software engineer',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)