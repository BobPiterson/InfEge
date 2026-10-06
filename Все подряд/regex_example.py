# Программа проверяет правильность оформления регулярных выражений

import re

# pattern = r".*thernet[0-9]+(?:[\/\.:][0-9]+)+[,:]?(?:\x20|$)"

# test_strings = [
#     "gigabitethernet1/0/1: up",      # ✅
#     "fastethernet0/0.100, down",     # ✅
#     "loopback0",                      # ❌ нет "thernet"
#     "ethernet0",                      # ❌ нет разделителя
# ]

# for s in test_strings:
#     if re.search(pattern, s):
#         print(f"✅ {s}")
#     else:
#         print(f"❌ {s}")

pattern = r"(?<=757\/)\d+"
#pattern = r"ge-[0-9]+(?:[\/\.:][0-9]+)+[,:]?(?:\x20|$)"
s = '757/00000'

#pattern = r"^No alarms currently active$"
#s = 'No alarms currently active'

if re.search(pattern, s):
    print(f"✅ {s}")
else:
    print(f"❌ {s}")
