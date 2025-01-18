def send_email(message, recipient, *, sender="university.help@gmail.com"): # создали функцию с аргументами сообщение,
    # получатель (обычные) и отправитель (со значением по умолчанию)
    boole = recipient.find('@') >= 0 and recipient.endswith((".com", ".ru", ".net")) \
            and sender.find('@') >= 0 and sender.endswith((".com", ".ru", ".net")) # Метод find() – это инструмент для
    # поиска подстроки в строке, а метод endswith() - для проверки того, заканчивается ли строка определенной подстрокой
    if boole == False: # если строки не содержит "@" или не оканчиваются на ".com"/".ru"/".net", то вывести
        print(f'Невозможно отправить письмо с адреса   {sender}   на адрес   {recipient}')
        return
    if sender == recipient: # если совпадают, то вывести
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == 'university.help@gmail.com': # если отправитель по умолчанию university.help@gmail.com, то вывести
        print(f'Письмо успешно отправлено с адреса   {sender}   на адрес   {recipient}')
    else: # иначе вывести
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса   {sender}   на адрес   {recipient}')
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')