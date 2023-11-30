from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apis.serializer import UserMasterSerializer
from apis.service.email_service import send_email
from apis.models import UserMaster
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(viewsets.ViewSet):

    @action(detail=False, url_path='register', methods=['POST'])
    def register_user(self, request):
        permission_classes = [AllowAny]
        serializer = UserMasterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(viewsets.ViewSet):
    queryset = UserMaster.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(detail=False, url_path='update', methods=['PUT'])
    def update_user_detail(self, request):
        user_id = request.data.get("user_id")
        if not user_id or user_id.strip() == "":
            return Response("User ID is required", status=status.HTTP_400_BAD_REQUEST)
        instance = get_object_or_404(UserMaster, pk=user_id)
        serializer = UserMasterSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, url_path='record', methods=['GET'])
    def get_user_record(self, request):
        user_id = request.query_params.get("user_id")
        order_by = request.query_params.get('order_by', 'created_at')
        page_number = request.query_params.get('page', 1)

        if user_id and user_id.strip() != "":
            user = get_object_or_404(UserMaster, pk=user_id)
            serializer = UserMasterSerializer(user)
            return Response(serializer.data)

        users = self.queryset.order_by(order_by)
        paginator = Paginator(users, per_page=20)
        paginated_users = paginator.get_page(page_number)
        serializer = UserMasterSerializer(paginated_users, many=True)
        response_data = {
            'count': paginator.count,
            'previous': paginated_users.previous_page_number() if paginated_users.has_previous() else None,
            'next': paginated_users.next_page_number() if paginated_users.has_next() else None,
            'total_pages': paginator.num_pages,
            'results': serializer.data,
        }
        return Response(response_data)

    @action(detail=False, url_path='delete', methods=['DELETE'])
    def delete_user(self, request):
        user_id = request.query_params.get("user_id")
        if not user_id or user_id.strip() == "":
            return Response("User ID is required", status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(UserMaster, pk=user_id)
        user.delete()
        return Response("User deleted successfully")
