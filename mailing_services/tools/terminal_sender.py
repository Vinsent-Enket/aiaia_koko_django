from django.core.mail import send_mail

send_mail(
    subject=input('Введите тему сообщения--> '),
    message=input('Введите текст сообщения--> '),
    from_email=input('Введите ваш email--> '),
    recipient_list=list(input('Введите email получателя--> '),)
)
