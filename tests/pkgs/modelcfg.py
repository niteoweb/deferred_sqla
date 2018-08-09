from deferred_sqla import model_config
from sqlalchemy.ext.declarative.base import _declarative_constructor

@model_config
class MyMainModel1(object):
    __abstract__ = True
    __init__ = _declarative_constructor

@model_config(category='main')
class MyMainModel2(object):
    __abstract__ = True
    __init__ = _declarative_constructor

@model_config()
class MyMainModel3(object):
    __abstract__ = True
    __init__ = _declarative_constructor

@model_config(category='other')
class MyOtherModel1(object):
    __abstract__ = True
    __init__ = _declarative_constructor

@model_config(category='other')
class MyOtherModel2(object):
    __abstract__ = True
    __init__ = _declarative_constructor
