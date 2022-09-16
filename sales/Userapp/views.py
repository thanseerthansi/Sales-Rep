


from sales.globalimport import *


# Create your views here.

class AreaView(ListAPIView):
    serializer_class = AreaSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        try:
            id= self.request.GET.get('id')
            area= self.request.GET.get('area')
            route = self.request.GET.get('route')
            qs = AreaModel.objects.all().select_related('route')
            if id: qs=qs.filter(id=id)
            if route : qs = qs.filter(route__id=route) 
            if area: qs=qs.filter(area_name=area)
            return qs
        except : return None

    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            # print("fdaat",self.request.data)
            # id = self.request.POST.get('id','') 
            try :id=self.request.data['id']                  
            except: id=''
            try :route=self.request.data['route']                  
            except: route=''
            # route = self.request.POST.get('route','')     
            # print("route",route)
            if route:
                # print("route",route) 
                route_qs = RouteModel.objects.filter(id=route)
                # print("ook",route_qs) 
                if route_qs.count():
                    # print("ookcount") 
                    route_qs = route_qs.first()   
                             
            if id:                 
                # if id.isdigit():
                area_qs = AreaModel.objects.filter(id=id)
                if area_qs.count():
                    area_qs = area_qs.first()
                    if not route:route_qs = area_qs.route
                    area_obj = AreaSerializer(area_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                area_obj = AreaSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            area_obj.is_valid(raise_exception=True)
            area_obj.save(route=route_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):      
        try:
            id = self.request.data['id']
            object = AreaModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class RouteView(ListAPIView):
    serializer_class = RouteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        try:
            # print("post",self.request.POST.get('id',''))
            # print("data",self.request.data)
            # print("get",self.request.GET.get('id'))
            id = self.request.GET.get('id','')
            qs = RouteModel.objects.all()
            if id: qs = qs.filter(id=id)
            return qs
        except : return None
    def post(self,request):   
        # isadmin = self.request.user.is_admin  
        superuser = self.request.user.is_superuser 
        if superuser == True  :
            try:
                id=''
                try : 
                    id=self.request.data['id']       
                except: id=''   
                print("fcgid",id)                 
                if id: 
                    # if id.isdigit():
                    route_qs = RouteModel.objects.filter(id=id)
                    if route_qs.count():
                        route_qs = route_qs.first()
                        print("okup")
                        route_obj = RouteSerializer(route_qs,data=self.request.data,partial=True)
                        msg = "Updated Successfully"
                        print("u[date")
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                    # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
                else:
                    route_obj = RouteSerializer(data=self.request.data,partial=True)
                    msg = "Created Successfully"
                    print("creat")
                route_obj.is_valid(raise_exception=True)
                route_obj.save()
                return Response({"Status":status.HTTP_200_OK,"Message":msg})
            except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
        else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Not Autherized"})

    def delete(self,request):
        superuser = self.request.user.is_superuser
        # print("iddd",self.request.data['id'])     
        try:
            if superuser == True:
                # print("iddd",self.request.data)
                id = self.request.data['id']
                object = RouteModel.objects.filter(id=id)
                if object.count():
                    object.delete()
                    return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
                else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:return Response({"Stauts":status.HTTP_400_BAD_REQUEST,"Message":"Not autherized"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})


class UserView(ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)
    
    def get_queryset(self):

        try:
            # print("post",self.request.POST.get('id',''))
            # print("data",self.request.data)
            # print("get",self.request.GET.get('employee'))
            id = self.request.GET.get('id')
            customer = self.request.GET.get("is_customer",'')#any value to filter customer
            # admin = self.request.GET.get("admin",'')#any value to filter all  partners
            user = self.request.GET.get('user') #to filter all employees 
            contact = self.request.GET.get('contact')
            employee = self.request.GET.get('is_employee')
            route = self.request.GET.get('route')
            userid = self.request.user.id
            qs = UserModel.objects.all()
            if id:qs = qs.filter(id=id)
            if user: qs = qs.filter(id=userid)
            # if admin: qs  = qs.filter(is_partner=True)
            if employee: qs  = qs.filter(is_employee=True)
            if customer: qs  = qs.filter(is_customer=True)
            if contact: qs=qs.filter(contact=contact)
            if route : qs=qs.filter(route__route=route)
            return qs
        except Exception as e:
            # print("euser",e)
            return None

    def post(self,request):
        userobj = ""
        try: id = self.request.data['id']
        except:id=''
        try: contact = self.request.data['contact']
        except:contact=''
        try: username = self.request.data['username']
        except:username=''
        try: route = self.request.data['route']
        except:route=''
        try: area = self.request.data['area']
        except:area=''
        try:
            print("daa",self.request.data)
            # id = self.request.POST.get("id","")
            # contact = self.request.POST.get("contact",'')
            # username = self.request.POST.get("username",'')
            mandatory = ['contact','username']
            data = Validate(self.request.data,mandatory)
            # print("contact",self.request.data['contact'])
            
            if route:
                route_qs = RouteModel.objects.filter(id=route)
                if route_qs.count():route_qs = route_qs.first()
            
            if area:
                area_qs = AreaModel.objects.filter(id=area)
                if area_qs.count():area_qs = area_qs.first()
            # print("userjname",self.request.POST.get('username'))
            print("okok")
            if id:
                # if id.isdigit():
                try:
                    print("datapost",self.request.data)
                    user = UserModel.objects.filter(id=id)
                    if user.count():
                        user = user.first()
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"User not found"})
                    if not route:route_qs = user.route
                    if not area: area_qs = user.area
                    if contact != user.contact:
                        contact_listqs = list(UserModel.objects.all().values_list('contact',flat=True)) 
                        if contact in contact_listqs:return Response({"Status":status.HTTP_208_ALREADY_REPORTED,"Message":"Number Already Exist"})
                    serializer = UserSerializer(user,data=request.data,partial= True)
                    serializer.is_valid(raise_exception=True)
                    email =  self.request.POST.get('email','')
                    if email:
                        msg = "user details and email updated successfully"
                        user_obj = serializer.save(password = make_password(email),route=route_qs)
                    else: 
                        msg = "User details updated successfully"
                        user_obj = serializer.save(route=route_qs,area=area_qs)
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})
                except Exception as e:
                    # print(f"Exception occured{e}")
                    if  user_obj : user_obj.delete()
                    else : pass
                    return  Response({
                        "Status":status.HTTP_400_BAD_REQUEST,
                        "Message":f"Excepction occured {e}"
                    })
                # else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Please provide valid user"})
            else:
                # print("id2",id)
                # mandatory = ['username','email']
                # data = Validate(self.request.data,mandatory)
                if contact:
                    contact_listqs = list(UserModel.objects.all().values_list('contact',flat=True)) 
                    if contact in contact_listqs:return Response({"Status":status.HTTP_208_ALREADY_REPORTED,"Message":"Number Already Exist"})
                if data == True:                
                    try:
                        serializer = UserSerializer(data=request.data, partial=True)
                        serializer.is_valid(raise_exception=True)
                        msg = "Created New User"
                        # user_obj = serializer.save(password=make_password(self.request.data['email']))    
                        user_obj = serializer.save(route=route_qs,area=area_qs)
                        # print("userserializer",user_obj)
                        return Response({"Status":status.HTTP_200_OK,"Message":msg})
                    except Exception as e :
                        return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
                else : return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":data})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    def delete(self,request):
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if isadmin==True or superuser == True:
        try:
            id = self.request.data['id']
            u_obj = UserModel.objects.filter(id=id)
            if u_obj.count():
                # print("obj",u_obj)
                u_obj.delete()
        
                return Response({"Status":status.HTTP_200_OK,"Message":"deleted successfully"})
            else: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No records with given id" })
            
        except Exception as e:
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
        # else: return Response({"Status":False,"Message":"Something went wrong"})
            
class WhoAmI(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self,request):
        try:
            return Response({
                "Status":1,
                "Data":self.request.user.username   
            })
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})

        
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # print("data",self.request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        # print(serializer)
        try:
            test = serializer.is_valid(raise_exception=True) 
            user = serializer.validated_data['user']

            
            token, created = Token.objects.get_or_create(user=user)
            # print("token",token.key)
            return Response({
                "Status":status.HTTP_200_OK,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
            })
        except Exception as e:
            # print("e",e)
            return Response({
                "Status":status.HTTP_400_BAD_REQUEST,
                "Message":"Incorrect Username or Password",
                "excepction":str(e),
            })

    


class otpLogin(ObtainAuthToken):
    serializer_class = otpLoginSerializer
    def post(self, request, *args, **kwargs):
        # print("data",self.request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(serializer)
        try:
            try:
                contact = self.request.data['contact']
            except: return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Contact required"})
            print("contact",self.request.data['contact'])
            test = serializer.is_valid(raise_exception=True) 
            # user = serializer.validated_data['user']
            user = UserModel.objects.filter(contact=contact).first()
            # if user.count():
                # user = user.first()
            print("user",user)
            token, created = Token.objects.get_or_create(user=user)
            # print("token",token.key)
            return Response({
                "Status":status.HTTP_200_OK,
                'token': "Token "+token.key,
                'user_id': user.pk,
                'username': user.username,
                'is_superuser':user.is_superuser,
                'is_customer':user.is_customer,
            })
            # else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Number Not found "})
        except Exception as e:
            # print("e",e)
            return Response({
                "Status":status.HTTP_400_BAD_REQUEST,
                "Message":"incorrect number",
                "excepction":str(e),
            })

    def get(self,request):
        try:
            contact = self.request.GET.get('contact')
            print("contat",contact)
            user_qs = UserModel.objects.filter(contact=contact,is_superuser="False")
            print(user_qs)
            if user_qs.count():return Response({"Status":status.HTTP_200_OK,"Message":"contact is user "})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Number not registered"})
        except Exception as e:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":str(e)})

class Logout(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
  
    def get(self,request):
        try:
            Data = Token.objects.get(user = self.request.user.id)
            Data.delete()
            # print("ok")
            return Response({"Status":status.HTTP_200_OK,"Message":"logout successfully"})
        except Exception as e:
            # print("e",e)
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
# class login(ListAPIView):
#     def get(self,request):
#         try:
#             print("data",self.request.data)
#             user = self.request.POST.get('username')
#             if user:
#                 userpbj = UserModel.objects.filter(username=user)
#                 print("usercount",userpbj.count())
#                 if userpbj.count():
 
#                     print("user",userpbj)
#                     return Response({
#                         "status":False,
#                         # "Data":userpbj
                
#                     })
#                 else:return Response({"status":False,"Messsage":"not found"})
#             else:return Response({"status":False,"Message":"user not found"})
#         except Exception as e:
#             return Response({"status":False,"Message":str(e)})
