import requests
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from member.pagination import PostPagination
from member.serializers import MyUserSerializer, UserCreateSerializer, TalingLoginSerializer
from utils.access_token_test import access_token_test, debug_token

MyUser = get_user_model()

##
# view 는 '사용제에게 제공될 데이터를 보는 것을 의미한다.
#   '데이터가 어떻게 보이는가?' 에 대한 것은 필요하지 않다.
#   '어떤 데이터가 보일것인가?' 에 집중해야한다.
##

class TalingSignUp(APIView):
    serializer_class = UserCreateSerializer
    # permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TalingLogin(APIView):
    serializer_class = TalingLoginSerializer

    def post(self, request, format=None):
        print('hello')
        serializer = TalingLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            token_key = serializer.validated_data


        return Response({'token': token_key})

    # def post(self, request):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #
    #     user = MyUser.objects.get(username=username)
    #     print(password)
    #     print(user.password)
    #     # if password != user.password:
    #     #     return Response('비밀번호가 일치하지 않습니다.')
    #
    #     token, created = user.get_user_token(user.pk)
    #     print(token)
    #
    #     return Response({'token': token.key})


class FaceBookLogin(APIView):
    def get(self, request):
        access_token = access_token_test(request)
        print(access_token)
        debug_result = debug_token(access_token)
        print(debug_result)

        def get_user_info(user_id, token):
            url_user_info = 'https://graph.facebook.com/v2.9/{user_id}'.format(user_id=user_id)
            url_user_info_params = {
                'access_token': token,
                'fields': ','.join([
                    'id',
                    'name',
                    'email',
                    'picture',
                ])
            }
            response = requests.get(url_user_info, params=url_user_info_params)
            result = response.json()
            print(result)
            return result

        user_info = get_user_info(user_id=debug_result['data']['user_id'], token=access_token)
        user = MyUser.objects.get_or_create_facebook_user(user_info)
        token, created = user.get_user_token(user.pk)
        return Response({'token': token.key})


class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    pagination_class = PostPagination


class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


# class MyUserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     ViewSet
#         - MyUserList + MyUserDetail = MyUserViewSet
#         - URL 구조는 기본 관례에 따라 자동으로 설정된다.
#     """
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserSerializer