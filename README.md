# AWS-Educate api key
## Get Api-Keys from AWS-Educate
### It uses Selenium webdriver for the interaction

### TODO:
Take it to requests(?)

### Usage
Create a creds.py file with this structure:

    username = "username_amazon_aws"
    password = "password_amazon_aws"


Create venv w/ requirements.txt

    python3 -m venv <pathvenv>
    source <pathvenv>/bin/activate
    pip install -r requirements.txt


Copy geckodriver in a path available in $PATH (recommended `<pathvenv>/bin/geckdriver` if you decide to use virtual environments)

Launch selen.py and wait for the API_Keys to appear
