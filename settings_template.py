# Rename this file to settings.py

# Your company username
USERNAME = ''

# Your company password
PASS = ''

# A Census API key you can request here: https://api.census.gov/data/key_signup.html
CENSUS_KEY = ''

# Add your company's proxy URL here
PROXY = ''

# The variable we'll use to send the message via a company proxy (otherwise it won't work)
PROXIES = { 'https' : 'https://{user}:{password}@{proxy_url}:8080'.format(user=USERNAME, password=PASS, proxy_url=PROXY) } 
