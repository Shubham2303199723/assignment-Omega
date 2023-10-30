from django.http import HttpResponse 
from django.shortcuts import render
from party.models import party

Select_City=0
Address=0
MobileNo=0
GSTNo=0
Party_Type=0
Address_full=0
Email=0
Land_line=0

def homepage(request):
    return render(request, "index.html")

def sve_party(request):
    global Select_City, Address, MobileNo, GSTNo, Address_full, Email, Land_line, Party_Type
    if request.method=="POST":
        Select_City=request.POST.get('Select_City',Select_City)
        Address=request.POST.get('Address',Address)
        MobileNo=request.POST.get('mobileNo',MobileNo)
        GSTNo=request.POST.get('gstno',GSTNo)
        Party_Type=request.POST.get('party_type',Party_Type)
        Address_full=request.POST.get('address_full',Address_full)
        Email=request.POST.get('email',Email)
        Land_line=request.POST.get('landline',Land_line)
        Party_Data=party(Select_city=Select_City,Address=Address,Mobile_no=MobileNo,GSTNO=GSTNo,Party_Type=Party_Type,Address_full=Address_full,Landline_no=Land_line)
        Party_Data.save()
    return render(request,"index.html")
    
