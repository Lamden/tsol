# tsol libs
from solc import compile_source, compile_standard
from jinja2 import Environment
from jinja2.nodes import Name
from io import BytesIO

BASE_JSON_PAYLOAD = '''{"language": "Solidity", "sources": {
				"{{name}}": {
					"content": {{sol}}
				}
			},
			"settings": {
				"outputSelection": {
					"*": {
						"*": [ "metadata", "evm.bytecode", "abi", "evm.bytecode.opcodes", "evm.gasEstimates", "evm.methodIdentifiers" ]
					}
				}
			}
		}'''

def get_template_variables(fo):
	nodes = Environment().parse(fo.read()).body[0].nodes
	var_names = [x.name for x in nodes if type(x) is Name]
	return var_names

def render_contract(payload):
	sol_contract = payload.pop('sol')
	template_variables = get_template_variables(BytesIO(sol_contract.encode()))
	assert 'contract_name' in payload
	name = payload.get('contract_name')
	assert all(x in template_variables for x in list(payload.keys()))
	template = Environment().from_string(sol_contract)
	return name, template.render(payload)

def load_tsol_file(path=None, payload=None):
	assert path and payload, 'No path or payload provided.'
	payload['sol'] = path.read()
	name, rendered_contract = render_contract(payload=payload)
	return name, rendered_contract

def does_compile(payload):
	try:
		compile_standard(json.loads(payload))
	except:
		return False
	return True

def compilation_payload_from_paths(template, example):
	code = open(template)

	# turn the example into a dict
	payload = None
	with open(example) as e:    
		payload = json.load(e)
	solidity = load_tsol_file(code, payload)
	return Environment().from_string(BASE_JSON_PAYLOAD).render(name=solidity[0], sol=json.dumps(solidity[1]))