import random
import string


def Token_Generator(size=40, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
   return ''.join(random.choice(chars) for _ in range(size))
