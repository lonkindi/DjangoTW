from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView

from hzapi.models import Anket

from hzapi.serializers import AnketSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginUser(APIView):
    """
    Класс для авторизации пользователей
    """
    def post(self, request, *args, **kwargs):
        """
        Авторизация методом POST
        """
        if {'username', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['username'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)
                    return JsonResponse({'Status': True, 'Token': token.key})
            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class GetAnketView(ListAPIView):
    """
    Класс для выдачи анкет
    """
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется авторизация!'}, status=403)
        state_param = request.query_params.get('state')
        if state_param is not None:
            queryset = Anket.objects.filter(state=state_param)
        else:
            queryset = Anket.objects.all()
        serializer_class = AnketSerializer(queryset, many=True)
        print(request.user.password)
        return Response(serializer_class.data)


class PutAnketView(APIView):
    """
    Класс для получения анкет с Яндекса
    """

    def post(self, request, *args, **kwargs):
        json_body = request.body  # json.loads(request.body)
        ext_id = request.headers['X-DELIVERY-ID']
        # print(ext_id)
        Anket.objects.create(external_id=ext_id, state=0, content=json_body)
        return JsonResponse({'Status': True, 'Error': 'None'}, status=200)

    def put(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Требуется авторизация!'}, status=403)
        id_item = request.query_params.get('id')
        state_item = request.query_params.get('state')
        if (id_item is not None) and (state_item is not None):
            Anket.objects.filter(external_id=id_item).update(state=state_item)
            return JsonResponse({'Status': True, 'Error': 'None'}, status=200)
        else:
            return JsonResponse({'Status': False, 'Error': 'Необходима авторизация'}, status=500)
        # print('json_body = ', items[0].content[2])
