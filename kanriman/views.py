from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class PingViewSet(GenericAPIView):
    #トークンの動作確認用。トークンに紐づくユーザ名を返します。
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(data={'username': request.user.username}, status=status.HTTP_200_OK)
