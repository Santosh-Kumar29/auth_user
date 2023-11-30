import json

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api_gateway import service


class UserGateway(viewsets.ViewSet):

    @action(detail=False, url_path='register', methods=['POST'])
    def register(self, request):
        response = service.register_user(request)
        return Response(json.loads(response.text), status=response.status_code)

    @action(detail=False, url_path='update', methods=['POST'])
    def update_user(self, request):
        response = service.update_user(request)
        return Response(json.loads(response.text), status=response.status_code)

    @action(detail=False, url_path='record', methods=['POST'])
    def user_record(self, request):
        user_id = request.query_params.get("user_id")
        response = service.user_record(request, user_id)
        return Response(json.loads(response.text), status=response.status_code)

    @action(detail=False, url_path='delete', methods=['POST'])
    def user_delete(self, request):
        user_id = request.query_params.get("user_id")
        response = service.user_delete(request, user_id)
        return Response(json.loads(response.text), status=response.status_code)


class UserJwtToken(viewsets.ViewSet):

    @action(detail=False, url_path='generate/token', methods=['POST'])
    def generate_token(self, request):
        response = service.generate_token(request)
        return Response(json.loads(response.text), status=response.status_code)
