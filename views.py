from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.
def index(request):
    #ดึงข้อมูลจากโมเดล person มาใช้ทั้งหมด
    all_person = Person.objects.all()
                                               #key : variable ส่งข้อมูลไปที่ html
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print( name, age)
        #บันทึกข้อมูล
        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"บันทึกข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นนทาง
        return redirect("/")

    else :    
       return render(request,"form.html")
    
def edit(request,person_id):
    if request.method == "POST":
        #เช็ค id
        person = Person.objects.get(id=person_id)
        #เปลี่ยนค่าใหม่
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"อัพเดตข้อมูลเรียบร้อย")
        #เปลี่ยนเส้นนทาง
        return redirect("/")

    else:
        #ดึงข้อูลประชากรที่จะเเก้ไข
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"ลบข้อมูลเรียบร้อย")
    return redirect("/")
    