from django.shortcuts import render
#
# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
# class ProductView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({'msg':'inside product get'})
#
# # localhost:8000/morning
# # get
# # good morning
#
# class MorningView(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({'msg':'good morning'})
# class EveningView(APIView):
#     def get(self,request,*args,**kwarg):
#         return Response({'msg':'good evening'})
# #
# # class AddView(APIView):
# #     def get(self,request,*args,**kwargs):
# #         num1=int(input('enter the number 1'))
# #         num2=int(input('enter the number 2'))
# #         res=num1+num2
# #         return Response({'result':res})
# class AddView(APIView):
#     def post(self,request,*args,**kwargs):
#         n1=request.data.get('num1')
#         n2=request.data.get('num2')
#         res=int(n1)+int(n2)
#         return Response({'result':res})
#
#
#
#
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get('num'))
        res=n1**3
        return Response({'result':res})
class NumCheckView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num'))
        if n%2==0:
            res="number is even"
        else:
            res='number is odd'
        return Response({'result':res})
class NumfactView(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get('num'))
        fact=1
        for i in range(1,(n+1)):
            fact=fact*i
        return Response({'result':fact})
class WordcountView(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get('txt')
        words=txt.split(' ')
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response({'result':wc})
class AmstrongView(APIView):
    def post(self,request,args,*kwargs):
        n = int(request.data.get("num"))
        count = 0
        num = num1 = n
        sum = 0
        while n > 0:
            n = n // 10
            count  += 1
        #print("number of digits=", count)
        while num > 0:
            d = num % 10
            sum +=  pow(d, count)
            num = num // 10
        if num1 == sum:
            res = "armstrong"
        else:
            res = "not armstrong"
        return Response(data = res)

class PalindromeView(APIView):
    def post(self,request,args,*kwargs):
        n = request.data.get("num")
        str1 = n[::-1]
        #print(str1)
        if n == str1:
            res = "palindrome"
        else:
            res = "not palindrome"
        return Response(data = res)

class PrimeView(APIView):
    def post(self,request,args,*kwargs):
        n = int(request.data.get('num'))
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count = count + 1
        if count == 2:
            res = "prime number"
        else:
            res = "not a prime"
        return Response(data = res)