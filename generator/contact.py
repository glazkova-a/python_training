from model.contact_model import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_phones(prefix, maxlen):
    symbols = string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_emails(prefix, maxlen):
    symbols = string.ascii_letters + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", surname="")] + [
    Contact(name=random_string("name", 12), middlen=random_string("", 3), surname=random_string("lastname", 15),
            address=random_string("Address", 5), email=random_string_emails("", 9), home_phone=random_string_phones("", 10))
    for i in range(7)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
