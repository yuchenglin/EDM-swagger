import sys
import json
sys.path.append('../')
# from utilities.file_op import fileOps
from ApiGenerator import *

class ApiGenerator:
    def __init__(self):
        self.__outjson = {}
        self.__dmname = ''
        self.__host = ''
        self.__accessKey = ''
        self.__user = ''

    '''
    Sample
    host: http://localhost:2000
    dmname: Generalization
    '''
    def set_basic_path(self, host, dmname):
        self.__host = host
        self.__dmname = dmname
        self.__json = self.__create_basic_template()

    def set_access_key(self, key):
        self.__accessKey = key

    def set_user_name(self, user):
        self.__user = user

    def add_entity(self, entity_name):
        self.__json['tags'].append({
            'name': entity_name,
            'description': 'Everything about' + entity_name
        })
        self.__set_entity_apis(entity_name)

    def generate_file(self, path):
        # with fileOps.safe_open_w(path + 'openAPI.json', 'w') as o:
        with open(path + 'openAPI.json', 'w') as o:
            json.dump(self.__json, o)

    def __create_basic_template(self):
        api = {
	        'swagger': '2.0',	
        }
        api['info'] = {
            'version': '1.0.0',
            'title': self.__dmname + ' API Reference'
	    }
        api['host'] = self.__host
        api['basePath'] = '/' + self.__dmname
        api['tags'] = []
        # api details
        api['paths'] = {}
        # definition
        api['definitions'] = {}
        return api

    def __set_entity_apis(self, entity_name):
        # create data payload structure
        properties = {}
        self.__define_object('SignleData', properties) ####### TODO
        self.__define_object('SingleId', properties)
        self.__define_object('MultiData', properties)
        self.__define_object('MultiId', properties)
        self.__define_object('UpdateById', properties)
        self.__define_object('UpdateByData', properties)

        params = []
        self.__gen_parameter(params, 'Create with single data', 'SignleData')
        self.__add_entity_api(entity_name, 'create', 'post', params)

        params = []
        self.__gen_parameter(params, 'Create with multiple data', 'MultiData')
        self.__add_entity_api(entity_name, 'createMany', 'post', params)

        params = []
        self.__gen_parameter(params, 'Read by data', 'SignleData')
        self.__gen_parameter(params, 'Read by id', 'SingleId')
        self.__add_entity_api(entity_name, 'readOne', 'post', params)

        params = []
        self.__gen_parameter(params, 'Read many by data', 'SignleData')
        self.__gen_parameter(params, 'Read many by ids', 'SingleId')
        self.__add_entity_api(entity_name, 'readMany', 'post', params)

        params = []
        self.__gen_parameter(params, 'Detele by data', 'SignleData')
        self.__gen_parameter(params, 'Delete by id', 'SingleId')
        self.__add_entity_api(entity_name, 'delete', 'delete', params)

        params = []
        self.__gen_parameter(params, 'Update data by data id', 'UpdateById')
        self.__gen_parameter(params, 'Update data by old data', 'UpdateByData')
        self.__add_entity_api(entity_name, 'update', 'put', params)
    
    '''
    add_entity_api(Generalization, create, post, ...)
    '''
    def __add_entity_api(self, entity_name, action, http_method, params):
        api_path = '/' + entity_name + '/' + action
        self.__json['paths'][api_path] = {}
        self.__json['paths'][api_path][http_method] = {
            'tags': [entity_name],
            'summary': action + ' elements for ' + entity_name,
            'consumes': ['application/json'],
            'produces': ['application/json'],
            'responses': {
                '200': {
                    'description': entity_name + ': ' + action + ' successfully'
                }
            },
            'parameters': params
        }

    '''
    generate sample payload
    '''
    def __gen_properties(self, entity_name, id=0, data=0):
        properties = {
            'collection': entity_name,
            'key': self.__accessKey,
            'username': self.__user
        }
        # smaple_id = ['5b2a10190d7dceabda2fe3bb', '5b2a10180d7dceabda2fe3ba', '5b15d6e854a3e5117c7c7429']
        # sample_data = []
        if id == 1:
            properties['_id'] = id
        if data:
            properties['data'] = data

    def __gen_parameter(self, params, description, object_name):
        param = {
            'in': 'body',
            'name': 'body',
            'description': description,
            'required': True,
            'schema': {
                '$ref': '#/definitions/' + object_name
            }
        }
        params.append(param)

    '''
    use for building sample data structure
    '''
    def __define_object(self, object_name, properties):
        self.__json['definitions'][object_name] = {
            'type': 'object',
	        'properties': properties
        }

if __name__ == '__main__':
    gen = ApiGenerator()
    gen.set_basic_path('http://localhost:2000', 'one_to_one')
    gen.set_access_key('...')
    gen.set_user_name('danny')
    gen.add_entity('class1')
    gen.add_entity('class2')
    gen.generate_file('./')