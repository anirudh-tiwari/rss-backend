def jwt_response_payload_handler(token, user=None, request=None):
    a="avinash"
    return {
        'token': token,
        'user': a
    }