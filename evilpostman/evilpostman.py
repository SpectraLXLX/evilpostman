from browsers import *
import argparse

print("""
         ..--""|
       |     |
       | .---'
 (\-.--| |-----------.      Python version: 3.7.2
/ \) \ | |            \     Script version: 1.0
|:.  | | |             |    Support browsers: Firefox        
|:.  | |o| EVIL POSTMAN|     
|:.  | `"`             |    Made by Spectra (c)
|:.  |_  __   __ _  __ /
`""""`""""|=`|"""""""`
          |=_|
    jgs   |= |

     """)

argument = argparse.ArgumentParser(description='Aurotegestration for GMAILs accounts on Python 3.7.2')

argument.add_argument('PathToDriver', type=str, help='Path to driver for your browser. Now script support only Firefox, but i add Google and Opera after any time')
argument.add_argument('AccountsCount', type=int, help='Number of accounts')                                                                                        

argument.add_argument('-pL', type=int, default=8, help='Password len')
argument.add_argument('-s', type=int, default=3, help='The speed of registration. The higher the value the lower the speed. Also, the faster the speed the greater the chance of blocking your ip address') #Заменить этот ключ на параметр скорости регестрации (time.sleep(?))
argument.add_argument('--output', type=str, default='D:\\results.txt', help='Directory where created gmail will be saved')
argument.add_argument('--proxys_list', type=str, default=None, help='Your proxy list that you can use')

Results = argument.parse_args() 

while(Results.AccountsCount != 0):
    Results.AccountsCount = Results.AccountsCount - 1
    Registration(Results.PathToDriver, Results.pL, Results.s, Results.output, Results.proxys_list)

