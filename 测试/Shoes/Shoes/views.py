from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
import json

def getusershoes_views(request,numl):
    # numl=request.GET['userid']
    # print(type(numl))
    numl=numl
    if numl:
     
        dic={}    
        name=User.objects.filter(id=int(numl))
        if name:
            dic['username']=name[0].name
            shoes=name[0].shoes_set.all()
            l=[] 
            for sh in shoes:
                d={}
                d['id']=sh.id
                d['color']=sh.color
                d['size']=sh.size
                l.append(d)
            dic['shoes']=l
            return HttpResponse(json.dumps(dic))
        else:
            return HttpResponse('用户不存在')

    else:
        return HttpResponse('查询失败　请输入 getusershoes/数字')


   
    

def updateusershoes_views(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        size=int(request.POST['size'])
        color=request.POST['color']
        user=User.objects.filter(name=name,phone=phone)

        if user:
            user_id=user[0].id
            obj=Shoes(size=size,color=color,user_id=user_id)
            obj.save()
            obj1=Shoes.objects.filter(user_id=user_id)
            l=[]
            for ob in obj1:
                l.append(ob.id)
            dic={"success":'true',
                "messsage":"ok",
                "result":{"userid":user_id,"shoesid":l}
                }
            return HttpResponse(json.dumps(dic))
        else:
            user=User(name=name,phone=phone)
            user.save()
            use=User.objects.get(name=name)
            obj=Shoes(size=size,color=color,user_id=use.id)
            obj.save()
            obj1=Shoes.objects.filter(user_id=use.id)
            l=[]
            for ob in obj1:
                l.append(ob.id)
            dic={"success":'true',
                "messsage":"ok",
                "result":{"userid":use.id,"shoesid":l}
                }
            return HttpResponse(json.dumps(dic))

       

