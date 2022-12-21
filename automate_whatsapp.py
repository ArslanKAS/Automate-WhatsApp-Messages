import pywhatkit as WA

# Sending Message to a Phone Number 
phone_number = "+92XXXXXXXXXX" # Country code + number
message = "Hi, How are you?"
hour = 9  # Its 9:30 AM at our region
minute = 37
WA.sendwhatmsg(phone_number, message, hour, minute)


# Sending Message to a Group
group_id = "C2PGURuNfpN4rruIYzjfT9" # The Group's ID
message = "Good Morning, Group Fellows"
hour = 9 # Its 9:30 AM at our region
min = 40
WA.sendwhatmsg_to_group(group_id, message, hour, min)


