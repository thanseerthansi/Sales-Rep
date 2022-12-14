from itertools import product
import json
from operator import gt
from django.shortcuts import render

from sales.globalimport import *

# Create your views here.

order ='0'

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
#         except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

#     def delete(self,request):      
#         try:
#             id = self.request.data['id']
#             object = AttendanceModel.objects.filter(id=id)
#             if object.count():
#                 object.delete()
#                 return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
#             else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
#         except Exception as e :
#             return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

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
            if product: qs=qs.filter(product_name__icontains=product)
            return qs.order_by('-id')
        except : return None

    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            print("datd",self.request.data)
            # id = self.request.POST.get('id','') 
            try: id = self.request.data['id']
            except:id=''        
            if id:                 
                # if id.isdigit():
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                    
                    product_obj = ProductSerializer(product_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                product_obj = ProductSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            product_obj.is_valid(raise_exception=True)
            product_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):      
        try:
            id = self.request.data['id']
            object = ProductModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
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
            return qs.order_by('-id')
        except : return None

    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            print('tad',self.request.data)
            # id = self.request.POST.get('id','') 
            try: id = self.request.data['id']
            except:id=''
            # product = self.request.POST.get('product','') 
            try: product = self.request.data['product']
            except:product=''  
           
            if product:
                
                product_qss = ProductModel.objects.filter(id=product)
                print('product',product)  
                if product_qss.count():
                    product_qs = product_qss.first()     
                    print("product")        
            if id:                 
                # if id.isdigit():
                sub_product_qs = SubproductModel.objects.filter(id=id)
                if sub_product_qs.count():
                    sub_product_qs = sub_product_qs.first()
                    if not product:product_qs = sub_product_qs.product
                    
                    sub_product_obj = SubproductSerializer(sub_product_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                sub_product_obj = SubproductSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"              
                product_qss.update(have_subproduct=True)              
            sub_product_obj.is_valid(raise_exception=True)
            sub_product_obj.save(product=product_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):      
        try:
            id = self.request.data['id']
            object = SubproductModel.objects.filter(id=id)
            if object.count():
                product_id=object[0].product.id
                object.delete()
                print("productqs",product_id)
                product_qs = SubproductModel.objects.filter(product__id=product_id)
                if product_qs.count():
                    pass        
                else:
                    print("ookD")
                    ProductModel.objects.filter(id=product_id).update(have_subproduct=False)
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class OrderView(ListAPIView):
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        try:
            print("params",self.request.GET.get('is_delivered'))
            id = self.request.GET.get('id')
            employee = self.request.GET.get('employee')
            customer = self.request.GET.get('customer')
            is_delivered = self.request.GET.get('is_delivered')
            qs = OrderModel.objects.all()
            if id: qs = qs.filter(id=id)
            if employee: qs = qs.filter(employee__id=employee)
            if customer: qs = qs.filter(customer__id=customer)
            if is_delivered: qs = qs.filter(is_delivered=is_delivered)
            return qs.order_by('-id')
        except:return None
    
    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            print("data",self.request.data)
            userid = self.request.user.id
            try:id=self.request.data['id']
            except:id=''       
            try:customer=self.request.data['customer']
            except:customer=''       
            # try:employee=self.request.data['employee']
            # except:employee=''  
            # try:quantity = self.request.data['quantity'] 
            # except:quantity='' 
            # if quantity:
            #     try: product_id = self.request.data['product_id']
            #     except:product_id=''
            #     try: subproduct_id = self.request.data['subproduct_id']
            #     except:subproduct_id=''
            #     if product_id:
            #         product_obj = ProductModel.objects.filter(id=product_id)
            #         if product_obj.count:
            #             product
            #     elif subproduct_id:
            #         pass
            #     else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Product not found"})
            if customer:
                    customer_qss = UserModel.objects.filter(id=customer,is_customer=True)
                    if customer_qss.count():
                        customer_qs = customer_qss.first()     
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Customer not found"})       
            if userid:
                    employee_qss = UserModel.objects.filter(id=userid)
                    if employee_qss.count():
                        employee_qs = employee_qss.first()             
            if id:                 
                # if id.isdigit():
                order_qs = OrderModel.objects.filter(id=id)
                if order_qs.count():
                    order_qs = order_qs.first()
                    if not customer:customer_qs = order_qs.customer
                    if not employee_qs:employee_qs = order_qs.employee
                    order_obj = OrderSerializer(order_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})
            else:
                order_obj = OrderSerializer(data=self.request.data,partial=True)
                msg = "Created Successfully"
            order_obj.is_valid(raise_exception=True)
            order_data = order_obj.save(customer=customer_qs,employee=employee_qs)
            # print("oredrdat",order_data.id)
            global order
            order=order_data.id
            print("ordreidddd",order)
            return Response({"Status":status.HTTP_200_OK,"Message":msg,"Order_id":order_data.id})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):      
        try:
            id = self.request.data['id']    
            object = OrderModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})


class OrderedproductView(ListAPIView):
    serializer_class = OrderproductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        try:
            
            id = self.request.GET.get('id')
            product_id = self.request.GET.get('product_id')
            product = self.request.GET.get('product')
            order_id = self.request.GET.get('order_id')
            qs = OrderedProductModel.objects.all()
            if id: qs = qs.filter(id=id)
            if order_id : qs=qs.filter(order_id__id=order_id)
            if product_id: qs = qs.filter(product_id=product_id)
            if product: qs = qs.filter(product=product)
            return qs
        except:return None
    
    def post(self,request):   
        # isadmin = self.request.user.is_admin
        # superuser = self.request.user.is_superuser
        # if superuser == True  :
        try:
            
            # print("dfdgdata",self.request.data)
            # id = self.request.POST.get('id','') 
            for i in self.request.data:
                try:id=i['id']
                except:id=''
                # print("iiii",i)
                # try:order_id=i['order_id']
                # except:order_id=''
                # order_id = self.request.POST.get('order_id','')       
                # employee = self.request.POST.get('employee','')     
                if order:
                    # print("orderid",order)
                    order_qs = OrderModel.objects.filter(id=order)
                    if order_qs.count():
                        order_qs = order_qs.first()             
                # if employee:
                #         employee_qs = UserModel.objects.filter(id=employee)
                #         if employee_qs.count():
                #             employee_qs = employee_qs.first()             
                if id:                 
                    # if id.isdigit():
                    orderedproduct_qs = OrderedProductModel.objects.filter(id=id)
                    if orderedproduct_qs.count():
                        orderedproduct_qs = orderedproduct_qs.first()
                        # if not order:order_qs = orderedproduct_qs.order_id
                        # if not employee_qs:customer_qs = employee.employee
                        orderedproduct_obj = OrderproductSerializer(orderedproduct_qs,data=i,partial=True)
                        orderedproduct_obj.is_valid(raise_exception=True)
                        orderedproduct_obj.save(order_id=order_qs)
                        msg="updated successfuly"
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Record Found with given id"})                    
                    # else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Provide valid id "})  
                else:
                    try:quantity=i['quantity']
                    except:quantity=''
                    try:product_id=i['product_id']
                    except:product_id=''
                    # print("proid",product_id)
                    # for i in self.request.data: print("fgg",i['quantity'])
                    # print("prdk",self.request.data['quantity'])
                    try:subproduct_id=i['subproduct_id']
                    except:subproduct_id=''
                    # print("subid",subproduct_id)
                    if product_id:
                        # print("product")
                        product_qs = ProductModel.objects.filter(id=product_id,stock__gte=quantity)
                        if product_qs.count():
                            product_qs = product_qs.first()
                            product_qs.stock = int(product_qs.stock) - int(quantity)                     
                            product_qs.save()
                            # print("saved")
                            # print("stockaftr",product_qs['stock'])
                        else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"product not found"})
                    elif subproduct_id:
                        # print("subpro")
                        subproduct_qs = SubproductModel.objects.filter(id=subproduct_id,stock__gte=quantity)
                        if subproduct_qs.count():
                            subproduct_qs = subproduct_qs.first()
                            # print("stock",subproduct_qs.stock)
                            subproduct_qs.stock=int (subproduct_qs.stock) - int(quantity)
                            subproduct_qs.save()
                            # print("stockaftr",subproduct_qs.stock)
                        else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"Product not found in data"})
                    else:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Product not found"})
                    orderedproduct_obj = OrderproductSerializer(data=i,partial=True)
                    msg = "Added successfully"
                orderedproduct_obj.is_valid(raise_exception=True)
                orderedproduct_obj.save(order_id=order_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def delete(self,request):      
        try:
            id = self.request.data['id']    
            object = OrderedProductModel.objects.filter(id=id)
            if object.count():
                object.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Deleted successfully"})
            else:return Response({"Staus":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
        except Exception as e :
            return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})