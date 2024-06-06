from typing import *
from loginService import *

email = emailValidator()
password = passwordValidator()
answer = login(email,password)

print(f"az email:{email} a jelszo:{password} {answer}")