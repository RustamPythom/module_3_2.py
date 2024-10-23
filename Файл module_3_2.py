def send_email(message, recipient, *, sender="university.help@gmail.com"):

    def is_valid_email (email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if is_valid_email(sender) == False or is_valid_email(recipient) == False:
        print( "Невозможно отправить письмо с адреса <sender> на адрес <recipient>")


    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return


    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

