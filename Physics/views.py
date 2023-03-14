from django.shortcuts import render

# Create your views here.

def Condition(request):
    d={"Vari":12}
    return render(request,'If_Condition.html',d)

def If_Else(request):
    s={"x":"Raj"}
    return render(request,'If_Else.html',s)

def If_Elif_Else(request):
    a={"x":120,"y":80,"z":58}
    return render(request,'If_Elif_Else.html',a)


def Nested_If(request):
    a={"x":120,"y":180,"z":258}
    return render(request,'Nested_If.html',a)

def Forloop(request):
    d={"Name":"Raja sekhar"}
    return render(request,'Forloop.html',d)