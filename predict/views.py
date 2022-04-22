from urllib.request import Request
from django.shortcuts import render
import joblib
from .models import education
import pandas as pd
from django.shortcuts import redirect
def home(request):
    # if request.user.is_authenticated:
    return render(request, "home.html")

def results(request):
    data = {
    "Age": "",
    "Gender": "",
    "Internships": "",
    "CGPA": "",
    "Certification": "",
    "HistoryOfBacklogs": "",
    "Stream": ""
    }

    data.update({'Age':request.POST['Age']})
    data.update({'Gender':request.POST['Gender']})
    data.update({'Internships':request.POST['Internships']})
    data.update({'CGPA':request.POST['CGPA']})
    data.update({'Certification':request.POST['Certification']})
    data.update({'HistoryOfBacklogs':request.POST['HistoryOfBacklogs']})
    data.update({'Stream':request.POST['Stream']})
    if(request.method=='POST'):
        print('asdasda')
        Education=education()
        
        Education.Age=request.POST['Age']
        Education.Gender=request.POST['Gender']
        Education.Internships=request.POST['Internships']
        Education.CGPA=request.POST['CGPA']
        Education.Certification=request.POST['Certification']
        Education.HistoryOfBacklogs=request.POST['HistoryOfBacklogs']
        Education.Stream=request.POST['Stream']
        Education.save()

    # education(Age=data['Age'],Gender=data['Gender'],Internships=data['Internships'],Stream=data['Stream'],CGPA=data['CGPA'],HistoryOfBacklogs=data['HistoryOfBacklogs'],Certification=data['Certification'])
    copyied_data=dict.copy(data)
    if int(data['Age'])<18:
        return render(request,"result.html",{'ans':"Sorry!Your age doesn't match the criteria",'lst':copyied_data,'reslst':'Age'})
    else:
        for i in data:
            if i=="Stream":
                if data[i]=='Civil':
                    data.update({i:0})
                elif data[i]=='Computer Science':
                    data.update({i:1})
                elif data[i]=='Electrical':
                    data.update({i:2})
                elif data[i]=='Electronics And Communication':
                    data.update({i:3})
                elif data[i]=='Information Technology':
                    data.update({i:4})
                elif data[i]=='Mechanical':
                    data.update({i:5})
            elif i=="Gender":
                if data[i]=='M':
                    data.update({i:1})
                else:
                    data.update({i:0})
            # elif i=="Internships":
            #     if data[i]=='Yes':
            #         data.update({i:1})
            #     else:
            #         data.update({i:0})
            elif i=="Certification":
                if data[i]=='Yes':
                    data.update({i:1})
                else:
                    data.update({i:0})
            elif i=="HistoryOfBacklogs":
                if data[i]=='Yes':
                    data.update({i:1})
                else:
                    data.update({i:0})
        # print(data)
        x=pd.DataFrame(data,index=[0])
        clf=joblib.load('finalized_model.sav')
        ans=clf.predict(x)
        # print(ans)
        if ans[0]==1:
            return render(request,"result.html",{'ans':"Dear student, Thank you for providing your details.As per your inputs, you are eligible to be placed!",'lst':copyied_data})
        else:
            reslst=[]
            for i,y in data.items():
                if i=="Internships":
                    # print(i)
                    if y==0:
                        reslst.append(i)
                elif i=="CGPA":
                    # print(i)
                    if int(y)<=6:
                        reslst.append(i)
                elif i=="HistoryOfBacklogs":
                    # print(i)
                    if y>=1:
                        reslst.append("History Of Backlogs")
            return render(request,"result.html",{'ans':"Oops! You are not eligible to be placed",'lst':copyied_data,'reslst':reslst})