from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def hellofunc(request):
    return render(request, 'titanic/input.html')

def resultfunc(request):
    name = request.POST['Name']
    pclass = request.POST['Pclass']
    gender = request.POST['Gender']
    age = request.POST['Age']
    
    data = {'Name':[name], 'Pclass':[pclass], 'Gender':[gender], 'Age':[age]}
    data = {'PassengerId':[1], 'Pclass':[pclass], 'Name':[name], 'Sex':[gender], 'Age':[age], 'SibSp':['tmp'], 'Parch':['tmp'], 'Ticket':['tmp'], 'Fare':['tmp'], 'Cabin':['tmp'], 'Embarked':['tmp']}
    df = pd.DataFrame(data=data)
    print(df)

    result = str(df) + ': Survived'
    return render(request, 'titanic/result.html', {'result': result})
