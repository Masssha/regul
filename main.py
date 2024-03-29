from pprint import pprint
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

with open("new_phonebook_raw.csv", "w", encoding="cp1251") as f:
  writerr = csv.writer(f)
  writerr.writerows(contacts_list)
