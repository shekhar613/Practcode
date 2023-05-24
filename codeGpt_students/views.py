from django.shortcuts import render
from django.http import HttpResponse
import json
from codeGpt_students import compiler ,testcase
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,"home.html")

def userlogin(request):
    if request.method == "POST":
        print(request.POST)
        
        data = json.dumps({
            "status":"done!!"
        })
        return HttpResponse(data)

    else:
        return render(request,"user_login.html")

def createUser(request):
    # if request.method == "POST":
    #     print(request.POST)
        
    #     data = json.dumps({
    #         "status":"created!!"
    #     })
    #     return HttpResponse(data)

    # else:
    return render(request,"create_user.html")

def userDashboard(request):
    return render(request,"user_dashboard.html")

def testingCompiler(request):
    Questions_objs = Question.objects.all()
    serializer = Questions_Serializer(Questions_objs,many=True)
    data = {}
    questionData = {}
   
    for i in range(len(serializer.data)):
        data[i] = [serializer.data[i]["question"],serializer.data[i]["id"]]
        questionData[serializer.data[i]['id']] = [serializer.data[i]["example"], serializer.data[i]["exp_inputs"] , serializer.data[i]["exp_outputs"],serializer.data[i]["constraint"]]
       
    return render(request,"newcompiler.html",{'ExamplesQuestion': json.dumps(dict(questionData)),'testcases':data ,'totalQues':len(serializer.data)})

def test_compilerCode(request):
    if request.method == "POST":

        # For Test the user code
        if(json.loads(request.body)["mode"]=="Testcode"):
            print("-"*15)
            Questions_objs = Question.objects.get(id=json.loads(request.body)["questionId"])
            serializer = Questions_Serializer(Questions_objs)
            print(serializer.data['testcases']['public'])
            # with open("questions.json", "r") as jsonFile:
            #     data = json.load(jsonFile)
            
            # code_output = compiler.run_code(json.loads(request.body))
            # print(json.loads(request.body))
            # print(str(json.loads(request.body)["code"]))
            testCaseStatus = testcase.play({
                'id': json.loads(request.body)["questionId"],
                'question': str(json.loads(request.body)["code"]),
                'test_cases':serializer.data['testcases']['public'], 'expected_outputs': serializer.data['expected']['public'],
                'language': json.loads(request.body)["language"]
                })
            # testCaseStatus["testcase output"]=code_output
            
            print(f"Final ouput \n {testCaseStatus} \n")
            
            return JsonResponse(testCaseStatus)
        # For Submit the user code and retrun private testcases result
        else:
            pass

    else:

        return render(request,"home.html")

def mycourses(request):
    return render(request,"mycourses.html")


# django JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# create user account and return token
class Registeruser(APIView):

    def post(self,request):
        # creating user in user model of django with token
        user_serializer = Createuser_Serializer(data = request.data)
        if not user_serializer.is_valid():
            print(user_serializer.errors)
            return Response({"status":403,"error":user_serializer.errors})

       
        user_serializer.save()
        user = User.objects.get(username = user_serializer.data['username'])
        refresh = RefreshToken.for_user(user)

        # Storeing other data of student  
        request.data['token']={'refresh': str(refresh),'access': str(refresh.access_token)}
        # request.data['password']=user_serializer.data['password']
        
        print(request.data)
        Student_dataserializer = Student_Serializer(data=request.data)
        if not Student_dataserializer.is_valid():
                print(Student_dataserializer.errors)
                User.objects.get(username = user_serializer.data['username']).delete()
                return Response({"status":403,"error":Student_dataserializer.errors})
        
        Student_dataserializer.save()

        return Response({"status":200,"token":{
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                },
                "payload":Student_dataserializer.data
                }
            )

# check user and return data
class Authenticateuser(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        Student_objs = Student.objects.all()
        serializer = Student_Serializer(Student_objs,many=True)
        return Response({"status":200,"payload":serializer.data})

    def post(self,request):
        data = request.data
        serializer = Student_Serializer(data=request.data)

        if not serializer.is_valid():
            print("Invalid data")
            return Response({"status":404,"message":"Invalid data","error":serializer.errors})
    
        serializer.save()
        print("testing in api_view")
        return Response({"status":"created!! at JWT"})
    
    def patch(self,request):
        try:
            student_obj = Student.objects.get(id= request.data['id'])
            serializer = Student_Serializer(student_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({"status":403,"error":serializer.errors})

            serializer.save()
            return Response({"status":200,"payload":serializer.data})
    
        except Exception as e:
            return Response({"status":403,"message":"invalid id"})

# create new token and login

class LoginAuth_token(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
       # Get the username and password from the request
    

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful
            login(request, user)
            r = User.objects.get(username = username)
            refresh = RefreshToken.for_user(r)

            

            return Response({'message': 'Login successful','token':str(refresh.access_token)})
        
        else:
            # Authentication failed
            return Response({'message': 'Invalid username or password'})
            



















# ==================================testing of JWT ==========================================

# class authenticationApiView(APIView):
#     authentication_classes = [JWTAuthentication]
   
#     def get(self,request):
#         Student_objs = Student.objects.all()
#         serializer = Student_Serializer(Student_objs,many=True)
#         return Response({"status":200,"payload":serializer.data})

#     def post(self,request):
#         data = request.data
#         serializer = Student_Serializer(data=request.data)

#         if not serializer.is_valid():
#             print("Invalid data")
#             return Response({"status":404,"message":"Invalid data","error":serializer.errors})
    
#         serializer.save()
#         print("testing in api_view")
#         return Response({"status":"created!! at JWT"})
    
#     def patch(self,request):
#         try:
#             student_obj = Student.objects.get(id= request.data['id'])
#             serializer = Student_Serializer(student_obj,data=request.data,partial=True)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({"status":403,"error":serializer.errors})

#             serializer.save()
#             return Response({"status":200,"payload":serializer.data})
    
#         except Exception as e:
#             return Response({"status":403,"message":"invalid id"})

# user authentication and token generation system 
# class UserRegistration(APIView):

#     def post(self,request):
#         serializer = UserAuth_Serializer(data = request.data)

#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({"status":403,"error":serializer.errors})

#         serializer.save()

#         user = User.objects.get(username = serializer.data['username'])
#         refresh = RefreshToken.for_user(user)

#         return Response({"status":200,"token":{
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#             },
#             "payload":serializer.data
#             }
#         )






# # sending data
# @api_view(["GET"])
# def testingForAuth(request):
#     Student_objs = Student.objects.all()
#     serializer = Student_Serializer(Student_objs,many=True)
#     return Response({"status":200,"payload":serializer.data})

# # getting data
# @api_view(["POST"])
# def testingForAuth_2(request):
#     data = request.data
#     serializer = Student_Serializer(data=request.data)

#     if not serializer.is_valid():
#         print("Invalid data")
#         return Response({"status":404,"message":"Invalid data","error":serializer.errors})
    
#     serializer.save()
#     print("testing in api_view")
#     # data = json.dumps()
#     return Response({"status":"created!! at JWT"})

# # updating data
# @api_view(["PATCH"])
# def testingForAuth_3(request,id):
#     try:
#         student_obj = Student.objects.get(id=id)
#         serializer = Student_Serializer(student_obj,data=request.data,partial=True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({"status":403,"error":serializer.errors})

#         serializer.save()
#         return Response({"status":200,"payload":serializer.data})
    
#     except Exception as e:
#         return Response({"status":403,"message":"invalid id"})