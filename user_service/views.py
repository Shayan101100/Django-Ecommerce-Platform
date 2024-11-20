
import email
from .models import UserInfo
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserInfoSerializer
# Create your views here.

class UserRegister(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserInfoSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                'id': user.id,
               'username': user.username,
               'email': user.enail,
               'fullname': user.fullname
               },status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class UserLogin(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = UserInfo.objects.filter(email=email).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
        
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "full_name": user.fullname,
            "phone_number": user.phone,
            "address": user.address,
            "city": user.city,
            "country": user.country,
            "postal_code": user.postal_code,
            "policy_agreement": user.policy_agreement,
            "policy_agreement_timestamp": user.policy_agreement_tiestamp
            }, status=status.HTTP_200_OK)