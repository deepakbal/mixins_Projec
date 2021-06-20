from django.shortcuts import render
from mixins_app.serializer import EmployeeSerializer
from mixins_app.models import Employee
from rest_framework import mixins,generics

class EmployeeListView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class =EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeeDetailsView(
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)



