from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

contacts_book = []
for person_data in contacts_list:
    #person_data = row.split("\n")
    #person_surname = person_data[0]
    #person_name = person_data[1]
    #person_father_name = person_data[2]
    person_fio = " ".join(person_data[:2])
    person_organization = person_data[3]
    person_position = person_data[4]
    person_email = person_data[6]
    person_phone = person_data[5]
    phone_pattern = r"(8|\+7)?\s*\((\d+\)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)(\s*(\D+)(\d+))?)"
    person_phone = re.sub(phone_pattern, r"+7(\2)\3-\4-\5\[s]('доб.')\[s]\6", person_phone)

    pattern_fio = re.compile([person_data[0]])
    for man in range(len(contacts_book)):

        if (match := re.match(pattern_fio, person_fio).group()) is False or (match_tel := re.search(phone_pattern, person_phone).group()) is False:
            person = {"FIO": person_fio, "organisation": person_organization, "person_email": person_email, "contact phone": person_phone}
            contacts_book.append(person)

print(contacts_book)
#print(contact_dic)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
