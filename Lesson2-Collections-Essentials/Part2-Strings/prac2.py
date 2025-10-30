def format_phone_number(phone):
    phone.replace(" ", "").replace("-", "").replace("(","").replace(")", "")
    if len(phone) == 10 and phone.isdigit():
        return ("({phone[0,1,2]}) {phone[3,4,5]}-{phone[6,7,8,9]}")
    return "Invalid phone number"
    
print(format_phone_number("(123) 456-7890"))
print(format_phone_number("6767"))
