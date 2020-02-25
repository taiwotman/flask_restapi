from flask import Blueprint
from flask_restplus import Api
from .namespace1 import api as ns1
# from .namespace2 import api as ns2
# ...
# from .namespaceX import api as nsX
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint, title='TODO API',version='1.0', description='A description')  # All API metadatas

api.add_namespace(ns1)
