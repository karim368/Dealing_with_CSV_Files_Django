from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
import csv
def insert_bank(request):
    with open('app\\bank.csv', 'r') as FO:
        IDO = csv.reader(FO)
        for i in IDO:
            bn = i[0].strip()
            BO = Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Records inserted into Bank File successfully')

def insert_branch(request):
    with open('app\\branch1.csv','r') as FO:
        IOD = csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn = i[0]
            BO = Bank.objects.filter(bank_name = bn)
            if BO:
                # BANK,IFSC,BRANCH,ADDRESS,CONTACT,CITY,DISTRICT,STATE
                ifs = i[1]
                bra = i[2]
                add = i[3]
                con = i[4]
                ci = i[5]
                dist = i[6]
                sta = i[7]
                BRO = Branch(bank_name = BO[0],ifsc=ifs,branch=bra,address=add,contact=con,city = ci,district = dist,state = sta)
                BRO.save()

    return HttpResponse('Branches are inserted into Branch Csv File')