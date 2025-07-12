from rest_framework.response import Response
from rest_framework import status

def success_response(message, data=None, code=status.HTTP_200_OK):
    return Response({
        "status": "success",
        "message": message,
        "data": data
    }, status=code)

def error_response(message, code=status.HTTP_400_BAD_REQUEST):
    return Response({
        "status": "error",
        "message": message,
        "data": None
    }, status=code)
