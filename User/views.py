from rest_framework.views import APIView
from rest_framework.response import Response
from .models import user,Customer
from .serilizer import User_Serializer


# Create your views here.
class User_view(APIView):
    def post(self, request):
        user_data = User_Serializer(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.data)
        else:
            return Response("not exists")

    def get(self,request):
        dept_data = user.objects.all()
        serializer = User_Serializer(dept_data,many=True)
        return Response(serializer.data)

    def put(self, request, id):
        if  user.objects.filter(id=id):
            dept_data = user.objects.get(id=id)
            serializer = User_Serializer(instance=dept_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"Status": "not exists"})

    def delete(self, request, id):
        if id:
            if user.objects.filter(id=id).exists():
                dept_data = user.objects.get(id=id)
                dept_data.delete()
                return Response("deleted")
            else:

                return Response("not deleted")


