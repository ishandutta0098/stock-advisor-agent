import time
from datetime import datetime

# Current date for context
Now = datetime.now()
Today = Now.strftime("%d-%b-%Y")


# Callback function to print a timestamp
def timestamp(Input):
    print(datetime.now())
