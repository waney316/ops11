from rest_framework.response import Response

def JSONAPIResponse(code, data=None, message=None, request_id=None):
    return Response({
        "code": code,
        "data": data,
        "message": message,
        "request_id": request_id
    })

