from django.shortcuts import render
import sqlite3

def first_page(request):
    return render(request, '../../djangoProject7/templates/1.html')

def second_page(request):
    c = sqlite3.connect('identifier.db')
    cur = c.cursor()
    cur.execute("SELECT amount,date,organization from Donations")
    test = cur.fetchall()
    return render(request, '../../djangoProject7/templates/2.html', {'test': test})


def thr_page(request):
    c = sqlite3.connect('identifier.db')
    car = c.cursor()
    car.execute("SELECT name,contact_info,skills, organization from Volunteers")
    test1 = car.fetchall()
    return render(request, '../../djangoProject7/templates/3.html', {'test1': test1})

