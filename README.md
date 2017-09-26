# Templated Solidity

### Jinja + Solidity = Smart Templates (tsol, pronounced teasle)

```pip install tsol```

We templated Solidity code so that we can reuse and deploy common contracts with ease and start to create better interfaces for things such as ERC20 token creation and smart asset generation. So instead of copying and pasting some Solidity code from some wiki, we can store all the commonly used contracts on Flora in a way that allows them to be simply modified with a JSON payload. That way, we keep the standardization where needed, and pop out the customizable metavariables when we need to.

Thus, Templated Solidity.

So imagine this. You want dynamically produced data models for a database blockchain app using Ethereum. You can't create dynamic structs in Solidity. So instead, let's create templated smart contracts from a base contract instead.

```contract Table {
    address owner;
    function Table() {
        owner = msg.sender;
    }
    
    struct Model {
        {% for key, value in struct.iteritems() %}
            {{ key|e }} {{ value|e }};
        {% endfor %}
    }
    
    mapping (uint => Model) lookup;
    
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    
    function get(uint id) returns (Model bb) {
       return lookup[id];
    }
    
    function set(Model b, uint id) onlyOwner returns (Model bb){
       lookup[id] = b;
       return lookup[id];
    }
}```

And you would just need to create some sort of dictionary object to go inside the struct like so:

```book = {
	title : string,
	author : string,
	owner : address
	}```

Now you have a way to create infinate numbers of data models on a blockchain.

Enjoy!