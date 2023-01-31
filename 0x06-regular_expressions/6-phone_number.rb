#!/usr/bin/env ruby
#To match regular digit phone number

import re

phone_number = "4155049898"

match = re.search(r"^\d{10}$", phone_number)

if match:
        print("Valid phone number")
else:
      print("Invalid phone number")
