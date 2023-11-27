from django.shortcuts import render
from django.http import HttpResponse

def index(request, name, age, interests):
    text='<h1>Информция обо мине(:</h1> <h3> <br><br>'\
        f'<p>Мое ФИО: {name}</p>'\
        f'<p>Мой возраст: {age}</p>'\
        f'<p>Moи инетерсы: {interests}</p>'
    return HttpResponse(text)


def about(request,I_from, performance, study):
    text1=f'<h1>Страница абоут:)</h1>'\
    f'<p>Я из {I_from}</p>'\
    f'<p>Учился я с средним баллом в {performance}</p>'\
    f'<p>Люблю ли я учиться? конечно {study}</p>'
    return HttpResponse(text1)


def contacts(request,GitHub,Telegramm,contact,contact1):
    text2=f'<h1>А вот и мои контакты:-)</h1>'\
    f'<p>Допустим вот мой гитхаб {GitHub}</p>'\
    f'<p>Тележка от гитхаба ничем не отличается:=)  {Telegramm}</p>'\
    f'<p>Мой номер телефона{contact1} :)</p>'\
    '<br><br><br><br><br><br><br><br><br><br><br><br><br>'\
    f'хи-хи, вы же не можете туда позвонить((((<br> поэтому вот рашн номер :D  {contact}'
    return HttpResponse(text2)

