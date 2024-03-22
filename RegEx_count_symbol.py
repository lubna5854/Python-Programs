
import re
input_string="@dfd$%^FG^&*BG!"
res=re.findall(r"[A-Za-z0-9]",input_string)
print("Length: ",len(input_string)-len(res))

#  Output
#  Length : 8