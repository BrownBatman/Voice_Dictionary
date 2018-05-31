import json
from difflib import get_close_matches
#from unidecode import unidecodef
#from safeprint import print
data = json.loads(open("data.json").read())
w = input("Give Input ")
w = w.lower()

li = get_close_matches(w,data.keys(),6)

print(li)
