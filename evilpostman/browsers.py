from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style
from selenium import webdriver
from proxy import *
import time, random

def GeneratePassword(PasswordLen):
    PasswordSymbols = list('1234567890abcdABCD!@#$%^&*()-=_?')                                      
    random.shuffle(PasswordSymbols)                                                                 
    return ''.join([random.choice(PasswordSymbols) for x in range(PasswordLen)]) 

def GenerateName():
    Names = ['Alexander', 'Michael', 'Charles', 'John',
             'Matthew', 'Daniel', 'Heracl', 'Gabriel',
             'Claude', 'Anatole', 'Andrew', 'Basil',
             'Benjamin', 'Vincent', 'George', 'Eugene',
             'Geoffrey', 'Elias', 'Joseph', 'Leo',
             'Nicholas', 'Paul', 'Peter', 'Serge']
    return random.choice(Names)

def GenerateSurname():
    Surnames = ['Abramson', 'Adamson', 'Adderiy', 'Dean',
                'Charison', 'Brickman', 'Bush', 'Laird',
                'MacAdam', 'Jones', 'Oliver', 'Roger',
                'Porter', 'Shorter', 'Vance', 'Wallace',
                'Wood', 'Sykes', 'Dodson', 'Clifford',
                'Evnas', 'Gill', 'Farmer', 'Nikson']
    return random.choice(Surnames)
    
def Registration(DriverPath, PasswordLen, Speed, OutputDirectory, ProxysList):
    if(ProxysList == None):
        print(Fore.RED + 'You are not using a proxy. It is possible to block by IP')
    else:
        ConnectToProxy(ProxysList)
    try:
        Name = GenerateName()
        Surname = GenerateSurname()
        AccountPassword = GeneratePassword(PasswordLen)
            
        driver = webdriver.Firefox(executable_path=DriverPath) 
        driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp')

        FirstName = driver.find_element_by_id('firstName')
        FirstName.send_keys(Name)
            
        time.sleep(Speed)
            
        LastName = driver.find_element_by_id('lastName')
        LastName.send_keys(Surname)
        time.sleep(Speed)

        Username = driver.find_element_by_name('Username').text
        
        Password = driver.find_element_by_name('Passwd')
        Password.send_keys(str(AccountPassword))
        time.sleep(Speed)
            
        ConfirmPassword = driver.find_element_by_name('ConfirmPasswd')
        ConfirmPassword.send_keys(str(AccountPassword))
        time.sleep(Speed)
            
        NextButton = driver.find_element_by_id('accountDetailsNext').click()
        time.sleep(Speed)
            
        DayOfBirthday = driver.find_element_by_class_name('whsOnd zHQkBf')
        DayOfBirthday.send_keys('31')
        time.sleep(Speed)
            
        YearOfBirthday = driver.find_element_by_class_name('rFrNMe uIZQNc og3oZc zKHdkd sdJrJc Tyc9J')
        YearOfBirthday.send_keys('1992')
        time.sleep(Speed)
            
        MonthOfBirthday = Select(driver.find.element_by_id('month'))
        MonthOfBirthday.select_by_index(2)
        time.sleep(Speed)
            
        Gender = Select(driver.find.element_by_id('gender'))
        Gender.select_by_index(2)
        time.sleep(Speed)
            
        PersonalDetailsButton = driver.find_element_by_id('personalDetailsNext').click()
        time.sleep(Speed)

        FinalStage = driver.find_element_by_id('termsofserviceNext').click()

        print(Fore.GREEN + '[+]One mail was registred')
        
        Results = open(output, 'x')
        Results.write('GMail: ' + Username + '@gmail.com' + '  ' + 'Password: ' + AccountPassword + '\n')
        Results.close()
    except:
        print(Fore.RED + '[-]O-o-ops! Problem. Your IP could be blocked or did you specify the wrong paths. Rechek your paths and try again')
        print(Fore.RED + '[~]Changing proxy...')
        driver.quit()

