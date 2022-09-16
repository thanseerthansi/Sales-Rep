from itertools import product
from django.shortcuts import render

from sales.globalimport import *
# Create your views here.



# class AttendanceView(ListAPIView):
#     serializer_class = AttendanceSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     def get_queryset(self):
#         try:
#             id= self.request.GET.get('id')
#             staff= self.request.GET.get('staff')
#             qs = AttendanceModel.objects.all()
#             if id: qs=qs.filter(id=id)
#             if staff: qs=qs.filter(staff__id=staff)
#             return qs
#         except : return None

#     def post(self,request):   
#         # isadmin = self.request.user.is_admin
#         # superuser = self.request.user.is_superuser
#         # if superuser == True  :
#         try:
#             id = self.request.POST.get('id','') 
#             staff = self.request.POST.get('staff','')       
#             if staff:
#                     staff_qs = UserModel.objects.filter(staff=staff,is_employee=True)
#                     if staff_qs.count():
#                         statff_qs = staff_qs.first()             
#             if id:                 
#                 if id.isdigit():
#                     attendance_qs = AttendanceModel.objects.filter(id=id)
#                     if attendance_qs.count():
#                         attendance_qs = attendance_qs.first()
#                         if not staff:staff_qs = statff_qs.route
#                         attendance_obj = AttendanceSerializer(staff_qs,data=self.request.data,partial=True)
#                         msg = "Updated Successfully"
#                     else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
#                 else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
#             else:
#                 attendance_obj = AttendanceSerializer(data=self.request.data,partial=True)
#                 msg = "Created Successfully"
#             attendance_obj.is_valid(raise_exception=True)
#             attendance_obj.save(staff=statff_qs)
#             return Response({"Status":status.HTTP_200_OK,"Message":msg})
#         except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

#     def delete(self,request):      
#         try:
#             id = self.request.data['id']
#             object = AttendanceModel.objects.filter(id=id)
#             if object.count():
#                 object.delete()
#                 return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
#             else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
#         except Exception as e :
#             return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

class ProductView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        try:
            id= self.request.GET.get('id')
            product= self.request.GET.get('product')
            qs = ProductModel.objects.all()
            if id: qs=qs.filter(id=id)
            if product: qs=qs.filter(product_name=product)
            return qs
        except : return None

    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            id = self.request.POST.get('id','')          
            if id:                 
                if id.isdigit():
                    product_qs = ProductModel.objects.filter(id=id)
                    if product_qs.count():
                        product_qs = product_qs.first()
                       
                        product_obj = ProductSerializer(product_qs,data=self.request.data,partial=True)
                        msg = "Updated Successfully"
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                product_obj = ProductSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            product_obj.is_valid(raise_exception=True)
            product_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

    def delete(self,request):      
        try:
            id = self.request.data['id']
            object = ProductModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})
    
class SubproductView(ListAPIView):
    serializer_class = SubproductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        try:
            id= self.request.GET.get('id')
            product= self.request.GET.get('product')
            sub_product= self.request.GET.get('sub_product')
            qs = SubproductModel.objects.all().select_related('product')
            if id: qs=qs.filter(id=id)
            if product: qs=qs.filter(product__id=product)
            if sub_product: qs=qs.filter(product_name=sub_product)
            return qs
        except : return None

    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            id = self.request.POST.get('id','') 
            product = self.request.POST.get('product','')       
            if product:
                    product_qs = ProductModel.objects.filter(product=product)
                    if product_qs.count():
                        product_qs = product_qs.first()             
            if id:                 
                if id.isdigit():
                    sub_product_qs = SubproductModel.objects.filter(id=id)
                    if sub_product_qs.count():
                        sub_product_qs = sub_product_qs.first()
                        if not product:route_qs = sub_product_qs.route
                        sub_product_obj = SubproductSerializer(sub_product_qs,data=self.request.data,partial=True)
                        msg = "Updated Successfully"
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                sub_product_obj = SubproductSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            sub_product_obj.is_valid(raise_exception=True)
            sub_product_obj.save(product=product_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

    def delete(self,request):      
        try:
            id = self.request.data['id']
            object = SubproductModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

class OrderView(ListAPIView):
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            employee = self.request.GET.get('employee')
            customer = self.request.GET.get('customer')
            qs = OrderModel.objects.all()
            if id: qs = qs.filter(id=id)
            if employee: qs = qs.filter(employee__id=employee)
            if customer: qs = qs.filter(customer__id=customer)
            return qs
        except:return None
    
    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            id = self.request.POST.get('id','') 
            customer = self.request.POST.get('customer','')       
            employee = self.request.POST.get('employee','')       
            if customer:
                    customer_qs = UserModel.objects.filter(id=customer,is_employee=True)
                    if customer_qs.count():
                        customer_qs = customer_qs.first()             
            if employee:
                    employee_qs = UserModel.objects.filter(id=employee)
                    if employee_qs.count():
                        employee_qs = employee_qs.first()             
            if id:                 
                if id.isdigit():
                    order_qs = OrderModel.objects.filter(id=id)
                    if order_qs.count():
                        order_qs = order_qs.first()
                        if not customer:customer_qs = customer_qs.customer
                        if not employee_qs:customer_qs = employee.employee
                        order_obj = OrderSerializer(order_qs,data=self.request.data,partial=True)
                        msg = "Updated Successfully"
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                order_obj = OrderSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            order_obj.is_valid(raise_exception=True)
            order_data = order_obj.save(customer=customer,employee=employee)
            # print("oredrdat",order_data.id)
            if id:  
                pass
            else:
                # print("dataproduct",self.request.data['product'])
                for i in self.request.data['product']:
                    orderedproduct_obj = OrderproductSerializer(data=i,partial=True)
                    orderedproduct_obj.is_valid(raise_exception=True)
                    orderedproduct_obj.save(order_id = order_data)
            
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

    def delete(self,request):      
        try:
            id = self.request.data['id']    
            object = OrderModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})


class OrderedproductView(ListAPIView):
    serializer_class = OrderproductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            product_id = self.request.GET.get('product_id')
            product = self.request.GET.get('product')
            qs = OrderedProductModel.objects.all()
            if id: qs = qs.filter(id=id)
            if product_id: qs = qs.filter(product_id=product_id)
            if product: qs = qs.filter(product=product)
            return qs
        except:return None
    
    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            id = self.request.POST.get('id','') 
            order_id = self.request.POST.get('order_id','')       
            # employee = self.request.POST.get('employee','')       
            if order_id:
                    order_qs = OrderModel.objects.filter(id=order_id)
                    if order_qs.count():
                        order_qs = order_qs.first()             
            # if employee:
            #         employee_qs = UserModel.objects.filter(id=employee)
            #         if employee_qs.count():
            #             employee_qs = employee_qs.first()             
            if id:                 
                if id.isdigit():
                    orderedproduct_qs = OrderedProductModel.objects.filter(id=id)
                    if orderedproduct_qs.count():
                        orderedproduct_qs = orderedproduct_qs.first()
                        if not order_id:order_qs = orderedproduct_qs.order_id
                        # if not employee_qs:customer_qs = employee.employee
                        orderedproduct_obj = OrderproductSerializer(orderedproduct_qs,data=self.request.data,partial=True)
                        orderedproduct_obj.is_valid(raise_exception=True)
                        orderedproduct_obj.save(order_id=order_qs)
                        return Response({"Status":status.HTTP_200_OK,"Message":"Successfully updated"})
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})  
            else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})  
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})

    def delete(self,request):      
        try:
            id = self.request.data['id']    
            object = OrderedProductModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":e})