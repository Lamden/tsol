# Templated Solidity

### Jinja + Solidity = Smart Templates (tsol, pronounced teasle)

```pip install tsol```

We templated Solidity code so that we can reuse and deploy common contracts with ease and start to create better interfaces for things such as ERC20 token creation and smart asset generation. So instead of copying and pasting some Solidity code from some wiki, we can store all the commonly used contracts on Flora in a way that allows them to be simply modified with a JSON payload. That way, we keep the standardization where needed, and pop out the customizable metavariables when we need to.

Thus, Templated Solidity.

So imagine this. You want dynamically produced data models for a database blockchain app using Ethereum. You can't create dynamic structs in Solidity. So instead, let's create templated smart contracts from a base contract.

```
pragma solidity ^0.4.14;
    contract Table {
    address owner;
    function Table() {
        owner = msg.sender;
    }
    
    struct Model {
        {% for key, value in struct.items() %}
            {{ value }} {{ key }};
        {% endfor %}
    }
    
    mapping (uint => Model) lookup;
    
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    
    function get(uint id) internal returns (Model bb) {
       return lookup[id];
    }
    
    function set(Model b, uint id) onlyOwner internal returns (Model bb){
       lookup[id] = b;
       return lookup[id];
    }
    {% for key, value in struct.items() %}
    function get_{{ key }}(uint id) returns ({{ value }} a) {
            Model m = lookup[id];
            return m.{{ key }};
        }
    {% endfor %}
}
```

And you would just need to create some sort of dictionary object to go inside the struct like so:

```
example = {
    'contract_name' : 'Book',
    'struct' : {
        'title' : 'string',
        'author' : 'string',
        'owner' : 'address'
    }   
}
```

Then, to compile it, all you have to do is call:

```
tsol.compile(template, example)
```

This then yields the following contract in pure Solidity:

```
pragma solidity ^0.4.14;
    contract Table {
    address owner;
    function Table() {
        owner = msg.sender;
    }
    
    struct Model {
            string author;
            string title;
            address owner;
    }
    
    mapping (uint => Model) lookup;
    
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
    
    function get(uint id) internal returns (Model bb) {
       return lookup[id];
    }
    
    function set(Model b, uint id) onlyOwner internal returns (Model bb){
       lookup[id] = b;
       return lookup[id];
    }
    
    function get_author(uint id) returns (string a) {
            Model memory m = lookup[id];
            return m.author;
        }
    
    function get_title(uint id) returns (string a) {
            Model memory m = lookup[id];
            return m.title;
        }
    
    function get_owner(uint id) returns (address a) {
            Model memory m = lookup[id];
            return m.owner;
        }
    
}
```

Now you have a way to create infinite numbers of data models on a blockchain.

Enjoy!