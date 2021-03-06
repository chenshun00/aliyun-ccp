# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RuntimeOptions(TeaModel):
    def __init__(self, autoretry=None, ignore_ssl=None, max_attempts=None, backoff_policy=None, backoff_period=None,
                 read_timeout=None, connect_timeout=None, http_proxy=None, https_proxy=None, no_proxy=None, max_idle_conns=None,
                 local_addr=None, socks_5proxy=None, socks_5net_work=None):
        # whether to try again
        self.autoretry = autoretry
        # ignore SSL validation
        self.ignore_ssl = ignore_ssl
        # maximum number of retries
        self.max_attempts = max_attempts
        # backoff policy
        self.backoff_policy = backoff_policy
        # backoff period
        self.backoff_period = backoff_period
        # read timeout
        self.read_timeout = read_timeout
        # connect timeout
        self.connect_timeout = connect_timeout
        # http proxy url
        self.http_proxy = http_proxy
        # https Proxy url
        self.https_proxy = https_proxy
        # agent blacklist
        self.no_proxy = no_proxy
        # maximum number of connections
        self.max_idle_conns = max_idle_conns
        # local addr
        self.local_addr = local_addr
        # SOCKS5 proxy
        self.socks_5proxy = socks_5proxy
        # SOCKS5 netWork
        self.socks_5net_work = socks_5net_work

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['autoretry'] = self.autoretry
        result['ignoreSSL'] = self.ignore_ssl
        result['maxAttempts'] = self.max_attempts
        result['backoffPolicy'] = self.backoff_policy
        result['backoffPeriod'] = self.backoff_period
        result['readTimeout'] = self.read_timeout
        result['connectTimeout'] = self.connect_timeout
        result['httpProxy'] = self.http_proxy
        result['httpsProxy'] = self.https_proxy
        result['noProxy'] = self.no_proxy
        result['maxIdleConns'] = self.max_idle_conns
        result['localAddr'] = self.local_addr
        result['socks5Proxy'] = self.socks_5proxy
        result['socks5NetWork'] = self.socks_5net_work
        return result

    def from_map(self, map={}):
        self.autoretry = map.get('autoretry')
        self.ignore_ssl = map.get('ignoreSSL')
        self.max_attempts = map.get('maxAttempts')
        self.backoff_policy = map.get('backoffPolicy')
        self.backoff_period = map.get('backoffPeriod')
        self.read_timeout = map.get('readTimeout')
        self.connect_timeout = map.get('connectTimeout')
        self.http_proxy = map.get('httpProxy')
        self.https_proxy = map.get('httpsProxy')
        self.no_proxy = map.get('noProxy')
        self.max_idle_conns = map.get('maxIdleConns')
        self.local_addr = map.get('localAddr')
        self.socks_5proxy = map.get('socks5Proxy')
        self.socks_5net_work = map.get('socks5NetWork')
        return self


class Config(TeaModel):
    def __init__(self, endpoint=None, domain_id=None, client_id=None, refresh_token=None, client_secret=None,
                 access_token=None, expire_time=None, protocol=None, type=None, security_token=None, access_key_id=None,
                 access_key_secret=None, nickname=None, user_agent=None):
        self.endpoint = endpoint
        self.domain_id = domain_id
        self.client_id = client_id
        self.refresh_token = refresh_token
        self.client_secret = client_secret
        self.access_token = access_token
        self.expire_time = expire_time
        self.protocol = protocol
        self.type = type
        self.security_token = security_token
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.nickname = nickname
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['endpoint'] = self.endpoint
        result['domainId'] = self.domain_id
        result['clientId'] = self.client_id
        result['refreshToken'] = self.refresh_token
        result['clientSecret'] = self.client_secret
        result['accessToken'] = self.access_token
        result['expireTime'] = self.expire_time
        result['protocol'] = self.protocol
        result['type'] = self.type
        result['securityToken'] = self.security_token
        result['accessKeyId'] = self.access_key_id
        result['accessKeySecret'] = self.access_key_secret
        result['nickname'] = self.nickname
        result['userAgent'] = self.user_agent
        return result

    def from_map(self, map={}):
        self.endpoint = map.get('endpoint')
        self.domain_id = map.get('domainId')
        self.client_id = map.get('clientId')
        self.refresh_token = map.get('refreshToken')
        self.client_secret = map.get('clientSecret')
        self.access_token = map.get('accessToken')
        self.expire_time = map.get('expireTime')
        self.protocol = map.get('protocol')
        self.type = map.get('type')
        self.security_token = map.get('securityToken')
        self.access_key_id = map.get('accessKeyId')
        self.access_key_secret = map.get('accessKeySecret')
        self.nickname = map.get('nickname')
        self.user_agent = map.get('userAgent')
        return self


class CancelLinkRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CancelLinkRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CancelLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ConfirmLinkRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ConfirmLinkRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ConfirmLinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ChangePasswordRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DefaultChangePasswordRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ChangePasswordModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SetPasswordRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DefaultSetPasswordRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SetPasswordModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class VerifyCodeRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = VerifyCodeRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VerifyCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = VerifyCodeResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetAccessTokenByLinkInfoRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAccessTokenByLinkInfoRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetAccessTokenByLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetCaptchaRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetCaptchaRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetCaptchaModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = Captcha()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetByLinkInfoRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoByUserIdRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetLinkInfoByUserIDRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetLinkInfoByUserIdModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = LinkInfoListResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetPublicKeyRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAppPublicKeyRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetPublicKeyModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetAppPublicKeyResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LinkRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountLinkRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LinkModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CheckExistRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileCheckExistRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CheckExistModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileCheckExistResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LoginRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileLoginRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class LoginModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class RegisterRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileRegisterRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class RegisterModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MobileSendSmsCodeRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileSendSmsCodeRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MobileSendSmsCodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = MobileSendSmsCodeResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AccountRevokeRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = RevokeRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AccountRevokeModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class AccountTokenRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = TokenRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AccountTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccountAccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AccessTokenResponse(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, default_drive_id=None, expire_time=None, expires_in=None,
                 refresh_token=None, role=None, token_type=None, user_id=None):
        # 用于调用业务接口的accessToken
        self.access_token = access_token
        # Default Drive ID
        self.default_drive_id = default_drive_id
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time
        # accessToken过期时间，单位秒
        self.expires_in = expires_in
        # 用于刷新accessToken
        self.refresh_token = refresh_token
        # 当前用户角色
        self.role = role
        # accessToken类型，Bearer
        self.token_type = token_type
        # 当前用户ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        self.validate_required(self.default_drive_id, 'default_drive_id')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.expires_in, 'expires_in')
        self.validate_required(self.refresh_token, 'refresh_token')
        self.validate_required(self.role, 'role')
        self.validate_required(self.token_type, 'token_type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['access_token'] = self.access_token
        result['default_drive_id'] = self.default_drive_id
        result['expire_time'] = self.expire_time
        result['expires_in'] = self.expires_in
        result['refresh_token'] = self.refresh_token
        result['role'] = self.role
        result['token_type'] = self.token_type
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.default_drive_id = map.get('default_drive_id')
        self.expire_time = map.get('expire_time')
        self.expires_in = map.get('expires_in')
        self.refresh_token = map.get('refresh_token')
        self.role = map.get('role')
        self.token_type = map.get('token_type')
        self.user_id = map.get('user_id')
        return self


class AccountAccessTokenResponse(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, avatar=None, data_pin_saved=None, data_pin_setup=None,
                 default_drive_id=None, exist_link=None, expire_time=None, expires_in=None, is_first_login=None, need_link=None,
                 nick_name=None, refresh_token=None, role=None, state=None, token_type=None, user_data=None, user_id=None,
                 user_name=None):
        # 用于调用业务接口的accessToken
        self.access_token = access_token
        # 当前用户头像
        self.avatar = avatar
        # 用户的数据密码是否保存服务端
        self.data_pin_saved = data_pin_saved
        # 用户的数据密码是否设置过
        self.data_pin_setup = data_pin_setup
        # Default Drive ID
        self.default_drive_id = default_drive_id
        # 当前用户已存在的登录方式
        self.exist_link = exist_link
        # accessToken过期时间，ISO时间
        self.expire_time = expire_time
        # accessToken过期时间，单位秒
        self.expires_in = expires_in
        # 用户是否为第一次登录
        self.is_first_login = is_first_login
        # 是否需要绑定
        self.need_link = need_link
        # 当前用户昵称
        self.nick_name = nick_name
        # 用于刷新accessToken
        self.refresh_token = refresh_token
        # 当前用户角色
        self.role = role
        # 临时权限，用于登录成功后设置密码
        self.state = state
        # accessToken类型，Bearer
        self.token_type = token_type
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 当前用户ID
        self.user_id = user_id
        # 当前用户名
        self.user_name = user_name

    def validate(self):
        self.validate_required(self.access_token, 'access_token')
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()
        self.validate_required(self.need_link, 'need_link')

    def to_map(self):
        result = {}
        result['access_token'] = self.access_token
        result['avatar'] = self.avatar
        result['data_pin_saved'] = self.data_pin_saved
        result['data_pin_setup'] = self.data_pin_setup
        result['default_drive_id'] = self.default_drive_id
        result['exist_link'] = []
        if self.exist_link is not None:
            for k in self.exist_link:
                result['exist_link'].append(k.to_map() if k else None)
        else:
            result['exist_link'] = None
        result['expire_time'] = self.expire_time
        result['expires_in'] = self.expires_in
        result['is_first_login'] = self.is_first_login
        result['need_link'] = self.need_link
        result['nick_name'] = self.nick_name
        result['refresh_token'] = self.refresh_token
        result['role'] = self.role
        result['state'] = self.state
        result['token_type'] = self.token_type
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.avatar = map.get('avatar')
        self.data_pin_saved = map.get('data_pin_saved')
        self.data_pin_setup = map.get('data_pin_setup')
        self.default_drive_id = map.get('default_drive_id')
        self.exist_link = []
        if map.get('exist_link') is not None:
            for k in map.get('exist_link'):
                temp_model = LinkInfo()
                temp_model = temp_model.from_map(k)
                self.exist_link.append(temp_model)
        else:
            self.exist_link = None
        self.expire_time = map.get('expire_time')
        self.expires_in = map.get('expires_in')
        self.is_first_login = map.get('is_first_login')
        self.need_link = map.get('need_link')
        self.nick_name = map.get('nick_name')
        self.refresh_token = map.get('refresh_token')
        self.role = map.get('role')
        self.state = map.get('state')
        self.token_type = map.get('token_type')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class AccountLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, detail=None, extra=None, identity=None, status=None, type=None, user_id=None):
        # 账号信息
        self.detail = detail
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 状态
        self.status = status
        # 认证类型
        self.type = type
        # 绑定的user_id
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['detail'] = self.detail
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['status'] = self.status
        result['type'] = self.type
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.detail = map.get('detail')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.status = map.get('status')
        self.type = map.get('type')
        self.user_id = map.get('user_id')
        return self


class AuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, login_type=None, redirect_uri=None, response_type=None, scope=None,
                 state=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type
        # 回调地址, 此处填写创建App时填写的回调地址
        self.redirect_uri = redirect_uri
        # 返回类型, 只能填写code
        self.response_type = response_type
        # 申请的权限列表, 默认为所有权限
        self.scope = scope
        # 用户自定义字段，会在鉴权成功后的callback带回
        self.state = state

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.response_type, 'response_type')

    def to_map(self):
        result = {}
        result['ClientID'] = self.client_id
        result['LoginType'] = self.login_type
        result['RedirectUri'] = self.redirect_uri
        result['ResponseType'] = self.response_type
        result['Scope'] = []
        if self.scope is not None:
            for k in self.scope:
                result['Scope'].append(k)
        else:
            result['Scope'] = None
        result['State'] = self.state
        return result

    def from_map(self, map={}):
        self.client_id = map.get('ClientID')
        self.login_type = map.get('LoginType')
        self.redirect_uri = map.get('RedirectUri')
        self.response_type = map.get('ResponseType')
        self.scope = []
        if map.get('Scope') is not None:
            for k in map.get('Scope'):
                self.scope.append(k)
        else:
            self.scope = None
        self.state = map.get('State')
        return self


class BaseCCPFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, size=None, starred=None, status=None, streams_info=None, streams_url_info=None,
                 thumbnail=None, trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None):
        # category
        self.category = category
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.streams_info = streams_info
        # @Deprecated streams url info
        self.streams_url_info = streams_url_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['streams_url_info'] = self.streams_url_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.streams_url_info = map.get('streams_url_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class BaseDriveResponse(TeaModel):
    """
    Base drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
        self.used_size = map.get('used_size')
        return self


class BaseOSSFileResponse(TeaModel):
    """
    Base file response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        return self


class BaseShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # permissions
        self.permissions = permissions
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k)
        else:
            result['permissions'] = None
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = []
        if map.get('permissions') is not None:
            for k in map.get('permissions'):
                self.permissions.append(k)
        else:
            self.permissions = None
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                temp_model = temp_model.from_map(k)
                self.share_policy.append(temp_model)
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class BatchSubResponse(TeaModel):
    """
    *
    """
    def __init__(self, body=None, id=None, status=None):
        # body 子请求的返回结果，可参考对于子请求文档 json 字符串
        self.body = body
        # id 请求带过来的id, 可以跟 request 进行关联
        self.id = id
        # status 子请求的返回状态码，可参考对于子请求文档
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['body'] = self.body
        result['id'] = self.id
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.body = map.get('body')
        self.id = map.get('id')
        self.status = map.get('status')
        return self


class CCPBatchResponse(TeaModel):
    """
    batch operation response
    """
    def __init__(self, responses=None):
        # responses 返回结果合集
        self.responses = responses

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['responses'].append(k.to_map() if k else None)
        else:
            result['responses'] = None
        return result

    def from_map(self, map={}):
        self.responses = []
        if map.get('responses') is not None:
            for k in map.get('responses'):
                temp_model = BatchSubResponse()
                temp_model = temp_model.from_map(k)
                self.responses.append(temp_model)
        else:
            self.responses = None
        return self


class CCPCompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, size=None, starred=None, status=None, streams_info=None, streams_url_info=None,
                 thumbnail=None, trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None):
        # category
        self.category = category
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.streams_info = streams_info
        # @Deprecated streams url info
        self.streams_url_info = streams_url_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['streams_url_info'] = self.streams_url_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.streams_url_info = map.get('streams_url_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CCPCopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # DomainID
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class CCPCreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(self, domain_id=None, drive_id=None, encrypt_mode=None, exist=None, file_id=None, file_name=None,
                 parent_file_id=None, part_info_list=None, rapid_upload=None, status=None, streams_upload_info=None, type=None,
                 upload_id=None):
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # exist
        # type: boolean
        self.exist = exist
        # file_id
        self.file_id = file_id
        # file_name
        self.file_name = file_name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # part_info_list
        self.part_info_list = part_info_list
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload
        # status
        self.status = status
        # streams_upload_info
        self.streams_upload_info = streams_upload_info
        # type
        self.type = type
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.file_name:
            self.validate_max_length(self.file_name, 'file_name', 255)
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['exist'] = self.exist
        result['file_id'] = self.file_id
        result['file_name'] = self.file_name
        result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['rapid_upload'] = self.rapid_upload
        result['status'] = self.status
        result['streams_upload_info'] = self.streams_upload_info
        result['type'] = self.type
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.exist = map.get('exist')
        self.file_id = map.get('file_id')
        self.file_name = map.get('file_name')
        self.parent_file_id = map.get('parent_file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.rapid_upload = map.get('rapid_upload')
        self.status = map.get('status')
        self.streams_upload_info = map.get('streams_upload_info')
        self.type = map.get('type')
        self.upload_id = map.get('upload_id')
        return self


class CCPDeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class CCPDeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['deleted_file_id_list'] = []
        if self.deleted_file_id_list is not None:
            for k in self.deleted_file_id_list:
                result['deleted_file_id_list'].append(k)
        else:
            result['deleted_file_id_list'] = None
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.deleted_file_id_list = []
        if map.get('deleted_file_id_list') is not None:
            for k in map.get('deleted_file_id_list'):
                self.deleted_file_id_list.append(k)
        else:
            self.deleted_file_id_list = None
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        return self


class CCPGetAsyncTaskResponse(TeaModel):
    """
    Get AsyncTask Response
    """
    def __init__(self, async_task_id=None, message=None, state=None):
        # async_task_id
        # type:string
        self.async_task_id = async_task_id
        # message
        self.message = message
        # state
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['message'] = self.message
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.message = map.get('message')
        self.state = map.get('state')
        return self


class CCPGetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, size=None, streams_url=None, url=None):
        # expiration
        self.expiration = expiration
        # method
        self.method = method
        # size
        self.size = size
        # streams url info
        self.streams_url = streams_url
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['method'] = self.method
        result['size'] = self.size
        result['streams_url'] = self.streams_url
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.method = map.get('method')
        self.size = map.get('size')
        self.streams_url = map.get('streams_url')
        self.url = map.get('url')
        return self


class CCPGetFileByPathResponse(TeaModel):
    """
    根据路径获取文件元数据response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, size=None, starred=None, status=None, streams_info=None, streams_url_info=None,
                 thumbnail=None, trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None):
        # category
        self.category = category
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.streams_info = streams_info
        # @Deprecated streams url info
        self.streams_url_info = streams_url_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['streams_url_info'] = self.streams_url_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.streams_url_info = map.get('streams_url_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CCPGetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, size=None, starred=None, status=None, streams_info=None, streams_url_info=None,
                 thumbnail=None, trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None):
        # category
        self.category = category
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.streams_info = streams_info
        # @Deprecated streams url info
        self.streams_url_info = streams_url_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['streams_url_info'] = self.streams_url_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.streams_url_info = map.get('streams_url_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CCPGetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_id=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['create_at'] = self.create_at
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.create_at = map.get('create_at')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class CCPListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseCCPFileResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class CCPListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_id=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_id
        self.file_id = file_id
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker
        # upload_id
        self.upload_id = upload_id
        # uploaded_parts
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['file_id'] = self.file_id
        result['next_part_number_marker'] = self.next_part_number_marker
        result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        else:
            result['uploaded_parts'] = None
        return result

    def from_map(self, map={}):
        self.file_id = map.get('file_id')
        self.next_part_number_marker = map.get('next_part_number_marker')
        self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.uploaded_parts.append(temp_model)
        else:
            self.uploaded_parts = None
        return self


class CCPMoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # DomainID
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        return self


class CCPScanFileMetaResponse(TeaModel):
    """
    scan file meta response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseCCPFileResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class CCPSearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseCCPFileResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class CCPUpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(self, category=None, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, encrypt_mode=None,
                 file_extension=None, file_id=None, hidden=None, image_media_metadata=None, labels=None, meta=None, name=None,
                 parent_file_id=None, size=None, starred=None, status=None, streams_info=None, streams_url_info=None,
                 thumbnail=None, trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, user_meta=None,
                 video_media_metadata=None):
        # category
        self.category = category
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # DomainID
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_extension
        self.file_extension = file_extension
        # file_id
        self.file_id = file_id
        # Hidden
        # type: boolean
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # Size
        self.size = size
        # starred
        # type: boolean
        self.starred = starred
        # status
        self.status = status
        self.streams_info = streams_info
        # @Deprecated streams url info
        self.streams_url_info = streams_url_info
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_extension'] = self.file_extension
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['size'] = self.size
        result['starred'] = self.starred
        result['status'] = self.status
        result['streams_info'] = self.streams_info
        result['streams_url_info'] = self.streams_url_info
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_extension = map.get('file_extension')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaResponse()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.size = map.get('size')
        self.starred = map.get('starred')
        self.status = map.get('status')
        self.streams_info = map.get('streams_info')
        self.streams_url_info = map.get('streams_url_info')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaResponse()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CancelLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, temporary_token=None):
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        self.temporary_token = map.get('temporary_token')
        return self


class Captcha(TeaModel):
    """
    *
    """
    def __init__(self, captcha=None, captcha_format=None, captcha_id=None):
        # 图片验证码，base64格式
        self.captcha = captcha
        # 图片格式
        self.captcha_format = captcha_format
        # 图片验证码ID
        self.captcha_id = captcha_id

    def validate(self):
        self.validate_required(self.captcha, 'captcha')
        self.validate_required(self.captcha_format, 'captcha_format')
        self.validate_required(self.captcha_id, 'captcha_id')

    def to_map(self):
        result = {}
        result['captcha'] = self.captcha
        result['captcha_format'] = self.captcha_format
        result['captcha_id'] = self.captcha_id
        return result

    def from_map(self, map={}):
        self.captcha = map.get('captcha')
        self.captcha_format = map.get('captcha_format')
        self.captcha_id = map.get('captcha_id')
        return self


class ConfirmLinkRequest(TeaModel):
    """
    *
    """
    def __init__(self, temporary_token=None):
        # 待绑定的临时token，此token只能访问绑定、取消绑定接口
        self.temporary_token = temporary_token

    def validate(self):
        self.validate_required(self.temporary_token, 'temporary_token')

    def to_map(self):
        result = {}
        result['temporary_token'] = self.temporary_token
        return result

    def from_map(self, map={}):
        self.temporary_token = map.get('temporary_token')
        return self


class CorsRule(TeaModel):
    """
    *
    """
    def __init__(self, allowed_header=None, allowed_method=None, allowed_origin=None, expose_header=None,
                 max_age_seconds=None):
        # AllowedHeader
        self.allowed_header = allowed_header
        # AllowedMethod
        self.allowed_method = allowed_method
        # AllowedOrigin
        self.allowed_origin = allowed_origin
        # ExposeHeader
        self.expose_header = expose_header
        # MaxAgeSeconds
        self.max_age_seconds = max_age_seconds

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['allowed_header'] = []
        if self.allowed_header is not None:
            for k in self.allowed_header:
                result['allowed_header'].append(k)
        else:
            result['allowed_header'] = None
        result['allowed_method'] = []
        if self.allowed_method is not None:
            for k in self.allowed_method:
                result['allowed_method'].append(k)
        else:
            result['allowed_method'] = None
        result['allowed_origin'] = []
        if self.allowed_origin is not None:
            for k in self.allowed_origin:
                result['allowed_origin'].append(k)
        else:
            result['allowed_origin'] = None
        result['expose_header'] = []
        if self.expose_header is not None:
            for k in self.expose_header:
                result['expose_header'].append(k)
        else:
            result['expose_header'] = None
        result['max_age_seconds'] = self.max_age_seconds
        return result

    def from_map(self, map={}):
        self.allowed_header = []
        if map.get('allowed_header') is not None:
            for k in map.get('allowed_header'):
                self.allowed_header.append(k)
        else:
            self.allowed_header = None
        self.allowed_method = []
        if map.get('allowed_method') is not None:
            for k in map.get('allowed_method'):
                self.allowed_method.append(k)
        else:
            self.allowed_method = None
        self.allowed_origin = []
        if map.get('allowed_origin') is not None:
            for k in map.get('allowed_origin'):
                self.allowed_origin.append(k)
        else:
            self.allowed_origin = None
        self.expose_header = []
        if map.get('expose_header') is not None:
            for k in map.get('expose_header'):
                self.expose_header.append(k)
        else:
            self.expose_header = None
        self.max_age_seconds = map.get('max_age_seconds')
        return self


class CreateDriveResponse(TeaModel):
    """
    Create drive response
    """
    def __init__(self, domain_id=None, drive_id=None):
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        return self


class CreateShareResponse(TeaModel):
    """
    Create share response
    """
    def __init__(self, domain_id=None, share_id=None):
        # domain_id
        self.domain_id = domain_id
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.share_id = map.get('share_id')
        return self


class DefaultChangePasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, encrypted_key=None, new_password=None, phone_number=None, phone_region=None,
                 state=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 新密码，必须包含数字和字母，长度8-20个字符
        self.new_password = new_password
        # 手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['encrypted_key'] = self.encrypted_key
        result['new_password'] = self.new_password
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.encrypted_key = map.get('encrypted_key')
        self.new_password = map.get('new_password')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.state = map.get('state')
        return self


class DefaultSetPasswordRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, encrypted_key=None, new_password=None, state=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
        self.new_password = new_password
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.encrypted_key, 'encrypted_key')
        self.validate_required(self.new_password, 'new_password')
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['encrypted_key'] = self.encrypted_key
        result['new_password'] = self.new_password
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.encrypted_key = map.get('encrypted_key')
        self.new_password = map.get('new_password')
        self.state = map.get('state')
        return self


class DeleteDriveResponse(TeaModel):
    """
    delete drive response
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DeviceAuthorizeRequest(TeaModel):
    """
    *
    """
    def __init__(self, client_id=None, device_info=None, device_name=None, login_type=None, scope=None):
        # Client ID, 此处填写创建App时返回的AppID
        self.client_id = client_id
        # 设备信息，用于用户识别设备
        self.device_info = device_info
        # 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
        self.device_name = device_name
        # 鉴权方式，目前支持ding,ram鉴权
        self.login_type = login_type
        # 申请的权限列表, 默认为所有权限
        self.scope = scope

    def validate(self):
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.device_name, 'device_name')

    def to_map(self):
        result = {}
        result['ClientID'] = self.client_id
        result['DeviceInfo'] = self.device_info
        result['DeviceName'] = self.device_name
        result['LoginType'] = self.login_type
        result['Scope'] = []
        if self.scope is not None:
            for k in self.scope:
                result['Scope'].append(k)
        else:
            result['Scope'] = None
        return result

    def from_map(self, map={}):
        self.client_id = map.get('ClientID')
        self.device_info = map.get('DeviceInfo')
        self.device_name = map.get('DeviceName')
        self.login_type = map.get('LoginType')
        self.scope = []
        if map.get('Scope') is not None:
            for k in map.get('Scope'):
                self.scope.append(k)
        else:
            self.scope = None
        return self


class FileDeltaResponse(TeaModel):
    """
    the file op info
    """
    def __init__(self, current_category=None, file=None, file_id=None, op=None):
        self.current_category = current_category
        self.file = file
        self.file_id = file_id
        self.op = op

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = {}
        result['current_category'] = self.current_category
        if self.file is not None:
            result['file'] = self.file.to_map()
        else:
            result['file'] = None
        result['file_id'] = self.file_id
        result['op'] = self.op
        return result

    def from_map(self, map={}):
        self.current_category = map.get('current_category')
        if map.get('file') is not None:
            temp_model = BaseCCPFileResponse()
            self.file = temp_model.from_map(map['file'])
        else:
            self.file = None
        self.file_id = map.get('file_id')
        self.op = map.get('op')
        return self


class GetAccessTokenByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, extra=None, identity=None, type=None):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 认证类型
        self.type = type

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class GetAppPublicKeyRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None):
        # App ID
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        return self


class GetByLinkInfoRequest(TeaModel):
    """
    *
    """
    def __init__(self, extra=None, identity=None, type=None):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 认证类型
        self.type = type

    def validate(self):
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class GetCaptchaRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None):
        # App ID, 当前访问的App
        self.app_id = app_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        return self


class GetDriveResponse(TeaModel):
    """
    Get drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
        self.used_size = map.get('used_size')
        return self


class GetLastCursorResponse(TeaModel):
    """
    get last file op cursor response
    """
    def __init__(self, cursor=None):
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cursor'] = self.cursor
        return result

    def from_map(self, map={}):
        self.cursor = map.get('cursor')
        return self


class GetLinkInfoByUserIDRequest(TeaModel):
    """
    *
    """
    def __init__(self, user_id=None):
        # user ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.user_id = map.get('user_id')
        return self


class GetPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, key_pair_id=None, public_key=None):
        # App ID
        self.app_id = app_id
        self.key_pair_id = key_pair_id
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['key_pair_id'] = self.key_pair_id
        result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.key_pair_id = map.get('key_pair_id')
        self.public_key = map.get('public_key')
        return self


class GetShareResponse(TeaModel):
    """
    Get share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # permissions
        self.permissions = permissions
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k)
        else:
            result['permissions'] = None
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = []
        if map.get('permissions') is not None:
            for k in map.get('permissions'):
                self.permissions.append(k)
        else:
            self.permissions = None
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                temp_model = temp_model.from_map(k)
                self.share_policy.append(temp_model)
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class ImageMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, district=None, exif=None, faces=None, height=None,
                 location=None, province=None, story_image_score=None, time=None, township=None, width=None):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # district
        self.district = district
        # exif json string
        self.exif = exif
        # faces json string
        self.faces = faces
        # height
        self.height = height
        # location
        self.location = location
        # province
        self.province = province
        # story_image_score
        self.story_image_score = story_image_score
        # time
        self.time = time
        # township
        self.township = township
        # width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['exif'] = self.exif
        result['faces'] = self.faces
        result['height'] = self.height
        result['location'] = self.location
        result['province'] = self.province
        result['story_image_score'] = self.story_image_score
        result['time'] = self.time
        result['township'] = self.township
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.exif = map.get('exif')
        self.faces = map.get('faces')
        self.height = map.get('height')
        self.location = map.get('location')
        self.province = map.get('province')
        self.story_image_score = map.get('story_image_score')
        self.time = map.get('time')
        self.township = map.get('township')
        self.width = map.get('width')
        return self


class LinkInfo(TeaModel):
    """
    *
    """
    def __init__(self, extra=None, identity=None, type=None):
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 当前用户已存在的登录标识
        self.identity = identity
        # 当前用户已存在的登录方式
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.type = map.get('type')
        return self


class LinkInfoListResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # items
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = LinkInfoResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        return self


class LinkInfoResponse(TeaModel):
    """
    *
    """
    def __init__(self, authentication_type=None, created_at=None, domain_id=None, extra=None, identity=None,
                 last_login_time=None, status=None, user_id=None):
        # 认证类型
        self.authentication_type = authentication_type
        # 创建时间
        self.created_at = created_at
        # Domain ID
        self.domain_id = domain_id
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra
        # 唯一身份标识
        self.identity = identity
        # 最后登录时间
        self.last_login_time = last_login_time
        # 状态
        self.status = status
        # 用户ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.authentication_type, 'authentication_type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['authentication_type'] = self.authentication_type
        result['created_at'] = self.created_at
        result['domain_id'] = self.domain_id
        result['extra'] = self.extra
        result['identity'] = self.identity
        result['last_login_time'] = self.last_login_time
        result['status'] = self.status
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.authentication_type = map.get('authentication_type')
        self.created_at = map.get('created_at')
        self.domain_id = map.get('domain_id')
        self.extra = map.get('extra')
        self.identity = map.get('identity')
        self.last_login_time = map.get('last_login_time')
        self.status = map.get('status')
        self.user_id = map.get('user_id')
        return self


class ListDriveResponse(TeaModel):
    """
    list drive response
    """
    def __init__(self, items=None, next_marker=None):
        # Drive 列表
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDriveResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListFileDeltaResponse(TeaModel):
    """
    list file op response
    """
    def __init__(self, cursor=None, has_more=None, items=None):
        # cursor
        self.cursor = cursor
        # has_more
        self.has_more = has_more
        # items
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cursor'] = self.cursor
        result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.cursor = map.get('cursor')
        self.has_more = map.get('has_more')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = FileDeltaResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        return self


class ListShareResponse(TeaModel):
    """
    List share response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseShareResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoreFileResponse(TeaModel):
    """
    List storage file
    """
    def __init__(self, items=None, next_marker=None):
        # items
        # file list
        self.items = items
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreFile()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoreResponse(TeaModel):
    """
    List storage
    """
    def __init__(self, items=None):
        # items
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = StoreItemResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        return self


class LoginByCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, access_token=None, app_id=None, auth_code=None, type=None):
        # 鉴权后返回的accessToken，淘宝登录需要此字段
        self.access_token = access_token
        # App ID, 当前访问的App
        self.app_id = app_id
        # 鉴权后返回的AuthCode，支付宝登录需要此字段
        self.auth_code = auth_code
        # 鉴权类型，淘宝、支付宝
        self.type = type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['access_token'] = self.access_token
        result['app_id'] = self.app_id
        result['auth_code'] = self.auth_code
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.access_token = map.get('access_token')
        self.app_id = map.get('app_id')
        self.auth_code = map.get('auth_code')
        self.type = map.get('type')
        return self


class MobileCheckExistRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, phone_number=None, phone_region=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        return self


class MobileCheckExistResponse(TeaModel):
    """
    *
    """
    def __init__(self, is_exist=None, phone_number=None, phone_region=None):
        # 当前手机号是否存在
        self.is_exist = is_exist
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region

    def validate(self):
        self.validate_required(self.is_exist, 'is_exist')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['is_exist'] = self.is_exist
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        return result

    def from_map(self, map={}):
        self.is_exist = map.get('is_exist')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        return self


class MobileLoginRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, auto_register=None, captcha_id=None, captcha_text=None, encrypted_key=None,
                 password=None, phone_number=None, phone_region=None, sms_code=None, sms_code_id=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 是否自动注册用户，使用密码登录此参数不生效
        self.auto_register = auto_register
        # 图片验证码ID, 密码登录需要此参数
        self.captcha_id = captcha_id
        # 用户输入的验证码值, 密码登录需要此参数
        self.captcha_text = captcha_text
        # AES-256对称加密密钥，通过App公钥加密后传输
        self.encrypted_key = encrypted_key
        # 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
        self.password = password
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容，使用密码登录此参数不生效
        self.sms_code = sms_code
        # 短信验证码ID，使用密码登录此参数不生效
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['auto_register'] = self.auto_register
        result['captcha_id'] = self.captcha_id
        result['captcha_text'] = self.captcha_text
        result['encrypted_key'] = self.encrypted_key
        result['password'] = self.password
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.auto_register = map.get('auto_register')
        self.captcha_id = map.get('captcha_id')
        self.captcha_text = map.get('captcha_text')
        self.encrypted_key = map.get('encrypted_key')
        self.password = map.get('password')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        return self


class MobileRegisterRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, phone_number=None, phone_region=None, sms_code=None, sms_code_id=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 待查询的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容
        self.sms_code = sms_code
        # 短信验证码ID
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        return self


class MobileSendSmsCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, captcha_id=None, captcha_text=None, phone_number=None, phone_region=None,
                 type=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 图片验证码ID
        self.captcha_id = captcha_id
        # 用户输入的验证码值
        self.captcha_text = captcha_text
        # 待发送验证短信的手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 验证码用途, 可下发: login、register、change_password
        self.type = type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['captcha_id'] = self.captcha_id
        result['captcha_text'] = self.captcha_text
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.captcha_id = map.get('captcha_id')
        self.captcha_text = map.get('captcha_text')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.type = map.get('type')
        return self


class MobileSendSmsCodeResponse(TeaModel):
    """
    *
    """
    def __init__(self, sms_code_id=None):
        # 短信验证码ID
        self.sms_code_id = sms_code_id

    def validate(self):
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        result['sms_code_id'] = self.sms_code_id
        return result

    def from_map(self, map={}):
        self.sms_code_id = map.get('sms_code_id')
        return self


class OSSCompleteFileResponse(TeaModel):
    """
    complete file response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None, crc=None):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url
        # crc
        self.crc = crc

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        result['crc'] = self.crc
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        self.crc = map.get('crc')
        return self


class OSSCopyFileResponse(TeaModel):
    """
    文件拷贝 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # drive_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSCreateFileResponse(TeaModel):
    """
    Create file response
    """
    def __init__(self, domain_id=None, drive_id=None, file_path=None, part_info_list=None, share_id=None, type=None,
                 upload_id=None):
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # part_info_list
        self.part_info_list = part_info_list
        # share_id
        self.share_id = share_id
        # type
        self.type = type
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9]{1,50}')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['type'] = self.type
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.type = map.get('type')
        self.upload_id = map.get('upload_id')
        return self


class OSSDeleteFileResponse(TeaModel):
    """
    删除文件 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSDeleteFilesResponse(TeaModel):
    """
    批量删除文件 response
    """
    def __init__(self, deleted_file_id_list=None, domain_id=None, drive_id=None, share_id=None):
        # deleted_file_id_list
        self.deleted_file_id_list = deleted_file_id_list
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['deleted_file_id_list'] = []
        if self.deleted_file_id_list is not None:
            for k in self.deleted_file_id_list:
                result['deleted_file_id_list'].append(k)
        else:
            result['deleted_file_id_list'] = None
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.deleted_file_id_list = []
        if map.get('deleted_file_id_list') is not None:
            for k in map.get('deleted_file_id_list'):
                self.deleted_file_id_list.append(k)
        else:
            self.deleted_file_id_list = None
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlResponse(TeaModel):
    """
    获取download url response
    """
    def __init__(self, expiration=None, method=None, url=None):
        # expiration
        self.expiration = expiration
        # method
        self.method = method
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['method'] = self.method
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.method = map.get('method')
        self.url = map.get('url')
        return self


class OSSGetFileResponse(TeaModel):
    """
    获取文件元数据response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        return self


class OSSGetSecureUrlResponse(TeaModel):
    """
    获取secure url response
    """
    def __init__(self, expiration=None, url=None):
        # expiration
        self.expiration = expiration
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['expiration'] = self.expiration
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.expiration = map.get('expiration')
        self.url = map.get('url')
        return self


class OSSGetUploadUrlResponse(TeaModel):
    """
    Get UploadUrl Response
    """
    def __init__(self, create_at=None, domain_id=None, drive_id=None, file_path=None, part_info_list=None,
                 upload_id=None):
        # created_at
        self.create_at = create_at
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['create_at'] = self.create_at
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.create_at = map.get('create_at')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class OSSListFileResponse(TeaModel):
    """
    List file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class OSSListUploadedPartResponse(TeaModel):
    """
    获取签名 response
    """
    def __init__(self, file_path=None, next_part_number_marker=None, upload_id=None, uploaded_parts=None):
        # file_path
        self.file_path = file_path
        # next_part_number_marker
        self.next_part_number_marker = next_part_number_marker
        # upload_id
        self.upload_id = upload_id
        # uploaded_parts
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['file_path'] = self.file_path
        result['next_part_number_marker'] = self.next_part_number_marker
        result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        else:
            result['uploaded_parts'] = None
        return result

    def from_map(self, map={}):
        self.file_path = map.get('file_path')
        self.next_part_number_marker = map.get('next_part_number_marker')
        self.upload_id = map.get('upload_id')
        self.uploaded_parts = []
        if map.get('uploaded_parts') is not None:
            for k in map.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.uploaded_parts.append(temp_model)
        else:
            self.uploaded_parts = None
        return self


class OSSMoveFileResponse(TeaModel):
    """
    文件移动 response
    """
    def __init__(self, async_task_id=None, domain_id=None, drive_id=None, file_path=None, share_id=None):
        # async_task_id
        self.async_task_id = async_task_id
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # drive_id
        self.share_id = share_id

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z-]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[a-z0-9A-Z]+')

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSSearchFileResponse(TeaModel):
    """
    search file response
    """
    def __init__(self, items=None, next_marker=None):
        # items
        self.items = items
        # next_marker
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseOSSFileResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class OSSUpdateFileMetaResponse(TeaModel):
    """
    更新文件元数据 response
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_type=None, crc_64hash=None,
                 created_at=None, description=None, domain_id=None, download_url=None, drive_id=None, file_extension=None,
                 file_path=None, name=None, parent_file_path=None, share_id=None, size=None, status=None, thumbnail=None,
                 trashed_at=None, type=None, updated_at=None, upload_id=None, url=None):
        # Content Hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # content_type
        self.content_type = content_type
        # crc64_hash
        self.crc_64hash = crc_64hash
        # created_at
        self.created_at = created_at
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # download_url
        self.download_url = download_url
        # drive_id
        self.drive_id = drive_id
        # file_extension
        self.file_extension = file_extension
        # file_path
        self.file_path = file_path
        # name
        self.name = name
        # parent_file_id
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # Size
        self.size = size
        # status
        self.status = status
        # thumbnail
        self.thumbnail = thumbnail
        # trashed_at
        self.trashed_at = trashed_at
        # type
        self.type = type
        # updated_at
        self.updated_at = updated_at
        # upload_id
        self.upload_id = upload_id
        # url
        self.url = url

    def validate(self):
        if self.domain_id:
            self.validate_pattern(self.domain_id, 'domain_id', '[a-z0-9A-Z]+')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')
        if self.parent_file_path:
            self.validate_pattern(self.parent_file_path, 'parent_file_path', '[a-z0-9]{1,50}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_type'] = self.content_type
        result['crc64_hash'] = self.crc_64hash
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['download_url'] = self.download_url
        result['drive_id'] = self.drive_id
        result['file_extension'] = self.file_extension
        result['file_path'] = self.file_path
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['status'] = self.status
        result['thumbnail'] = self.thumbnail
        result['trashed_at'] = self.trashed_at
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        result['upload_id'] = self.upload_id
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_type = map.get('content_type')
        self.crc_64hash = map.get('crc64_hash')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.download_url = map.get('download_url')
        self.drive_id = map.get('drive_id')
        self.file_extension = map.get('file_extension')
        self.file_path = map.get('file_path')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.status = map.get('status')
        self.thumbnail = map.get('thumbnail')
        self.trashed_at = map.get('trashed_at')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        self.upload_id = map.get('upload_id')
        self.url = map.get('url')
        return self


class OSSVideoDRMLicenseResponse(TeaModel):
    """
    DRM License response
    """
    def __init__(self, data=None, states=None):
        # drm_data
        self.data = data
        # states
        self.states = states

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.states, 'states')

    def to_map(self):
        result = {}
        result['data'] = self.data
        result['states'] = self.states
        return result

    def from_map(self, map={}):
        self.data = map.get('data')
        self.states = map.get('states')
        return self


class OSSVideoDefinitionResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, frame_rate=None):
        # definition_list
        self.definition_list = definition_list
        # frame_rate
        self.frame_rate = frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['definition_list'] = []
        if self.definition_list is not None:
            for k in self.definition_list:
                result['definition_list'].append(k)
        else:
            result['definition_list'] = None
        result['frame_rate'] = self.frame_rate
        return result

    def from_map(self, map={}):
        self.definition_list = []
        if map.get('definition_list') is not None:
            for k in map.get('definition_list'):
                self.definition_list.append(k)
        else:
            self.definition_list = None
        self.frame_rate = map.get('frame_rate')
        return self


class OSSVideoTranscodeResponse(TeaModel):
    """
    转码接口response
    """
    def __init__(self, definition_list=None, duration=None, hls_time=None):
        # definition_list
        self.definition_list = definition_list
        # duration
        self.duration = duration
        # hls_time
        self.hls_time = hls_time

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['definition_list'] = []
        if self.definition_list is not None:
            for k in self.definition_list:
                result['definition_list'].append(k)
        else:
            result['definition_list'] = None
        result['duration'] = self.duration
        result['hls_time'] = self.hls_time
        return result

    def from_map(self, map={}):
        self.definition_list = []
        if map.get('definition_list') is not None:
            for k in map.get('definition_list'):
                self.definition_list.append(k)
        else:
            self.definition_list = None
        self.duration = map.get('duration')
        self.hls_time = map.get('hls_time')
        return self


class PreHashCheckSuccessResponse(TeaModel):
    """
    Pre hash check Response
    """
    def __init__(self, code=None, file_name=None, message=None, parent_file_id=None, pre_hash=None):
        # code
        self.code = code
        # file_name
        self.file_name = file_name
        # message
        self.message = message
        # parent_file_id
        self.parent_file_id = parent_file_id
        # pre_hash
        self.pre_hash = pre_hash

    def validate(self):
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['code'] = self.code
        result['file_name'] = self.file_name
        result['message'] = self.message
        result['parent_file_id'] = self.parent_file_id
        result['pre_hash'] = self.pre_hash
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.file_name = map.get('file_name')
        self.message = map.get('message')
        self.parent_file_id = map.get('parent_file_id')
        self.pre_hash = map.get('pre_hash')
        return self


class RevokeRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, refresh_token=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.refresh_token = map.get('refresh_token')
        return self


class SharePermissionPolicy(TeaModel):
    """
    *
    """
    def __init__(self, file_path=None, permission_inheritable=None, permission_list=None, permission_type=None):
        self.file_path = file_path
        self.permission_inheritable = permission_inheritable
        self.permission_list = permission_list
        self.permission_type = permission_type

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['file_path'] = self.file_path
        result['permission_inheritable'] = self.permission_inheritable
        result['permission_list'] = []
        if self.permission_list is not None:
            for k in self.permission_list:
                result['permission_list'].append(k)
        else:
            result['permission_list'] = None
        result['permission_type'] = self.permission_type
        return result

    def from_map(self, map={}):
        self.file_path = map.get('file_path')
        self.permission_inheritable = map.get('permission_inheritable')
        self.permission_list = []
        if map.get('permission_list') is not None:
            for k in map.get('permission_list'):
                self.permission_list.append(k)
        else:
            self.permission_list = None
        self.permission_type = map.get('permission_type')
        return self


class StoreFile(TeaModel):
    """
    *
    """
    def __init__(self, domain_id=None, name=None, parent_file_path=None, store_id=None, type=None):
        self.domain_id = domain_id
        self.name = name
        self.parent_file_path = parent_file_path
        self.store_id = store_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        result['name'] = self.name
        result['parent_file_path'] = self.parent_file_path
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        self.name = map.get('name')
        self.parent_file_path = map.get('parent_file_path')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class StoreItemResponse(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, customized_endpoint=None,
                 domain_id=None, endpoint=None, internal_endpoint=None, ownership=None, policy=None, role_arn=None,
                 store_id=None, type=None):
        # 全球加速域名
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 用户自定义绑定存储地址
        self.customized_endpoint = customized_endpoint
        self.domain_id = domain_id
        # 存储访问地址
        self.endpoint = endpoint
        # 内网存储地址
        self.internal_endpoint = internal_endpoint
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['customized_endpoint'] = self.customized_endpoint
        result['domain_id'] = self.domain_id
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.customized_endpoint = map.get('customized_endpoint')
        self.domain_id = map.get('domain_id')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class StreamInfo(TeaModel):
    """
    *
    """
    def __init__(self, crc_64hash=None, download_url=None, thumbnail=None, url=None):
        # crc64_hash
        self.crc_64hash = crc_64hash
        # download_url
        self.download_url = download_url
        # thumbnail
        self.thumbnail = thumbnail
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['crc64_hash'] = self.crc_64hash
        result['download_url'] = self.download_url
        result['thumbnail'] = self.thumbnail
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.crc_64hash = map.get('crc64_hash')
        self.download_url = map.get('download_url')
        self.thumbnail = map.get('thumbnail')
        self.url = map.get('url')
        return self


class StreamUploadInfo(TeaModel):
    """
    *
    """
    def __init__(self, part_info_list=None, pre_rapid_upload=None, rapid_upload=None, upload_id=None):
        # part_info_list
        self.part_info_list = part_info_list
        # pre_rapid_upload
        # type: boolean
        self.pre_rapid_upload = pre_rapid_upload
        # rapid_upload
        # type: boolean
        self.rapid_upload = rapid_upload
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['pre_rapid_upload'] = self.pre_rapid_upload
        result['rapid_upload'] = self.rapid_upload
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.pre_rapid_upload = map.get('pre_rapid_upload')
        self.rapid_upload = map.get('rapid_upload')
        self.upload_id = map.get('upload_id')
        return self


class TokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, grant_type=None, refresh_token=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 只能填refresh_token
        self.grant_type = grant_type
        # refresh token, 登录时返回的
        self.refresh_token = refresh_token

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.grant_type, 'grant_type')
        self.validate_required(self.refresh_token, 'refresh_token')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['grant_type'] = self.grant_type
        result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.grant_type = map.get('grant_type')
        self.refresh_token = map.get('refresh_token')
        return self


class UpdateDriveResponse(TeaModel):
    """
    Update drive response
    """
    def __init__(self, creator=None, description=None, domain_id=None, drive_id=None, drive_name=None,
                 drive_type=None, encrypt_data_access=None, encrypt_mode=None, owner=None, relative_path=None, status=None,
                 store_id=None, total_size=None, used_size=None):
        # Drive 创建者
        self.creator = creator
        # Drive 备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # Drive 类型
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        # Drive 所有者
        self.owner = owner
        # Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
        self.relative_path = relative_path
        # Drive 状态
        self.status = status
        # 存储 ID, domain的PathType为OSSPath时返回
        self.store_id = store_id
        # Drive 空间总量
        self.total_size = total_size
        # Drive 空间已使用量
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        result['used_size'] = self.used_size
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
        self.used_size = map.get('used_size')
        return self


class UpdateShareResponse(TeaModel):
    """
    Update share response
    """
    def __init__(self, created_at=None, creator=None, description=None, domain_id=None, drive_id=None,
                 expiration=None, expired=None, owner=None, permissions=None, share_file_path=None, share_id=None,
                 share_name=None, share_policy=None, status=None, updated_at=None):
        # created_at
        self.created_at = created_at
        # creator
        self.creator = creator
        # description
        self.description = description
        # domain_id
        self.domain_id = domain_id
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # expired
        self.expired = expired
        # owner
        self.owner = owner
        # permissions
        self.permissions = permissions
        # share_path
        self.share_file_path = share_file_path
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        self.share_policy = share_policy
        # status
        self.status = status
        # updated_at
        self.updated_at = updated_at

    def validate(self):
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['created_at'] = self.created_at
        result['creator'] = self.creator
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['expired'] = self.expired
        result['owner'] = self.owner
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k)
        else:
            result['permissions'] = None
        result['share_file_path'] = self.share_file_path
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.created_at = map.get('created_at')
        self.creator = map.get('creator')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.expired = map.get('expired')
        self.owner = map.get('owner')
        self.permissions = []
        if map.get('permissions') is not None:
            for k in map.get('permissions'):
                self.permissions.append(k)
        else:
            self.permissions = None
        self.share_file_path = map.get('share_file_path')
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                temp_model = temp_model.from_map(k)
                self.share_policy.append(temp_model)
        else:
            self.share_policy = None
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        return self


class UploadPartInfo(TeaModel):
    """
    *
    """
    def __init__(self, etag=None, part_number=None, part_size=None, upload_url=None):
        # etag
        self.etag = etag
        # PartNumber
        self.part_number = part_number
        # PartSize：
        self.part_size = part_size
        # upload_url
        self.upload_url = upload_url

    def validate(self):
        if self.part_number:
            self.validate_pattern(self.part_number, 'part_number', '[0-9]+')

    def to_map(self):
        result = {}
        result['etag'] = self.etag
        result['part_number'] = self.part_number
        result['part_size'] = self.part_size
        result['upload_url'] = self.upload_url
        return result

    def from_map(self, map={}):
        self.etag = map.get('etag')
        self.part_number = map.get('part_number')
        self.part_size = map.get('part_size')
        self.upload_url = map.get('upload_url')
        return self


class UrlInfo(TeaModel):
    """
    *
    """
    def __init__(self, download_url=None, thumbnail=None, url=None):
        # download_url
        self.download_url = download_url
        # thumbnail
        self.thumbnail = thumbnail
        # url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['download_url'] = self.download_url
        result['thumbnail'] = self.thumbnail
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.download_url = map.get('download_url')
        self.thumbnail = map.get('thumbnail')
        self.url = map.get('url')
        return self


class UserAuthentication(TeaModel):
    """
    *
    """
    def __init__(self, authentication_type=None, created_at=None, detail=None, domain_id=None, identity=None,
                 last_login_time=None, status=None, user_id=None, extra=None):
        # 认证类型
        self.authentication_type = authentication_type
        # 创建时间
        self.created_at = created_at
        # 详情
        self.detail = detail
        # Domain ID
        self.domain_id = domain_id
        # 唯一身份标识
        self.identity = identity
        # 最后登录时间
        self.last_login_time = last_login_time
        # 状态
        self.status = status
        # 用户ID
        self.user_id = user_id
        # 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
        self.extra = extra

    def validate(self):
        self.validate_required(self.authentication_type, 'authentication_type')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.detail, 'detail')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.identity, 'identity')
        self.validate_required(self.last_login_time, 'last_login_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['AuthenticationType'] = self.authentication_type
        result['CreatedAt'] = self.created_at
        result['Detail'] = self.detail
        result['DomainID'] = self.domain_id
        result['Identity'] = self.identity
        result['LastLoginTime'] = self.last_login_time
        result['Status'] = self.status
        result['UserID'] = self.user_id
        result['extra'] = self.extra
        return result

    def from_map(self, map={}):
        self.authentication_type = map.get('AuthenticationType')
        self.created_at = map.get('CreatedAt')
        self.detail = map.get('Detail')
        self.domain_id = map.get('DomainID')
        self.identity = map.get('Identity')
        self.last_login_time = map.get('LastLoginTime')
        self.status = map.get('Status')
        self.user_id = map.get('UserID')
        self.extra = map.get('extra')
        return self


class VerifyCodeRequest(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, phone_number=None, phone_region=None, sms_code=None, sms_code_id=None,
                 verify_type=None):
        # App ID, 当前访问的App
        self.app_id = app_id
        # 手机号
        self.phone_number = phone_number
        # 国家编号，默认86，不需要填+号，直接填数字
        self.phone_region = phone_region
        # 短信验证码内容
        self.sms_code = sms_code
        # 短信验证码ID
        self.sms_code_id = sms_code_id
        # 需要被校验内容的类型
        self.verify_type = verify_type

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.phone_number, 'phone_number')
        self.validate_required(self.sms_code, 'sms_code')
        self.validate_required(self.sms_code_id, 'sms_code_id')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['phone_number'] = self.phone_number
        result['phone_region'] = self.phone_region
        result['sms_code'] = self.sms_code
        result['sms_code_id'] = self.sms_code_id
        result['verify_type'] = self.verify_type
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.phone_number = map.get('phone_number')
        self.phone_region = map.get('phone_region')
        self.sms_code = map.get('sms_code')
        self.sms_code_id = map.get('sms_code_id')
        self.verify_type = map.get('verify_type')
        return self


class VerifyCodeResponse(TeaModel):
    """
    *
    """
    def __init__(self, state=None):
        # 修改密码的临时授权码
        self.state = state

    def validate(self):
        self.validate_required(self.state, 'state')

    def to_map(self):
        result = {}
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.state = map.get('state')
        return self


class VideoMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, district=None, duration=None, height=None,
                 location=None, province=None, time=None, township=None, width=None):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # district
        self.district = district
        # duration 单位 秒
        self.duration = duration
        # height
        self.height = height
        # location
        self.location = location
        # province
        self.province = province
        # time
        self.time = time
        # township
        self.township = township
        # width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['duration'] = self.duration
        result['height'] = self.height
        result['location'] = self.location
        result['province'] = self.province
        result['time'] = self.time
        result['township'] = self.township
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.duration = map.get('duration')
        self.height = map.get('height')
        self.location = map.get('location')
        self.province = map.get('province')
        self.time = map.get('time')
        self.township = map.get('township')
        self.width = map.get('width')
        return self


class AdminListStoresRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AdminListStoresRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AdminListStoresModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoresResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUserAccessTokenRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUserAccessTokenRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUserAccessTokenModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AccessTokenResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class AddStoreResponse(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, customized_endpoint=None,
                 domain_id=None, endpoint=None, internal_endpoint=None, ownership=None, policy=None, role_arn=None,
                 store_id=None, type=None):
        # 全球加速域名
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 用户自定义绑定存储地址
        self.customized_endpoint = customized_endpoint
        # domain ID
        self.domain_id = domain_id
        # 存储访问地址
        self.endpoint = endpoint
        # 内网存储地址
        self.internal_endpoint = internal_endpoint
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.domain_id, 'domain_id')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['customized_endpoint'] = self.customized_endpoint
        result['domain_id'] = self.domain_id
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.customized_endpoint = map.get('customized_endpoint')
        self.domain_id = map.get('domain_id')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class AdminListStoresRequest(TeaModel):
    """
    *
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class AppAccessStrategy(TeaModel):
    """
    *
    """
    def __init__(self, effect=None, except_app_id_list=None):
        self.effect = effect
        self.except_app_id_list = except_app_id_list

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['effect'] = self.effect
        result['except_app_id_list'] = []
        if self.except_app_id_list is not None:
            for k in self.except_app_id_list:
                result['except_app_id_list'].append(k)
        else:
            result['except_app_id_list'] = None
        return result

    def from_map(self, map={}):
        self.effect = map.get('effect')
        self.except_app_id_list = []
        if map.get('except_app_id_list') is not None:
            for k in map.get('except_app_id_list'):
                self.except_app_id_list.append(k)
        else:
            self.except_app_id_list = None
        return self


class AuthConfig(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, app_secret=None, callback_security=None, enable=None, endpoint=None,
                 enterprise_id=None):
        self.app_id = app_id
        self.app_secret = app_secret
        self.callback_security = callback_security
        self.enable = enable
        self.endpoint = endpoint
        self.enterprise_id = enterprise_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['app_secret'] = self.app_secret
        result['callback_security'] = self.callback_security
        result['enable'] = self.enable
        result['endpoint'] = self.endpoint
        result['enterprise_id'] = self.enterprise_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.app_secret = map.get('app_secret')
        self.callback_security = map.get('callback_security')
        self.enable = map.get('enable')
        self.endpoint = map.get('endpoint')
        self.enterprise_id = map.get('enterprise_id')
        return self


class BaseDomainResponse(TeaModel):
    """
    base domain response
    """
    def __init__(self, auth_alipay_app_id=None, auth_alipay_enable=None, auth_alipay_private_key=None,
                 auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None, auth_dingding_enable=None,
                 auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None, auth_ram_enable=None, created_at=None,
                 data_hash_name=None, description=None, domain_id=None, domain_name=None, event_filename_matches=None,
                 event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None, init_drive_enable=None,
                 init_drive_size=None, init_drive_store_id=None, path_type=None, published_app_access_strategy=None, sharable=None,
                 store_level=None, store_region_list=None, updated_at=None):
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = []
        if self.event_names is not None:
            for k in self.event_names:
                result['event_names'].append(k)
        else:
            result['event_names'] = None
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = []
        if self.store_region_list is not None:
            for k in self.store_region_list:
                result['store_region_list'].append(k)
        else:
            result['store_region_list'] = None
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = []
        if map.get('event_names') is not None:
            for k in map.get('event_names'):
                self.event_names.append(k)
        else:
            self.event_names = None
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = []
        if map.get('store_region_list') is not None:
            for k in map.get('store_region_list'):
                self.store_region_list.append(k)
        else:
            self.store_region_list = None
        self.updated_at = map.get('updated_at')
        return self


class CreateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(self, auth_alipay_app_id=None, auth_alipay_enable=None, auth_alipay_private_key=None,
                 auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None, auth_dingding_enable=None,
                 auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None, auth_ram_enable=None, created_at=None,
                 data_hash_name=None, description=None, domain_id=None, domain_name=None, event_filename_matches=None,
                 event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None, init_drive_enable=None,
                 init_drive_size=None, init_drive_store_id=None, path_type=None, published_app_access_strategy=None, sharable=None,
                 store_level=None, store_region_list=None, updated_at=None):
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = []
        if self.event_names is not None:
            for k in self.event_names:
                result['event_names'].append(k)
        else:
            result['event_names'] = None
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = []
        if self.store_region_list is not None:
            for k in self.store_region_list:
                result['store_region_list'].append(k)
        else:
            result['store_region_list'] = None
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = []
        if map.get('event_names') is not None:
            for k in map.get('event_names'):
                self.event_names.append(k)
        else:
            self.event_names = None
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = []
        if map.get('store_region_list') is not None:
            for k in map.get('store_region_list'):
                self.store_region_list.append(k)
        else:
            self.store_region_list = None
        self.updated_at = map.get('updated_at')
        return self


class GetAppPublicKeyResponse(TeaModel):
    """
    *
    """
    def __init__(self, app_id=None, public_key=None):
        # App ID
        self.app_id = app_id
        # RSA加密算法的公钥, PEM格式
        self.public_key = public_key

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.public_key, 'public_key')

    def to_map(self):
        result = {}
        result['app_id'] = self.app_id
        result['public_key'] = self.public_key
        return result

    def from_map(self, map={}):
        self.app_id = map.get('app_id')
        self.public_key = map.get('public_key')
        return self


class GetAppResponse(TeaModel):
    """
    *
    """
    def __init__(self, ali_owner_id=None, app_id=None, app_name=None, app_secret=None, created_at=None,
                 description=None, logo=None, provider=None, redirect_uri=None, scope=None, screenshots=None, stage=None,
                 type=None, updated_at=None):
        # App 拥有者
        self.ali_owner_id = ali_owner_id
        # App ID
        self.app_id = app_id
        # App名称
        self.app_name = app_name
        # App 秘钥
        self.app_secret = app_secret
        # App 创建时间
        self.created_at = created_at
        # App描述
        self.description = description
        # App图标
        self.logo = logo
        # App 提供方
        self.provider = provider
        # App回调地址
        self.redirect_uri = redirect_uri
        # App权限列表
        self.scope = scope
        # App 屏幕截图
        self.screenshots = screenshots
        # App 当前阶段
        self.stage = stage
        # App类型
        self.type = type
        # App 修改时间
        self.updated_at = updated_at

    def validate(self):
        self.validate_required(self.ali_owner_id, 'ali_owner_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_name, 'app_name')
        if self.app_name:
            self.validate_pattern(self.app_name, 'app_name', '[0-9a-zA-Z]+')
        self.validate_required(self.app_secret, 'app_secret')
        self.validate_required(self.created_at, 'created_at')
        self.validate_required(self.description, 'description')
        if self.description:
            self.validate_max_length(self.description, 'description', 128)
        self.validate_required(self.logo, 'logo')
        self.validate_required(self.provider, 'provider')
        self.validate_required(self.redirect_uri, 'redirect_uri')
        self.validate_required(self.scope, 'scope')
        self.validate_required(self.screenshots, 'screenshots')
        self.validate_required(self.stage, 'stage')
        self.validate_required(self.type, 'type')
        self.validate_required(self.updated_at, 'updated_at')

    def to_map(self):
        result = {}
        result['ali_owner_id'] = self.ali_owner_id
        result['app_id'] = self.app_id
        result['app_name'] = self.app_name
        result['app_secret'] = self.app_secret
        result['created_at'] = self.created_at
        result['description'] = self.description
        result['logo'] = self.logo
        result['provider'] = self.provider
        result['redirect_uri'] = self.redirect_uri
        result['scope'] = []
        if self.scope is not None:
            for k in self.scope:
                result['scope'].append(k)
        else:
            result['scope'] = None
        result['screenshots'] = []
        if self.screenshots is not None:
            for k in self.screenshots:
                result['screenshots'].append(k)
        else:
            result['screenshots'] = None
        result['stage'] = self.stage
        result['type'] = self.type
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.ali_owner_id = map.get('ali_owner_id')
        self.app_id = map.get('app_id')
        self.app_name = map.get('app_name')
        self.app_secret = map.get('app_secret')
        self.created_at = map.get('created_at')
        self.description = map.get('description')
        self.logo = map.get('logo')
        self.provider = map.get('provider')
        self.redirect_uri = map.get('redirect_uri')
        self.scope = []
        if map.get('scope') is not None:
            for k in map.get('scope'):
                self.scope.append(k)
        else:
            self.scope = None
        self.screenshots = []
        if map.get('screenshots') is not None:
            for k in map.get('screenshots'):
                self.screenshots.append(k)
        else:
            self.screenshots = None
        self.stage = map.get('stage')
        self.type = map.get('type')
        self.updated_at = map.get('updated_at')
        return self


class GetDomainResponse(TeaModel):
    """
    get domain response
    """
    def __init__(self, auth_alipay_app_id=None, auth_alipay_enable=None, auth_alipay_private_key=None,
                 auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None, auth_dingding_enable=None,
                 auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None, auth_ram_enable=None, created_at=None,
                 data_hash_name=None, description=None, domain_id=None, domain_name=None, event_filename_matches=None,
                 event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None, init_drive_enable=None,
                 init_drive_size=None, init_drive_store_id=None, path_type=None, published_app_access_strategy=None, sharable=None,
                 store_level=None, store_region_list=None, updated_at=None):
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = []
        if self.event_names is not None:
            for k in self.event_names:
                result['event_names'].append(k)
        else:
            result['event_names'] = None
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = []
        if self.store_region_list is not None:
            for k in self.store_region_list:
                result['store_region_list'].append(k)
        else:
            result['store_region_list'] = None
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = []
        if map.get('event_names') is not None:
            for k in map.get('event_names'):
                self.event_names.append(k)
        else:
            self.event_names = None
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = []
        if map.get('store_region_list') is not None:
            for k in map.get('store_region_list'):
                self.store_region_list.append(k)
        else:
            self.store_region_list = None
        self.updated_at = map.get('updated_at')
        return self


class GetUserAccessTokenRequest(TeaModel):
    """
    *
    """
    def __init__(self, role=None, user_id=None):
        # 角色
        self.role = role
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['role'] = self.role
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.role = map.get('role')
        self.user_id = map.get('user_id')
        return self


class ListAppsResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None, next_marker=None):
        # App 列表
        self.items = items
        # App 分批查询游标
        self.next_marker = next_marker

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = GetAppResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListDomainCORSRuleResponse(TeaModel):
    """
    list domain cors response
    """
    def __init__(self, cors_rule_list=None, domain_id=None):
        # cors rule 列表
        self.cors_rule_list = cors_rule_list
        # Domain ID
        self.domain_id = domain_id

    def validate(self):
        if self.cors_rule_list:
            for k in self.cors_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cors_rule_list'] = []
        if self.cors_rule_list is not None:
            for k in self.cors_rule_list:
                result['cors_rule_list'].append(k.to_map() if k else None)
        else:
            result['cors_rule_list'] = None
        result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.cors_rule_list = []
        if map.get('cors_rule_list') is not None:
            for k in map.get('cors_rule_list'):
                temp_model = CorsRule()
                temp_model = temp_model.from_map(k)
                self.cors_rule_list.append(temp_model)
        else:
            self.cors_rule_list = None
        self.domain_id = map.get('domain_id')
        return self


class ListDomainsResponse(TeaModel):
    """
    list domain response
    """
    def __init__(self, items=None, next_marker=None):
        # domain 列表
        self.items = items
        # 下次分页查询游标
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseDomainResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class ListStoresResponse(TeaModel):
    """
    *
    """
    def __init__(self, items=None):
        # Store 列表
        self.items = items

    def validate(self):
        self.validate_required(self.items, 'items')
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = Store()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        return self


class Store(TeaModel):
    """
    *
    """
    def __init__(self, accelerate_endpoint=None, base_path=None, bucket=None, customized_endpoint=None,
                 endpoint=None, internal_endpoint=None, ownership=None, policy=None, role_arn=None, store_id=None, type=None):
        # 全球加速域名
        self.accelerate_endpoint = accelerate_endpoint
        # 存储公共前缀
        self.base_path = base_path
        # bucket名称
        self.bucket = bucket
        # 用户自定义绑定存储地址
        self.customized_endpoint = customized_endpoint
        # 存储访问地址
        self.endpoint = endpoint
        # 内网存储地址
        self.internal_endpoint = internal_endpoint
        # 存储归属，system表示系统提供，custom表示使用自己的存储
        self.ownership = ownership
        # Policy授权,system类型store会将bucket权限授予当前云账号
        self.policy = policy
        # 访问Bucket的角色ARN
        self.role_arn = role_arn
        # store ID
        self.store_id = store_id
        # 存储类型，当前只支持oss
        self.type = type

    def validate(self):
        self.validate_required(self.bucket, 'bucket')
        self.validate_required(self.endpoint, 'endpoint')
        self.validate_required(self.ownership, 'ownership')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.store_id, 'store_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['accelerate_endpoint'] = self.accelerate_endpoint
        result['base_path'] = self.base_path
        result['bucket'] = self.bucket
        result['customized_endpoint'] = self.customized_endpoint
        result['endpoint'] = self.endpoint
        result['internal_endpoint'] = self.internal_endpoint
        result['ownership'] = self.ownership
        result['policy'] = self.policy
        result['role_arn'] = self.role_arn
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.accelerate_endpoint = map.get('accelerate_endpoint')
        self.base_path = map.get('base_path')
        self.bucket = map.get('bucket')
        self.customized_endpoint = map.get('customized_endpoint')
        self.endpoint = map.get('endpoint')
        self.internal_endpoint = map.get('internal_endpoint')
        self.ownership = map.get('ownership')
        self.policy = map.get('policy')
        self.role_arn = map.get('role_arn')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class UpdateDomainResponse(TeaModel):
    """
    create domain response
    """
    def __init__(self, auth_alipay_app_id=None, auth_alipay_enable=None, auth_alipay_private_key=None,
                 auth_config=None, auth_dingding_app_id=None, auth_dingding_app_secret=None, auth_dingding_enable=None,
                 auth_endpoint_enable=None, auth_ram_app_id=None, auth_ram_app_secret=None, auth_ram_enable=None, created_at=None,
                 data_hash_name=None, description=None, domain_id=None, domain_name=None, event_filename_matches=None,
                 event_mns_endpoint=None, event_mns_topic=None, event_names=None, event_role_arn=None, init_drive_enable=None,
                 init_drive_size=None, init_drive_store_id=None, path_type=None, published_app_access_strategy=None, sharable=None,
                 store_level=None, store_region_list=None, updated_at=None):
        # 支付宝 App Id
        self.auth_alipay_app_id = auth_alipay_app_id
        # 是否开启了支付宝认证
        self.auth_alipay_enable = auth_alipay_enable
        # 支付宝 App Secret
        self.auth_alipay_private_key = auth_alipay_private_key
        # 登录相关信息
        self.auth_config = auth_config
        # 钉钉 App Id
        self.auth_dingding_app_id = auth_dingding_app_id
        # 钉钉 App Secret
        self.auth_dingding_app_secret = auth_dingding_app_secret
        # 是否开启了钉钉认证
        self.auth_dingding_enable = auth_dingding_enable
        self.auth_endpoint_enable = auth_endpoint_enable
        # RAM App Id
        self.auth_ram_app_id = auth_ram_app_id
        # RAM App Secret
        self.auth_ram_app_secret = auth_ram_app_secret
        # 是否开启了 RAM 认证
        self.auth_ram_enable = auth_ram_enable
        # Domain 创建时间
        self.created_at = created_at
        # 数据 Hash 算法
        self.data_hash_name = data_hash_name
        # Domain 描述
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # Domain 描述
        self.domain_name = domain_name
        # 事件通知 MNS 匹配文件名
        self.event_filename_matches = event_filename_matches
        # 事件通知 MNS Endpoint
        self.event_mns_endpoint = event_mns_endpoint
        # 事件通知 MNS Topic
        self.event_mns_topic = event_mns_topic
        # 事件名列表
        self.event_names = event_names
        # 事件通知 Role Arn
        self.event_role_arn = event_role_arn
        # 是否开启了自动初始化 Drive
        self.init_drive_enable = init_drive_enable
        # 自动初始化 Drive 大小
        self.init_drive_size = init_drive_size
        # 自动初始化 Drive 所用 Store ID
        self.init_drive_store_id = init_drive_store_id
        # Domain 类型
        self.path_type = path_type
        self.published_app_access_strategy = published_app_access_strategy
        # 是否开启了分享
        self.sharable = sharable
        # 存储级别
        self.store_level = store_level
        # 存储 Region 列表
        self.store_region_list = store_region_list
        # Domain 更新时间
        self.updated_at = updated_at

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        result = {}
        result['auth_alipay_app_id'] = self.auth_alipay_app_id
        result['auth_alipay_enable'] = self.auth_alipay_enable
        result['auth_alipay_private_key'] = self.auth_alipay_private_key
        result['auth_config'] = self.auth_config
        result['auth_dingding_app_id'] = self.auth_dingding_app_id
        result['auth_dingding_app_secret'] = self.auth_dingding_app_secret
        result['auth_dingding_enable'] = self.auth_dingding_enable
        result['auth_endpoint_enable'] = self.auth_endpoint_enable
        result['auth_ram_app_id'] = self.auth_ram_app_id
        result['auth_ram_app_secret'] = self.auth_ram_app_secret
        result['auth_ram_enable'] = self.auth_ram_enable
        result['created_at'] = self.created_at
        result['data_hash_name'] = self.data_hash_name
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['domain_name'] = self.domain_name
        result['event_filename_matches'] = self.event_filename_matches
        result['event_mns_endpoint'] = self.event_mns_endpoint
        result['event_mns_topic'] = self.event_mns_topic
        result['event_names'] = []
        if self.event_names is not None:
            for k in self.event_names:
                result['event_names'].append(k)
        else:
            result['event_names'] = None
        result['event_role_arn'] = self.event_role_arn
        result['init_drive_enable'] = self.init_drive_enable
        result['init_drive_size'] = self.init_drive_size
        result['init_drive_store_id'] = self.init_drive_store_id
        result['path_type'] = self.path_type
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        else:
            result['published_app_access_strategy'] = None
        result['sharable'] = self.sharable
        result['store_level'] = self.store_level
        result['store_region_list'] = []
        if self.store_region_list is not None:
            for k in self.store_region_list:
                result['store_region_list'].append(k)
        else:
            result['store_region_list'] = None
        result['updated_at'] = self.updated_at
        return result

    def from_map(self, map={}):
        self.auth_alipay_app_id = map.get('auth_alipay_app_id')
        self.auth_alipay_enable = map.get('auth_alipay_enable')
        self.auth_alipay_private_key = map.get('auth_alipay_private_key')
        self.auth_config = map.get('auth_config')
        self.auth_dingding_app_id = map.get('auth_dingding_app_id')
        self.auth_dingding_app_secret = map.get('auth_dingding_app_secret')
        self.auth_dingding_enable = map.get('auth_dingding_enable')
        self.auth_endpoint_enable = map.get('auth_endpoint_enable')
        self.auth_ram_app_id = map.get('auth_ram_app_id')
        self.auth_ram_app_secret = map.get('auth_ram_app_secret')
        self.auth_ram_enable = map.get('auth_ram_enable')
        self.created_at = map.get('created_at')
        self.data_hash_name = map.get('data_hash_name')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.domain_name = map.get('domain_name')
        self.event_filename_matches = map.get('event_filename_matches')
        self.event_mns_endpoint = map.get('event_mns_endpoint')
        self.event_mns_topic = map.get('event_mns_topic')
        self.event_names = []
        if map.get('event_names') is not None:
            for k in map.get('event_names'):
                self.event_names.append(k)
        else:
            self.event_names = None
        self.event_role_arn = map.get('event_role_arn')
        self.init_drive_enable = map.get('init_drive_enable')
        self.init_drive_size = map.get('init_drive_size')
        self.init_drive_store_id = map.get('init_drive_store_id')
        self.path_type = map.get('path_type')
        if map.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(map['published_app_access_strategy'])
        else:
            self.published_app_access_strategy = None
        self.sharable = map.get('sharable')
        self.store_level = map.get('store_level')
        self.store_region_list = []
        if map.get('store_region_list') is not None:
            for k in map.get('store_region_list'):
                self.store_region_list.append(k)
        else:
            self.store_region_list = None
        self.updated_at = map.get('updated_at')
        return self


class CreateDriveRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteDriveRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteDriveModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetDriveRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDefaultDriveRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDefaultDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDefaultDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListDrivesRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListMyDrivesRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListMyDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListMyDrivesModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateDriveRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateDriveRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateDriveModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateDriveResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CompleteFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCompleteFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CompleteFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCompleteFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CopyFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCopyFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CopyFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCopyFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCreateFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSCreateFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSDeleteFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteFileModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDownloadUrlRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetDownloadUrlRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetDownloadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetDownloadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetSecureUrlRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetSecureUrlRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetSecureUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetSecureUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUploadUrlRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetUploadUrlRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUploadUrlModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSGetUploadUrlResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSListFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSListFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUploadedPartsRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSListUploadedPartRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUploadedPartsModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSListUploadedPartResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MoveFileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSMoveFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class MoveFileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSMoveFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoDefinitionRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoDefinitionRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoDefinitionModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoDefinitionResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoLicenseRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoDRMLicenseRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoLicenseModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoDRMLicenseResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoM3u8RequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoM3U8Request()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoM3u8Model(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['body'] = self.body
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.body = map.get('body')
        return self


class VideoTranscodeRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoTranscodeRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class VideoTranscodeModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = OSSVideoTranscodeResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateShareRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateShareRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateShareModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateShareResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteShareRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteShareRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteShareModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetShareRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetShareModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetShareResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListShareRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListShareRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListShareModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListShareResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateShareRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateShareRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateShareModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateShareResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListStorefileRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoreFileRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListStorefileModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListStoreFileResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class BaseCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, drive_id=None, part_info_list=None, upload_id=None):
        # drive_id
        self.drive_id = drive_id
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class BaseCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(self, content_md_5=None, content_type=None, name=None, part_info_list=None, size=None, type=None):
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # Name
        self.name = name
        # part_info_list
        self.part_info_list = part_info_list
        # Size
        self.size = size
        # Type
        self.type = type

    def validate(self):
        self.validate_required(self.content_md_5, 'content_md_5')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.name, 'name')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.size, 'size')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['name'] = self.name
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['size'] = self.size
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.name = map.get('name')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.size = map.get('size')
        self.type = map.get('type')
        return self


class BaseGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, part_info_list=None, upload_id=None):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # upload_part_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        return self


class BaseListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class BaseMediaResponse(TeaModel):
    """
    *
    """
    def __init__(self, address_line=None, city=None, country=None, district=None, height=None, location=None,
                 province=None, time=None, township=None, width=None):
        # address_line
        self.address_line = address_line
        # city
        self.city = city
        # country
        self.country = country
        # district
        self.district = district
        # height
        self.height = height
        # location
        self.location = location
        # province
        self.province = province
        # time
        self.time = time
        # township
        self.township = township
        # width
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['address_line'] = self.address_line
        result['city'] = self.city
        result['country'] = self.country
        result['district'] = self.district
        result['height'] = self.height
        result['location'] = self.location
        result['province'] = self.province
        result['time'] = self.time
        result['township'] = self.township
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.address_line = map.get('address_line')
        self.city = map.get('city')
        self.country = map.get('country')
        self.district = map.get('district')
        self.height = map.get('height')
        self.location = map.get('location')
        self.province = map.get('province')
        self.time = map.get('time')
        self.township = map.get('township')
        self.width = map.get('width')
        return self


class BaseMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, new_name=None, overwrite=None):
        # drive_id
        self.drive_id = drive_id
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        return self


class BatchSubRequest(TeaModel):
    """
    *
    """
    def __init__(self, body=None, headers=None, id=None, method=None, url=None):
        # body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
        self.body = body
        # headers 请求头，表示body传入数据的类型
        self.headers = headers
        # id 用于request 和 response关联， 不允许重复
        self.id = id
        # method
        self.method = method
        # url 子请求的api path路径， 可参考对于子请求文档
        self.url = url

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.method, 'method')
        self.validate_required(self.url, 'url')

    def to_map(self):
        result = {}
        result['body'] = self.body
        result['headers'] = self.headers
        result['id'] = self.id
        result['method'] = self.method
        result['url'] = self.url
        return result

    def from_map(self, map={}):
        self.body = map.get('body')
        self.headers = map.get('headers')
        self.id = map.get('id')
        self.method = map.get('method')
        self.url = map.get('url')
        return self


class CCPBatchRequest(TeaModel):
    """
    批处理
    """
    def __init__(self, requests=None, resource=None):
        # Requests 请求合集
        self.requests = requests
        # 支持的资源类型
        self.resource = resource

    def validate(self):
        self.validate_required(self.requests, 'requests')
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()
        self.validate_required(self.resource, 'resource')

    def to_map(self):
        result = {}
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        else:
            result['requests'] = None
        result['resource'] = self.resource
        return result

    def from_map(self, map={}):
        self.requests = []
        if map.get('requests') is not None:
            for k in map.get('requests'):
                temp_model = BatchSubRequest()
                temp_model = temp_model.from_map(k)
                self.requests.append(temp_model)
        else:
            self.requests = None
        self.resource = map.get('resource')
        return self


class CCPCompleteFileRequest(TeaModel):
    """
    合并文件上传任务
    """
    def __init__(self, drive_id=None, part_info_list=None, upload_id=None, file_id=None):
        # drive_id
        self.drive_id = drive_id
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        self.file_id = map.get('file_id')
        return self


class CCPCopyFileRequest(TeaModel):
    """
    文件拷贝
    """
    def __init__(self, auto_rename=None, drive_id=None, file_id=None, new_name=None, to_drive_id=None,
                 to_parent_file_id=None):
        # auto_rename
        # type: boolean
        self.auto_rename = auto_rename
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # new_name
        self.new_name = new_name
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.to_drive_id:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id:
            self.validate_pattern(self.to_parent_file_id, 'to_parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['auto_rename'] = self.auto_rename
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['new_name'] = self.new_name
        result['to_drive_id'] = self.to_drive_id
        result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        self.auto_rename = map.get('auto_rename')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.new_name = map.get('new_name')
        self.to_drive_id = map.get('to_drive_id')
        self.to_parent_file_id = map.get('to_parent_file_id')
        return self


class CCPCreateFileRequest(TeaModel):
    """
    创建文件
    """
    def __init__(self, content_md_5=None, content_type=None, name=None, part_info_list=None, size=None, type=None,
                 auto_rename=None, check_name_mode=None, content_hash=None, content_hash_name=None, description=None,
                 drive_id=None, encrypt_mode=None, file_id=None, hidden=None, image_media_metadata=None, labels=None,
                 last_updated_at=None, meta=None, parent_file_id=None, pre_hash=None, streams_info=None, user_meta=None,
                 video_media_metadata=None):
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # Name
        self.name = name
        # part_info_list
        self.part_info_list = part_info_list
        # Size
        self.size = size
        # Type
        self.type = type
        self.auto_rename = auto_rename
        # check_name_mode
        self.check_name_mode = check_name_mode
        # content_hash
        self.content_hash = content_hash
        # content_hash_name
        self.content_hash_name = content_hash_name
        # description
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # file_id
        self.file_id = file_id
        # hidden
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        # labels
        self.labels = labels
        # last_updated_at
        self.last_updated_at = last_updated_at
        self.meta = meta
        # parent_file_id
        self.parent_file_id = parent_file_id
        # pre_hash
        self.pre_hash = pre_hash
        # streams_info
        self.streams_info = streams_info
        # user_meta
        self.user_meta = user_meta
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.description:
            self.validate_max_length(self.description, 'description', 0)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['name'] = self.name
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['size'] = self.size
        result['type'] = self.type
        result['auto_rename'] = self.auto_rename
        result['check_name_mode'] = self.check_name_mode
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        else:
            result['image_media_metadata'] = None
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['last_updated_at'] = self.last_updated_at
        result['meta'] = self.meta
        result['parent_file_id'] = self.parent_file_id
        result['pre_hash'] = self.pre_hash
        result['streams_info'] = self.streams_info
        result['user_meta'] = self.user_meta
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        else:
            result['video_media_metadata'] = None
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.name = map.get('name')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.size = map.get('size')
        self.type = map.get('type')
        self.auto_rename = map.get('auto_rename')
        self.check_name_mode = map.get('check_name_mode')
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        if map.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(map['image_media_metadata'])
        else:
            self.image_media_metadata = None
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.last_updated_at = map.get('last_updated_at')
        self.meta = map.get('meta')
        self.parent_file_id = map.get('parent_file_id')
        self.pre_hash = map.get('pre_hash')
        self.streams_info = map.get('streams_info')
        self.user_meta = map.get('user_meta')
        if map.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(map['video_media_metadata'])
        else:
            self.video_media_metadata = None
        return self


class CCPDeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, drive_id=None, file_id=None, permanently=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # permanently
        # type: false
        self.permanently = permanently

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['permanently'] = self.permanently
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.permanently = map.get('permanently')
        return self


class CCPDeleteFilesRequest(TeaModel):
    """
    批量删除文件请求
    """
    def __init__(self, drive_id=None, file_id_list=None):
        # drive_id
        self.drive_id = drive_id
        # file_id_list
        self.file_id_list = file_id_list

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id_list, 'file_id_list')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id_list'] = []
        if self.file_id_list is not None:
            for k in self.file_id_list:
                result['file_id_list'].append(k)
        else:
            result['file_id_list'] = None
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id_list = []
        if map.get('file_id_list') is not None:
            for k in map.get('file_id_list'):
                self.file_id_list.append(k)
        else:
            self.file_id_list = None
        return self


class CCPGetAsyncTaskRequest(TeaModel):
    """
    获取异步人去信息
    """
    def __init__(self, async_task_id=None):
        # async_task_id
        # type:string
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        return self


class CCPGetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_id=None, file_name=None):
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_id
        self.file_id = file_id
        # file_name
        self.file_name = file_name

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.file_name:
            self.validate_max_length(self.file_name, 'file_name', 1024)

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_id'] = self.file_id
        result['file_name'] = self.file_name
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_id = map.get('file_id')
        self.file_name = map.get('file_name')
        return self


class CCPGetFileByPathRequest(TeaModel):
    """
    根据路径获取 File 接口 body
    """
    def __init__(self, drive_id=None, fields=None, file_id=None, file_path=None, image_thumbnail_process=None,
                 image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id
        # fields
        self.fields = fields
        # file_id
        self.file_id = file_id
        # file_path
        self.file_path = file_path
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['fields'] = self.fields
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.fields = map.get('fields')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class CCPGetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, drive_id=None, fields=None, file_id=None, image_thumbnail_process=None,
                 image_url_process=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id
        # fields
        self.fields = fields
        # file_id
        self.file_id = file_id
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['fields'] = self.fields
        result['file_id'] = self.file_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.fields = map.get('fields')
        self.file_id = map.get('file_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class CCPGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, part_info_list=None, upload_id=None, file_id=None):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # upload_part_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id
        # file_id
        self.file_id = file_id

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        result['file_id'] = self.file_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        self.file_id = map.get('file_id')
        return self


class CCPListFileByCustomIndexKeyRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 video_thumbnail_process=None, starred=None, category=None, custom_index_key=None, encrypt_mode=None, fields=None,
                 order_direction=None, status=None, type=None, url_expire_sec=None):
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process
        # starred
        self.starred = starred
        # category
        self.category = category
        # custom_index_key
        self.custom_index_key = custom_index_key
        # encrypt_mode
        self.encrypt_mode = encrypt_mode
        # fields
        self.fields = fields
        # order_direction
        self.order_direction = order_direction
        # status
        self.status = status
        # type
        self.type = type
        # url_expire_sec
        self.url_expire_sec = url_expire_sec

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['video_thumbnail_process'] = self.video_thumbnail_process
        result['Starred'] = self.starred
        result['category'] = self.category
        result['custom_index_key'] = self.custom_index_key
        result['encrypt_mode'] = self.encrypt_mode
        result['fields'] = self.fields
        result['order_direction'] = self.order_direction
        result['status'] = self.status
        result['type'] = self.type
        result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        self.starred = map.get('Starred')
        self.category = map.get('category')
        self.custom_index_key = map.get('custom_index_key')
        self.encrypt_mode = map.get('encrypt_mode')
        self.fields = map.get('fields')
        self.order_direction = map.get('order_direction')
        self.status = map.get('status')
        self.type = map.get('type')
        self.url_expire_sec = map.get('url_expire_sec')
        return self


class CCPListFileRequest(TeaModel):
    """
    列举文件
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 video_thumbnail_process=None, starred=None, all=None, category=None, fields=None, order_by=None, order_direction=None,
                 parent_file_id=None, status=None, type=None, url_expire_sec=None):
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process
        # starred
        self.starred = starred
        # all
        self.all = all
        # category
        self.category = category
        # fields
        self.fields = fields
        # order_by
        self.order_by = order_by
        # order_direction
        self.order_direction = order_direction
        # ParentFileID
        self.parent_file_id = parent_file_id
        # status
        self.status = status
        # type
        self.type = type
        # url_expire_sec
        self.url_expire_sec = url_expire_sec

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['video_thumbnail_process'] = self.video_thumbnail_process
        result['Starred'] = self.starred
        result['all'] = self.all
        result['category'] = self.category
        result['fields'] = self.fields
        result['order_by'] = self.order_by
        result['order_direction'] = self.order_direction
        result['parent_file_id'] = self.parent_file_id
        result['status'] = self.status
        result['type'] = self.type
        result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        self.starred = map.get('Starred')
        self.all = map.get('all')
        self.category = map.get('category')
        self.fields = map.get('fields')
        self.order_by = map.get('order_by')
        self.order_direction = map.get('order_direction')
        self.parent_file_id = map.get('parent_file_id')
        self.status = map.get('status')
        self.type = map.get('type')
        self.url_expire_sec = map.get('url_expire_sec')
        return self


class CCPListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, drive_id=None, file_id=None, limit=None, part_number_marker=None, upload_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # limit
        self.limit = limit
        # part_number_marker
        self.part_number_marker = part_number_marker
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        self.validate_required(self.limit, 'limit')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
        if self.part_number_marker:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['limit'] = self.limit
        result['part_number_marker'] = self.part_number_marker
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.limit = map.get('limit')
        self.part_number_marker = map.get('part_number_marker')
        self.upload_id = map.get('upload_id')
        return self


class CCPMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, new_name=None, overwrite=None, file_id=None, to_parent_file_id=None):
        # drive_id
        self.drive_id = drive_id
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        # file_id
        self.file_id = file_id
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.to_parent_file_id:
            self.validate_max_length(self.to_parent_file_id, 'to_parent_file_id', 50)

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['file_id'] = self.file_id
        result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.file_id = map.get('file_id')
        self.to_parent_file_id = map.get('to_parent_file_id')
        return self


class CCPScanFileMetaRequest(TeaModel):
    """
    全量获取file元信息的请求body
    """
    def __init__(self, category=None, drive_id=None, limit=None, marker=None):
        # category
        self.category = category
        # drive_id
        self.drive_id = drive_id
        # limit
        self.limit = limit
        # marker
        self.marker = marker

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class CCPSearchFileRequest(TeaModel):
    """
    搜索文件元数据
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 order_by=None, query=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # Marker
        self.marker = marker
        # order_by
        self.order_by = order_by
        # query
        self.query = query
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.query:
            self.validate_max_length(self.query, 'query', 4096)

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['order_by'] = self.order_by
        result['query'] = self.query
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.order_by = map.get('order_by')
        self.query = map.get('query')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class CCPUpdateFileMetaRequest(TeaModel):
    """
    更新文件元数据
    """
    def __init__(self, custom_index_key=None, description=None, drive_id=None, encrypt_mode=None, file_id=None,
                 hidden=None, labels=None, meta=None, name=None, starred=None, user_meta=None):
        self.custom_index_key = custom_index_key
        # description
        # type: string
        self.description = description
        # drive_id
        self.drive_id = drive_id
        self.encrypt_mode = encrypt_mode
        # file_id
        self.file_id = file_id
        # hidden
        # type: boolean
        self.hidden = hidden
        # labels
        self.labels = labels
        self.meta = meta
        # name
        self.name = name
        # starred
        # type: boolean
        self.starred = starred
        # user_meta
        self.user_meta = user_meta

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.name:
            self.validate_max_length(self.name, 'name', 1024)

    def to_map(self):
        result = {}
        result['custom_index_key'] = self.custom_index_key
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['encrypt_mode'] = self.encrypt_mode
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k)
        else:
            result['labels'] = None
        result['meta'] = self.meta
        result['name'] = self.name
        result['starred'] = self.starred
        result['user_meta'] = self.user_meta
        return result

    def from_map(self, map={}):
        self.custom_index_key = map.get('custom_index_key')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.encrypt_mode = map.get('encrypt_mode')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                self.labels.append(k)
        else:
            self.labels = None
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.starred = map.get('starred')
        self.user_meta = map.get('user_meta')
        return self


class CompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, drive_id=None, file_id=None, file_path=None, part_info_list=None, share_id=None,
                 upload_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_path = file_path
        # part_info_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class CopyFileRequest(TeaModel):
    """
    copy file request
    """
    def __init__(self, drive_id=None, file_id=None, file_path=None, new_name=None, overwrite=None, share_id=None,
                 to_drive_id=None, to_parent_file_id=None, to_parent_file_path=None, to_share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_path = file_path
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        self.share_id = share_id
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_id
        self.to_parent_file_id = to_parent_file_id
        self.to_parent_file_path = to_parent_file_path
        self.to_share_id = to_share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        self.validate_required(self.new_name, 'new_name')
        if self.new_name:
            self.validate_pattern(self.new_name, 'new_name', '[a-zA-Z0-9.-]{1,1000}')
        self.validate_required(self.to_drive_id, 'to_drive_id')
        if self.to_drive_id:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_id, 'to_parent_file_id')
        if self.to_parent_file_id:
            self.validate_pattern(self.to_parent_file_id, 'to_parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['share_id'] = self.share_id
        result['to_drive_id'] = self.to_drive_id
        result['to_parent_file_id'] = self.to_parent_file_id
        result['to_parent_file_path'] = self.to_parent_file_path
        result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.share_id = map.get('share_id')
        self.to_drive_id = map.get('to_drive_id')
        self.to_parent_file_id = map.get('to_parent_file_id')
        self.to_parent_file_path = map.get('to_parent_file_path')
        self.to_share_id = map.get('to_share_id')
        return self


class CreateDriveRequest(TeaModel):
    """
    create drive request
    """
    def __init__(self, default_=None, description=None, drive_name=None, drive_type=None, encrypt_mode=None,
                 owner=None, relative_path=None, status=None, store_id=None, total_size=None):
        # 是否默认drive, 只允许设置一个默认drive
        self.default_ = default_
        # 描述信息
        self.description = description
        # Drive 名称
        self.drive_name = drive_name
        # Drive类型
        self.drive_type = drive_type
        self.encrypt_mode = encrypt_mode
        # 所属者
        self.owner = owner
        # domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
        self.relative_path = relative_path
        # 状态
        self.status = status
        # StoreID , domain的PathType为OSSPath时必选
        self.store_id = store_id
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size

    def validate(self):
        self.validate_required(self.drive_name, 'drive_name')
        self.validate_required(self.owner, 'owner')

    def to_map(self):
        result = {}
        result['default'] = self.default_
        result['description'] = self.description
        result['drive_name'] = self.drive_name
        result['drive_type'] = self.drive_type
        result['encrypt_mode'] = self.encrypt_mode
        result['owner'] = self.owner
        result['relative_path'] = self.relative_path
        result['status'] = self.status
        result['store_id'] = self.store_id
        result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        self.default_ = map.get('default')
        self.description = map.get('description')
        self.drive_name = map.get('drive_name')
        self.drive_type = map.get('drive_type')
        self.encrypt_mode = map.get('encrypt_mode')
        self.owner = map.get('owner')
        self.relative_path = map.get('relative_path')
        self.status = map.get('status')
        self.store_id = map.get('store_id')
        self.total_size = map.get('total_size')
        return self


class CreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(self, content_hash=None, content_hash_name=None, content_md_5=None, content_type=None,
                 description=None, drive_id=None, hidden=None, meta=None, name=None, parent_file_id=None, parent_file_path=None,
                 part_info_list=None, pre_hash=None, share_id=None, size=None, tags=None, type=None):
        # ContentHash
        self.content_hash = content_hash
        # ContentHashName
        self.content_hash_name = content_hash_name
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # Description
        self.description = description
        # DriveID
        self.drive_id = drive_id
        # Hidden
        self.hidden = hidden
        # Meta
        self.meta = meta
        # name
        self.name = name
        # parent_file_id
        self.parent_file_id = parent_file_id
        # ParentFilePath
        self.parent_file_path = parent_file_path
        # part_info_list
        self.part_info_list = part_info_list
        # pre_hash
        self.pre_hash = pre_hash
        # ShareID
        self.share_id = share_id
        # Size
        self.size = size
        # tags
        self.tags = tags
        # Type
        self.type = type

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        self.validate_required(self.content_type, 'content_type')
        if self.description:
            self.validate_max_length(self.description, 'description', 0)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.name, 'name')
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.size, 'size')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['content_hash'] = self.content_hash
        result['content_hash_name'] = self.content_hash_name
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['hidden'] = self.hidden
        result['meta'] = self.meta
        result['name'] = self.name
        result['parent_file_id'] = self.parent_file_id
        result['parent_file_path'] = self.parent_file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['pre_hash'] = self.pre_hash
        result['share_id'] = self.share_id
        result['size'] = self.size
        result['tags'] = self.tags
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.content_hash = map.get('content_hash')
        self.content_hash_name = map.get('content_hash_name')
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.hidden = map.get('hidden')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.parent_file_id = map.get('parent_file_id')
        self.parent_file_path = map.get('parent_file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.pre_hash = map.get('pre_hash')
        self.share_id = map.get('share_id')
        self.size = map.get('size')
        self.tags = map.get('tags')
        self.type = map.get('type')
        return self


class CreateShareRequest(TeaModel):
    """
    create share request
    """
    def __init__(self, description=None, drive_id=None, expiration=None, owner=None, permissions=None,
                 share_file_path=None, share_name=None, share_policy=None, status=None):
        # description
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # expiration
        self.expiration = expiration
        # creator
        self.owner = owner
        # permissions
        self.permissions = permissions
        # share_file_path
        self.share_file_path = share_file_path
        # share_name
        self.share_name = share_name
        # share create policy
        # 
        # share_policy
        self.share_policy = share_policy
        # status
        self.status = status

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.owner, 'owner')
        self.validate_required(self.share_file_path, 'share_file_path')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['expiration'] = self.expiration
        result['owner'] = self.owner
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k)
        else:
            result['permissions'] = None
        result['share_file_path'] = self.share_file_path
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.expiration = map.get('expiration')
        self.owner = map.get('owner')
        self.permissions = []
        if map.get('permissions') is not None:
            for k in map.get('permissions'):
                self.permissions.append(k)
        else:
            self.permissions = None
        self.share_file_path = map.get('share_file_path')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                temp_model = temp_model.from_map(k)
                self.share_policy.append(temp_model)
        else:
            self.share_policy = None
        self.status = map.get('status')
        return self


class DeleteDriveRequest(TeaModel):
    """
    Delete drive request
    """
    def __init__(self, drive_id=None):
        # Drive ID
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        return self


class DeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, drive_id=None, file_id=None, file_path=None, permanently=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_path = file_path
        self.permanently = permanently
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['permanently'] = self.permanently
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.permanently = map.get('permanently')
        self.share_id = map.get('share_id')
        return self


class DeleteShareRequest(TeaModel):
    """
    delete share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.share_id, 'share_id')

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        return self


class DownloadRequest(TeaModel):
    """
    下载文件请求body
    """
    def __init__(self, drive_id=None, file_id=None, image_process=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # image_process
        self.image_process = image_process
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['DriveID'] = self.drive_id
        result['FileID'] = self.file_id
        result['ImageProcess'] = self.image_process
        result['ShareID'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('DriveID')
        self.file_id = map.get('FileID')
        self.image_process = map.get('ImageProcess')
        self.share_id = map.get('ShareID')
        return self


class GetAsyncTaskRequest(TeaModel):
    """
    获取异步人去信息
    """
    def __init__(self, async_task_id=None):
        # async_task_id
        # type:string
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, map={}):
        self.async_task_id = map.get('async_task_id')
        return self


class GetDefaultDriveRequest(TeaModel):
    """
    Get default drive request
    """
    def __init__(self, user_id=None):
        # 用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.user_id = map.get('user_id')
        return self


class GetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_id=None, file_name=None, file_path=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_id
        self.file_id = file_id
        # file_name
        self.file_name = file_name
        self.file_path = file_path
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        if self.file_name:
            self.validate_pattern(self.file_name, 'file_name', '[a-zA-Z0-9.-]{1,1000}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_id'] = self.file_id
        result['file_name'] = self.file_name
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_id = map.get('file_id')
        self.file_name = map.get('file_name')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class GetDriveRequest(TeaModel):
    """
    Get drive request
    """
    def __init__(self, drive_id=None):
        # Drive ID
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        return self


class GetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, drive_id=None, file_id=None, file_path=None, image_thumbnail_process=None,
                 image_url_process=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_path = file_path
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process
        self.share_id = share_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.share_id = map.get('share_id')
        return self


class GetLastCursorRequest(TeaModel):
    """
    获取最新游标
    """
    def __init__(self, drive_id=None):
        # drive_id
        self.drive_id = drive_id

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        return self


class GetShareRequest(TeaModel):
    """
    get share request
    """
    def __init__(self, share_id=None):
        # share_id
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.share_id = map.get('share_id')
        return self


class GetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, file_id=None, file_path=None, part_info_list=None,
                 share_id=None, upload_id=None):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        self.file_path = file_path
        # upload_part_list
        self.part_info_list = part_info_list
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9]{1,50}')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        self.validate_required(self.upload_id, 'upload_id')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['file_path'] = self.file_path
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.file_path = map.get('file_path')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class ImageMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, height=None, width=None):
        # height
        self.height = height
        # width：
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['height'] = self.height
        result['width'] = self.width
        return result

    def from_map(self, map={}):
        self.height = map.get('height')
        self.width = map.get('width')
        return self


class ListDriveRequest(TeaModel):
    """
    List drive request
    """
    def __init__(self, limit=None, marker=None, owner=None):
        # 每页大小限制
        self.limit = limit
        # 翻页标记, 接口返回的标记值
        self.marker = marker
        # 所属者
        self.owner = owner

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['owner'] = self.owner
        return result

    def from_map(self, map={}):
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.owner = map.get('owner')
        return self


class ListFileDeltaRequest(TeaModel):
    """
    获取增量文件操作记录
    """
    def __init__(self, cursor=None, drive_id=None, limit=None):
        # cursor 游标
        self.cursor = cursor
        # drive_id
        self.drive_id = drive_id
        # limit
        # default 100
        self.limit = limit

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')

    def to_map(self):
        result = {}
        result['cursor'] = self.cursor
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        return result

    def from_map(self, map={}):
        self.cursor = map.get('cursor')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        return self


class ListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, all=None, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None,
                 marker=None, parent_file_id=None, parent_file_path=None, share_id=None, status=None):
        # all
        self.all = all
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # ParentFileID
        self.parent_file_id = parent_file_id
        self.parent_file_path = parent_file_path
        self.share_id = share_id
        # status
        self.status = status

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
        self.validate_required(self.parent_file_id, 'parent_file_id')
        if self.parent_file_id:
            self.validate_pattern(self.parent_file_id, 'parent_file_id', '[a-z0-9.-_]{1,50}')

    def to_map(self):
        result = {}
        result['all'] = self.all
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_id'] = self.parent_file_id
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.all = map.get('all')
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_id = map.get('parent_file_id')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.status = map.get('status')
        return self


class ListMyDriveRequest(TeaModel):
    """
    List my drive request
    """
    def __init__(self, limit=None, marker=None):
        # 每页大小限制
        self.limit = limit
        # 翻页标记, 接口返回的标记值
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListShareRequest(TeaModel):
    """
    list share request
    """
    def __init__(self, creator=None, drive_id=None, limit=None, marker=None, owner=None, share_file_path=None):
        # creator
        self.creator = creator
        self.drive_id = drive_id
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # Owner
        self.owner = owner
        # share_file_path
        self.share_file_path = share_file_path

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.limit, 'limit')

    def to_map(self):
        result = {}
        result['creator'] = self.creator
        result['drive_id'] = self.drive_id
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['owner'] = self.owner
        result['share_file_path'] = self.share_file_path
        return result

    def from_map(self, map={}):
        self.creator = map.get('creator')
        self.drive_id = map.get('drive_id')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.owner = map.get('owner')
        self.share_file_path = map.get('share_file_path')
        return self


class ListStoreFileRequest(TeaModel):
    """
    list store file
    """
    def __init__(self, limit=None, marker=None, parent_file_path=None, store_id=None, type=None):
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # parent_file_path
        self.parent_file_path = parent_file_path
        # store_id
        self.store_id = store_id
        # type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_path'] = self.parent_file_path
        result['store_id'] = self.store_id
        result['type'] = self.type
        return result

    def from_map(self, map={}):
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_path = map.get('parent_file_path')
        self.store_id = map.get('store_id')
        self.type = map.get('type')
        return self


class ListStoreRequest(TeaModel):
    """
    list storage file
    """
    def __init__(self, domain_id=None):
        # domain_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['domain_id'] = self.domain_id
        return result

    def from_map(self, map={}):
        self.domain_id = map.get('domain_id')
        return self


class OSSCompleteFileRequest(TeaModel):
    """
    complete file request
    """
    def __init__(self, drive_id=None, part_info_list=None, upload_id=None, file_path=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # part_info_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id
        self.file_path = file_path
        self.share_id = share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSCopyFileRequest(TeaModel):
    """
    copy file request
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None, to_drive_id=None,
                 to_parent_file_path=None, to_share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        # share_id
        self.share_id = share_id
        # to_drive_id
        self.to_drive_id = to_drive_id
        # to_parent_file_path
        self.to_parent_file_path = to_parent_file_path
        # share_id
        self.to_share_id = to_share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.new_name:
            self.validate_pattern(self.new_name, 'new_name', '[a-zA-Z0-9.-]{1,1000}')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.to_drive_id, 'to_drive_id')
        if self.to_drive_id:
            self.validate_pattern(self.to_drive_id, 'to_drive_id', '[0-9]+')
        self.validate_required(self.to_parent_file_path, 'to_parent_file_path')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['share_id'] = self.share_id
        result['to_drive_id'] = self.to_drive_id
        result['to_parent_file_path'] = self.to_parent_file_path
        result['to_share_id'] = self.to_share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.share_id = map.get('share_id')
        self.to_drive_id = map.get('to_drive_id')
        self.to_parent_file_path = map.get('to_parent_file_path')
        self.to_share_id = map.get('to_share_id')
        return self


class OSSCreateFileRequest(TeaModel):
    """
    create file request
    """
    def __init__(self, content_md_5=None, content_type=None, name=None, part_info_list=None, size=None, type=None,
                 drive_id=None, parent_file_path=None, share_id=None):
        # ContentMd5
        self.content_md_5 = content_md_5
        # ContentType
        self.content_type = content_type
        # Name
        self.name = name
        # part_info_list
        self.part_info_list = part_info_list
        # Size
        self.size = size
        # Type
        self.type = type
        # drive_id
        self.drive_id = drive_id
        # parent_file_path
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['content_type'] = self.content_type
        result['name'] = self.name
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['size'] = self.size
        result['type'] = self.type
        result['drive_id'] = self.drive_id
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.content_type = map.get('content_type')
        self.name = map.get('name')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.size = map.get('size')
        self.type = map.get('type')
        self.drive_id = map.get('drive_id')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        return self


class OSSDeleteFileRequest(TeaModel):
    """
    删除文件请求
    """
    def __init__(self, drive_id=None, file_path=None, permanently=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # permanently
        # type: false
        self.permanently = permanently
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['permanently'] = self.permanently
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.permanently = map.get('permanently')
        self.share_id = map.get('share_id')
        return self


class OSSGetDownloadUrlRequest(TeaModel):
    """
    获取文件下载地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_name=None, file_path=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_name
        self.file_name = file_name
        # file_path
        self.file_path = file_path
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_name'] = self.file_name
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_name = map.get('file_name')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSGetFileRequest(TeaModel):
    """
    获取文件元数据
    """
    def __init__(self, drive_id=None, file_path=None, image_thumbnail_process=None, image_url_process=None,
                 share_id=None, url_expire_sec=None):
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_path = file_path
        # image_thumbnail_process
        # type:string
        self.image_thumbnail_process = image_thumbnail_process
        # image_thumbnail_process
        # type:string
        self.image_url_process = image_url_process
        # share_id
        self.share_id = share_id
        # url_expire_sec
        self.url_expire_sec = url_expire_sec

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['share_id'] = self.share_id
        result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.share_id = map.get('share_id')
        self.url_expire_sec = map.get('url_expire_sec')
        return self


class OSSGetSecureUrlRequest(TeaModel):
    """
    获取文件安全地址的请求body
    """
    def __init__(self, drive_id=None, expire_sec=None, file_path=None, secure_ip=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # expire_sec 单位秒
        self.expire_sec = expire_sec
        # file_path
        self.file_path = file_path
        # secure_ip
        self.secure_ip = secure_ip
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_path'] = self.file_path
        result['secure_ip'] = self.secure_ip
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_path = map.get('file_path')
        self.secure_ip = map.get('secure_ip')
        self.share_id = map.get('share_id')
        return self


class OSSGetUploadUrlRequest(TeaModel):
    """
    获取文件上传URL
    """
    def __init__(self, content_md_5=None, drive_id=None, part_info_list=None, upload_id=None, file_path=None,
                 share_id=None):
        # content_md5
        self.content_md_5 = content_md_5
        # drive_id
        self.drive_id = drive_id
        # upload_part_list
        self.part_info_list = part_info_list
        # upload_id
        self.upload_id = upload_id
        # file_path
        self.file_path = file_path
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.content_md_5:
            self.validate_max_length(self.content_md_5, 'content_md_5', 32)
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['content_md5'] = self.content_md_5
        result['drive_id'] = self.drive_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        else:
            result['part_info_list'] = None
        result['upload_id'] = self.upload_id
        result['file_path'] = self.file_path
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.content_md_5 = map.get('content_md5')
        self.drive_id = map.get('drive_id')
        self.part_info_list = []
        if map.get('part_info_list') is not None:
            for k in map.get('part_info_list'):
                temp_model = UploadPartInfo()
                temp_model = temp_model.from_map(k)
                self.part_info_list.append(temp_model)
        else:
            self.part_info_list = None
        self.upload_id = map.get('upload_id')
        self.file_path = map.get('file_path')
        self.share_id = map.get('share_id')
        return self


class OSSListFileRequest(TeaModel):
    """
    list file request
    """
    def __init__(self, drive_id=None, image_thumbnail_process=None, image_url_process=None, limit=None, marker=None,
                 parent_file_path=None, share_id=None, url_expire_sec=None, video_thumbnail_process=None):
        # drive_id
        self.drive_id = drive_id
        # image_thumbnail_process
        self.image_thumbnail_process = image_thumbnail_process
        # image_url_process
        self.image_url_process = image_url_process
        # limit
        self.limit = limit
        # marker
        self.marker = marker
        # ParentFilePath
        self.parent_file_path = parent_file_path
        # share_id
        self.share_id = share_id
        # url_expire_sec
        self.url_expire_sec = url_expire_sec
        # video_thumbnail_process
        # type:string
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]{1,3}')
        self.validate_required(self.parent_file_path, 'parent_file_path')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['image_thumbnail_process'] = self.image_thumbnail_process
        result['image_url_process'] = self.image_url_process
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['parent_file_path'] = self.parent_file_path
        result['share_id'] = self.share_id
        result['url_expire_sec'] = self.url_expire_sec
        result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.image_thumbnail_process = map.get('image_thumbnail_process')
        self.image_url_process = map.get('image_url_process')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.parent_file_path = map.get('parent_file_path')
        self.share_id = map.get('share_id')
        self.url_expire_sec = map.get('url_expire_sec')
        self.video_thumbnail_process = map.get('video_thumbnail_process')
        return self


class OSSListUploadedPartRequest(TeaModel):
    """
    列举uploadID对应的已上传分片
    """
    def __init__(self, drive_id=None, file_path=None, limit=None, part_number_marker=None, share_id=None,
                 upload_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # limit
        self.limit = limit
        # part_number_marker
        self.part_number_marker = part_number_marker
        # share_id
        self.share_id = share_id
        # upload_id
        self.upload_id = upload_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        self.validate_required(self.limit, 'limit')
        if self.limit:
            self.validate_pattern(self.limit, 'limit', '[0-9]+')
        if self.part_number_marker:
            self.validate_pattern(self.part_number_marker, 'part_number_marker', '[0-9]+')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['limit'] = self.limit
        result['part_number_marker'] = self.part_number_marker
        result['share_id'] = self.share_id
        result['upload_id'] = self.upload_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.limit = map.get('limit')
        self.part_number_marker = map.get('part_number_marker')
        self.share_id = map.get('share_id')
        self.upload_id = map.get('upload_id')
        return self


class OSSMoveFileRequest(TeaModel):
    """
    文件移动请求
    """
    def __init__(self, drive_id=None, file_path=None, new_name=None, overwrite=None, share_id=None,
                 to_parent_file_path=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # new_name
        self.new_name = new_name
        # overwrite
        # type: boolean
        self.overwrite = overwrite
        # share_id
        self.share_id = share_id
        # file_path
        self.to_parent_file_path = to_parent_file_path

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.new_name, 'new_name')
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['new_name'] = self.new_name
        result['overwrite'] = self.overwrite
        result['share_id'] = self.share_id
        result['to_parent_file_path'] = self.to_parent_file_path
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.new_name = map.get('new_name')
        self.overwrite = map.get('overwrite')
        self.share_id = map.get('share_id')
        self.to_parent_file_path = map.get('to_parent_file_path')
        return self


class OSSVideoDRMLicenseRequest(TeaModel):
    """
    获取视频DRM License
    """
    def __init__(self, drm_type=None, license_request=None):
        # drmType
        self.drm_type = drm_type
        # licenseRequest
        self.license_request = license_request

    def validate(self):
        self.validate_required(self.drm_type, 'drm_type')
        self.validate_required(self.license_request, 'license_request')

    def to_map(self):
        result = {}
        result['drmType'] = self.drm_type
        result['licenseRequest'] = self.license_request
        return result

    def from_map(self, map={}):
        self.drm_type = map.get('drmType')
        self.license_request = map.get('licenseRequest')
        return self


class OSSVideoDefinitionRequest(TeaModel):
    """
    获取视频分辨率列表
    """
    def __init__(self, drive_id=None, file_path=None, protection_scheme=None, share_id=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # protection_scheme
        self.protection_scheme = protection_scheme
        # share_id
        self.share_id = share_id

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['protection_scheme'] = self.protection_scheme
        result['share_id'] = self.share_id
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.protection_scheme = map.get('protection_scheme')
        self.share_id = map.get('share_id')
        return self


class OSSVideoM3U8Request(TeaModel):
    """
    获取视频的m3u8文件
    """
    def __init__(self, definition=None, drive_id=None, expire_sec=None, file_path=None, protection_scheme=None,
                 share_id=None, sign_token=None):
        # definition
        self.definition = definition
        # drive_id
        self.drive_id = drive_id
        # expire_sec
        self.expire_sec = expire_sec
        # file_path
        self.file_path = file_path
        # protection_scheme
        self.protection_scheme = protection_scheme
        # share_id
        self.share_id = share_id
        # sign_token
        self.sign_token = sign_token

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')
        self.validate_required(self.sign_token, 'sign_token')

    def to_map(self):
        result = {}
        result['definition'] = self.definition
        result['drive_id'] = self.drive_id
        result['expire_sec'] = self.expire_sec
        result['file_path'] = self.file_path
        result['protection_scheme'] = self.protection_scheme
        result['share_id'] = self.share_id
        result['sign_token'] = self.sign_token
        return result

    def from_map(self, map={}):
        self.definition = map.get('definition')
        self.drive_id = map.get('drive_id')
        self.expire_sec = map.get('expire_sec')
        self.file_path = map.get('file_path')
        self.protection_scheme = map.get('protection_scheme')
        self.share_id = map.get('share_id')
        self.sign_token = map.get('sign_token')
        return self


class OSSVideoTranscodeRequest(TeaModel):
    """
    启动视频转码请求
    """
    def __init__(self, drive_id=None, file_path=None, hls_time=None, protection_scheme=None, remarks=None,
                 share_id=None, transcode=None):
        # drive_id
        self.drive_id = drive_id
        # file_path
        self.file_path = file_path
        # hls_time
        self.hls_time = hls_time
        # protection_scheme
        self.protection_scheme = protection_scheme
        # remarks
        self.remarks = remarks
        # share_id
        self.share_id = share_id
        # transcode
        self.transcode = transcode

    def validate(self):
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_path, 'file_path')
        if self.file_path:
            self.validate_max_length(self.file_path, 'file_path', 1000)
        if self.share_id:
            self.validate_pattern(self.share_id, 'share_id', '[0-9a-zA-Z-]+')

    def to_map(self):
        result = {}
        result['drive_id'] = self.drive_id
        result['file_path'] = self.file_path
        result['hls_time'] = self.hls_time
        result['protection_scheme'] = self.protection_scheme
        result['remarks'] = self.remarks
        result['share_id'] = self.share_id
        result['transcode'] = self.transcode
        return result

    def from_map(self, map={}):
        self.drive_id = map.get('drive_id')
        self.file_path = map.get('file_path')
        self.hls_time = map.get('hls_time')
        self.protection_scheme = map.get('protection_scheme')
        self.remarks = map.get('remarks')
        self.share_id = map.get('share_id')
        self.transcode = map.get('transcode')
        return self


class UCGetObjectInfoByObjectKeyRequest(TeaModel):
    """
    UCGetObjectInfoByObjectKeyRequest
    """
    def __init__(self, object_key=None):
        self.object_key = object_key

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['object_key'] = self.object_key
        return result

    def from_map(self, map={}):
        self.object_key = map.get('object_key')
        return self


class UCGetObjectInfoBySha1Request(TeaModel):
    """
    UCGetObjectInfoBySha1Request
    """
    def __init__(self, sha_1=None):
        self.sha_1 = sha_1

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['sha1'] = self.sha_1
        return result

    def from_map(self, map={}):
        self.sha_1 = map.get('sha1')
        return self


class UpdateDriveRequest(TeaModel):
    """
    Update drive request
    """
    def __init__(self, description=None, drive_id=None, drive_name=None, encrypt_data_access=None,
                 encrypt_mode=None, status=None, total_size=None):
        # 描述信息
        self.description = description
        # Drive ID
        self.drive_id = drive_id
        # Drive 名称
        self.drive_name = drive_name
        # 授权访问加密数据
        self.encrypt_data_access = encrypt_data_access
        # 加密模式
        self.encrypt_mode = encrypt_mode
        # 状态
        self.status = status
        # 总大小,单位Byte [如果设置 -1 代表不限制]
        self.total_size = total_size

    def validate(self):
        self.validate_required(self.drive_id, 'drive_id')

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['drive_name'] = self.drive_name
        result['encrypt_data_access'] = self.encrypt_data_access
        result['encrypt_mode'] = self.encrypt_mode
        result['status'] = self.status
        result['total_size'] = self.total_size
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.drive_name = map.get('drive_name')
        self.encrypt_data_access = map.get('encrypt_data_access')
        self.encrypt_mode = map.get('encrypt_mode')
        self.status = map.get('status')
        self.total_size = map.get('total_size')
        return self


class UpdateFileMetaRequest(TeaModel):
    """
    更新文件元数据
    """
    def __init__(self, description=None, drive_id=None, file_id=None, hidden=None, meta=None, name=None,
                 share_id=None, starred=None, tags=None):
        # description
        # type: string
        self.description = description
        # drive_id
        self.drive_id = drive_id
        # file_id
        self.file_id = file_id
        # hidden
        # type: boolean
        self.hidden = hidden
        # meta
        self.meta = meta
        # name
        self.name = name
        self.share_id = share_id
        # starred
        # type: boolean
        self.starred = starred
        # tags
        self.tags = tags

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1000)
        self.validate_required(self.drive_id, 'drive_id')
        if self.drive_id:
            self.validate_pattern(self.drive_id, 'drive_id', '[0-9]+')
        self.validate_required(self.file_id, 'file_id')
        if self.file_id:
            self.validate_pattern(self.file_id, 'file_id', '[a-z0-9.-_]{1,50}')
        self.validate_required(self.name, 'name')
        if self.name:
            self.validate_pattern(self.name, 'name', '[a-zA-Z0-9.-]{1,1000}')

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['drive_id'] = self.drive_id
        result['file_id'] = self.file_id
        result['hidden'] = self.hidden
        result['meta'] = self.meta
        result['name'] = self.name
        result['share_id'] = self.share_id
        result['starred'] = self.starred
        result['tags'] = self.tags
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.drive_id = map.get('drive_id')
        self.file_id = map.get('file_id')
        self.hidden = map.get('hidden')
        self.meta = map.get('meta')
        self.name = map.get('name')
        self.share_id = map.get('share_id')
        self.starred = map.get('starred')
        self.tags = map.get('tags')
        return self


class UpdateShareRequest(TeaModel):
    """
    update share request
    """
    def __init__(self, description=None, expiration=None, permissions=None, share_id=None, share_name=None,
                 share_policy=None, status=None):
        # description
        self.description = description
        # expiration
        self.expiration = expiration
        # permissions
        self.permissions = permissions
        # share_id
        self.share_id = share_id
        # share_name
        self.share_name = share_name
        # share_policy
        self.share_policy = share_policy
        # status
        self.status = status

    def validate(self):
        if self.description:
            self.validate_max_length(self.description, 'description', 1024)
        self.validate_required(self.share_id, 'share_id')
        if self.share_policy:
            for k in self.share_policy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['expiration'] = self.expiration
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k)
        else:
            result['permissions'] = None
        result['share_id'] = self.share_id
        result['share_name'] = self.share_name
        result['share_policy'] = []
        if self.share_policy is not None:
            for k in self.share_policy:
                result['share_policy'].append(k.to_map() if k else None)
        else:
            result['share_policy'] = None
        result['status'] = self.status
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.expiration = map.get('expiration')
        self.permissions = []
        if map.get('permissions') is not None:
            for k in map.get('permissions'):
                self.permissions.append(k)
        else:
            self.permissions = None
        self.share_id = map.get('share_id')
        self.share_name = map.get('share_name')
        self.share_policy = []
        if map.get('share_policy') is not None:
            for k in map.get('share_policy'):
                temp_model = SharePermissionPolicy()
                temp_model = temp_model.from_map(k)
                self.share_policy.append(temp_model)
        else:
            self.share_policy = None
        self.status = map.get('status')
        return self


class VideoMediaMetadata(TeaModel):
    """
    *
    """
    def __init__(self, duration=None):
        # Duration
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['duration'] = self.duration
        return result

    def from_map(self, map={}):
        self.duration = map.get('duration')
        return self


class CreateUserRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteUserRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteUserModel(TeaModel):
    def __init__(self, headers=None):
        # headers
        self.headers = headers

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetUserRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUsersRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ListUsersModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SearchUserRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = SearchUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class SearchUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateUserRequestModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateUserRequest()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UpdateUserModel(TeaModel):
    def __init__(self, headers=None, body=None):
        # headers
        self.headers = headers
        # body
        self.body = body

    def validate(self):
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = UpdateUserResponse()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class BaseUserResponse(TeaModel):
    """
    Base user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class CreateUserRequest(TeaModel):
    """
    Create user request
    """
    def __init__(self, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None, status=None,
                 user_data=None, user_id=None, user_name=None):
        # 头像
        self.avatar = avatar
        # 描述信息
        self.description = description
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['description'] = self.description
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.description = map.get('description')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class CreateUserResponse(TeaModel):
    """
    Create user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class DeleteUserRequest(TeaModel):
    """
    Delete user request
    """
    def __init__(self, user_id=None):
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.user_id = map.get('user_id')
        return self


class DeleteUserResponse(TeaModel):
    """
    Delete user response
    """
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class GetUserRequest(TeaModel):
    """
    Get user request
    """
    def __init__(self, user_id=None):
        # 用户 ID, 使用ak方式访问，该项必传, access_token访问如果不传，默认取自己的user信息
        # example
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.user_id = map.get('user_id')
        return self


class GetUserResponse(TeaModel):
    """
    Get user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self


class ListUserRequest(TeaModel):
    """
    List user request
    """
    def __init__(self, limit=None, marker=None):
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['limit'] = self.limit
        result['marker'] = self.marker
        return result

    def from_map(self, map={}):
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        return self


class ListUserResponse(TeaModel):
    """
    List user response
    """
    def __init__(self, items=None, next_marker=None):
        self.items = items
        # 翻页标记
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        result['next_marker'] = self.next_marker
        return result

    def from_map(self, map={}):
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = BaseUserResponse()
                temp_model = temp_model.from_map(k)
                self.items.append(temp_model)
        else:
            self.items = None
        self.next_marker = map.get('next_marker')
        return self


class SearchUserRequest(TeaModel):
    """
    Search user request
    """
    def __init__(self, email=None, limit=None, marker=None, nick_name=None, phone=None, role=None, status=None,
                 user_name=None):
        # 邮箱
        self.email = email
        # 每页大小限制
        self.limit = limit
        # 翻页标记
        self.marker = marker
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # 用户名
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['email'] = self.email
        result['limit'] = self.limit
        result['marker'] = self.marker
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.email = map.get('email')
        self.limit = map.get('limit')
        self.marker = map.get('marker')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_name = map.get('user_name')
        return self


class UpdateUserRequest(TeaModel):
    """
    Update user request
    """
    def __init__(self, avatar=None, description=None, email=None, nick_name=None, phone=None, role=None, status=None,
                 user_data=None, user_id=None):
        # 头像
        self.avatar = avatar
        # 描述信息
        self.description = description
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话号码
        self.phone = phone
        # 角色
        self.role = role
        # 状态
        self.status = status
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id

    def validate(self):
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['description'] = self.description
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.description = map.get('description')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        return self


class UpdateUserResponse(TeaModel):
    """
    Update user response
    """
    def __init__(self, avatar=None, created_at=None, default_drive_id=None, description=None, domain_id=None,
                 email=None, nick_name=None, phone=None, role=None, status=None, updated_at=None, user_data=None,
                 user_id=None, user_name=None):
        # 头像
        self.avatar = avatar
        # 用户创建时间
        self.created_at = created_at
        # 默认 Drive ID
        self.default_drive_id = default_drive_id
        # 用户备注信息
        self.description = description
        # Domain ID
        self.domain_id = domain_id
        # 邮箱
        self.email = email
        # 昵称
        self.nick_name = nick_name
        # 电话
        self.phone = phone
        # 角色
        self.role = role
        # 用户状态
        self.status = status
        # 用户修改时间
        self.updated_at = updated_at
        # 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        self.user_data = user_data
        # 用户 ID
        self.user_id = user_id
        # 用户名称
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['avatar'] = self.avatar
        result['created_at'] = self.created_at
        result['default_drive_id'] = self.default_drive_id
        result['description'] = self.description
        result['domain_id'] = self.domain_id
        result['email'] = self.email
        result['nick_name'] = self.nick_name
        result['phone'] = self.phone
        result['role'] = self.role
        result['status'] = self.status
        result['updated_at'] = self.updated_at
        result['user_data'] = self.user_data
        result['user_id'] = self.user_id
        result['user_name'] = self.user_name
        return result

    def from_map(self, map={}):
        self.avatar = map.get('avatar')
        self.created_at = map.get('created_at')
        self.default_drive_id = map.get('default_drive_id')
        self.description = map.get('description')
        self.domain_id = map.get('domain_id')
        self.email = map.get('email')
        self.nick_name = map.get('nick_name')
        self.phone = map.get('phone')
        self.role = map.get('role')
        self.status = map.get('status')
        self.updated_at = map.get('updated_at')
        self.user_data = map.get('user_data')
        self.user_id = map.get('user_id')
        self.user_name = map.get('user_name')
        return self
