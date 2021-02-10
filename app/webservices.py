from modernrpc.core import rpc_method
from modernrpc.core import REQUEST_KEY, ENTRY_POINT_KEY, PROTOCOL_KEY, HANDLER_KEY
from modernrpc.exceptions import RPCInternalError
from django.core.exceptions import ValidationError
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth import update_session_auth_hash, get_user_model, authenticate, login
import datetime
import time
from django.conf import settings
from app import models


@rpc_method
def login_custom(username,password,**kwargs):
    
    user = authenticate(username=username, password=password)

    request = kwargs.get(REQUEST_KEY)

    if user is None:
        raise RPCInternalError('Incorrect username or password.')
    
    login(request, user)

    if not request.session.exists(request.session.session_key):
        request.session.create()

    result = {"session":request.session.session_key}

    return result


