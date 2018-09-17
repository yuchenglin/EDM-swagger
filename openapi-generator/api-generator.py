import json
api = {
	'swagger': '2.0',	
}
api['info'] = {
	    'version': '1.0.0',
	    'title': 'Test API Reference'
	    }
api['host'] = 'petstore.swagger.io'
api['basePath'] = '/dbName'
api['tags'] = []
api['tags'].append({
		'name': 'Entity',
		'description': 'Everything about Entity'
	})
# append other entity tag ...

# api details
api['paths'] = {}
api['paths']['/class1/create'] = {}
api['paths']['/class1/create']['post'] = {
	'tags': ['Entity'],
	'summary': 'Summary of this API',
	"consumes": [
      "application/json",
      "application/xml"
    ],
    "produces": [
      "application/xml",
      "application/json"
    ],
    "parameters": [
      {
        "in": "body",
        "name": "body",
        "description": "Pet object that needs to be added to the store",
        "required": True,
        "schema": {
          "$ref": "#/definitions/SampleData"
        }
      }
    ],
    "responses": {
      "405": {
        "description": "Invalid input"
      }
    }
}


# definition
api['definitions'] = {}
api['definitions']['SampleData'] = {
	'type': 'object',
	'properties': {
		'collection': {
			'type': 'string'
		},
		'data': {
			'type': 'string'
		},
		'key': {
			'type': 'string'
		},
		'username': {
			'type': 'string'
		}
	}
}

# json = json.dumps(api, indent=4)
# print(json)
with open('../test.json', 'w') as outfile:
    json.dump(api, outfile)




