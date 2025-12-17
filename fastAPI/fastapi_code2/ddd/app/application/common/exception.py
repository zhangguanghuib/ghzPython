'''
通用业务异常
'''
from typing import Optional


class DomainException(Exception):
    '''
    业务异常
    '''
    def __init__(self, message:str, code: Optional[str]=None):
        self.message = message
        self.code  = code
        super().__init__(message)

class AuthError(DomainException):
    '''
    认证异常
    '''
    def __init__(self, message='认证失败'):
        super().__init__(message, 'AUTH_ERROR')

class DuplicateError(DomainException):
    '''
    重复数据异常
    '''
    def __init__(self, message='数据已存在'):
        super().__init__(message, 'DUPLICATE_ERROR')
    
class NotFoundError(DomainException):
    '''
    数据不存在异常
    '''
    def __init__(self, message='数据不存在'):
        super().__init__(message, 'NOT_FOUND_ERROR')
class ValidationError(DomainException):
    '''
    数据验证异常
    '''
    def __init__(self, message='数据验证失败'):
        super().__init__(message, 'VALIDATION_ERROR')