# ---creating a random generator project---------
import random

#---------key parameters-------------
l_caps = "ABCDEFGHIJKLMN"
l_lower = "abcdefghijklmn"
numbers = "1234567890"
special_characters = "~!@#$%^&*()_+"
length_of_password = 20
password_generated = l_caps + l_lower + numbers + special_characters

#---------joing the parameters to constitute a paassword randomly generated-----------
password = "".join(random.sample(password_generated, length_of_password))
print(f"My password is: {password}")
