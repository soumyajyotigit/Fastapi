from uuid import uuid4


def generate_uuid():

    return str(uuid4())


def success_response(
    message: str,
    data=None
):

    return {
        "success": True,
        "message": message,
        "data": data
    }


def error_response(
    message: str,
    errors=None
):

    return {
        "success": False,
        "message": message,
        "errors": errors
    }