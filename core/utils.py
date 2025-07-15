from typing import Any, Optional
from rest_framework.response import Response
from rest_framework import status


def success_response(
    message: str,
    data: Optional[Any] = None,
    code: int = status.HTTP_200_OK
) -> Response:
    """
    Return a standardized success response.
    
    Args:
        message (str): Message to describe the success.
        data (Any, optional): Optional data payload. Defaults to None.
        code (int, optional): HTTP status code. Defaults to 200.
    
    Returns:
        Response: DRF Response object with success structure.
    """
    return Response({
        "status": "success",
        "message": message,
        "data": data
    }, status=code)


def error_response(
    message: str,
    errors: Optional[Any] = None,
    code: int = status.HTTP_400_BAD_REQUEST
) -> Response:
    """
    Return a standardized error response.

    Args:
        message (str): Message to describe the error.
        errors (Any, optional): Optional error details (e.g., validation). Defaults to None.
        code (int, optional): HTTP status code. Defaults to 400.
    
    Returns:
        Response: DRF Response object with error structure.
    """
    return Response({
        "status": "error",
        "message": message,
        "errors": errors,
        "data": None
    }, status=code)
