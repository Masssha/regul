import re
from pprint import pprint


text = 'Опросыыы показал, что женщины и молодые работники менее склонны тревожиться из-за работы. В географическом разрезе наиболее низкая доля людей, опасающихся потери работы, выявлена на Урале (21%) и Северном Кавказе (24%), наиболее высокая — на Дальнем Востоке (38%) и в Сибири (36%)! В разрезе отраслей наиболее оптимистичны работники финансового низкое сектора (71%), промышленности, медицины и образования (по 70%). В целом эксперты связывают снижение тревожности с текущей ситуацией на рынке труда: очень низкая безработица, компании постоянно ощущают дефицит кадров.'

# pattern = 'низк\w+'
# result = re.findall(pattern, text)
# print(result)
gi
# result = re.findall('\w+', text)
# print(result)
# print(len(result))

# result = re.split(r'[.!?]', text)
result = re.split(r'[.!?]\s*', text)

# result.remove("")
# for x in result:
#     if x != "":
#         print(x)
print(result)
print(len(result))



from pprint import pprint

import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list_edited = []
  for string in contacts_list:
      FIO = ' '.join(string[:3]).strip()
      first_three = FIO.split(" ")
      if '' in first_three:
          first_three.remove('')
      string_new = first_three + string[3:]
      contacts_list_edited.append(string_new)
      print(string_new)
  # print(contacts_list_edited)
      # ".".join(string[:2])
      # print(string[:3])
    # split(" ")
# pprint(contacts_list)

# with open("phonebook.csv", "w", encoding="cp1251") as f:
#   writerr = csv.writer(f)
#   writerr.writerows(contacts_list_edited)


      res2 = re.split(r'', res1)
      res2.pop(0)
      res3 = ' '.join(res2)

      for double_user in double:
          t = []
          t_new = []
          for contact_ok in contacts_list_edited_no_double:
              if contact_ok[0] == double_user[0] and contact_ok[1] == double_user[1]:
                  t.append(contact_ok)
                  t.append(double_user)
          # t_set = set(t)
          for tt in t:
              for ttt in tt:
                  if ttt not in t_new:
                      t_new.append(ttt)