from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    contacts_list_edited = [contacts_list[0]]
    for string in contacts_list:
        FIO = ' '.join(string[:3])
        first_three = FIO.split(" ")[0:4]
        if '' in first_three:
          first_three.remove('')

        result = re.findall('\d+', string[5])
        res1 = ''.join(result)
        # print(len(res1))
        # print(res1)
        new_phone = []
        if len(res1) == 11:
            pattern = r'(^7|^8)(\d\d\d)(\d\d\d)(\d\d)(\d\d)'
            subs = r'+7(\2)\3-\4-\5'
            phone = re.sub(pattern, subs, res1)
            new_phone.append(phone)
        if len(res1) == 15:
            pattern = r'(^7|^8)(\d\d\d)(\d\d\d)(\d\d)(\d\d)(\d\d\d\d)'
            subs = r'+7(\2)\3-\4-\5 доб.\6'
            phone = re.sub(pattern, subs, res1)
            new_phone.append(phone)
        if len(res1) == 0:
            phone = ''
            new_phone.append(phone)

        string_new_name = first_three + string[3:5] + new_phone + string[6:]
        contacts_list_edited.append(string_new_name)
    contacts_list_edited.pop(1)
    # print(contacts_list_edited)

    contacts_list_edited_no_double = []
    contacts_total_ok = []
    names = []
    names2 = []
    double = []
    for contact in contacts_list_edited:
        if contact[0]+contact[1] not in names:
            names.append(contact[0]+contact[1])
            contacts_list_edited_no_double.append(contact)
        else:
            double.append(contact)
            names2.append(contact[0] + contact[1])
    for contact in contacts_list_edited_no_double:
        if contact[0] + contact[1] not in names2:
            contacts_total_ok.append(contact)

    # print(double)
    # print(contacts_list_edited_no_double)
    # t = []
    for double_user in double:
        t = []

        for contact_ok in contacts_list_edited_no_double:
            if contact_ok[0] == double_user[0] and contact_ok[1] == double_user[1]:
                t.append(contact_ok)
                t.append(double_user)
        # print(t)
        x = t[0]
        s = t[1]
        xs = zip(x, s)
        toto = []
        tooo = []
        for xx in xs:
            xx_list = list(set(list(xx)))
            if '' in xx_list:
                if len(xx_list) > 1:
                    xx_list.remove('')
            toto.append(xx_list)
        for tototo in toto:
            tooo.append(tototo[0])
        # print(tooo)
        contacts_total_ok.append(tooo)

    # for rrr in contacts_total_ok:
    #     print(rrr)



with open("phonebook.csv", "w", encoding="cp1251") as f:
  writerr = csv.writer(f)
  writerr.writerows(contacts_total_ok)




