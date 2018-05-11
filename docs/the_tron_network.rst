============
The TRON Network
============

.. contents:: Table of contents
    :depth: 1
    :local:

Connecting to the Network
-------------------------

Test Network
------------

Setting up a local private testnet
----------------------------------
The TRON Network is built on a system of ascending levels of trust. 

The witness node designates seed nodes in its config file. Java-tron learns of those when it runs. The witness node's IP address is not listed, its presence is known only through its connections to the seeds. Seed nodes advertise the blockchain for the witness nodes.


• A *node* is a server that shares information on the p2p blockchain  
• A *witness node* is a node that is configured with a private key and is available to produce blocks.  
• A *super representative*  (aka Super Delegate) is a witness node that has been elected to produce blocks  
• Full Node runs without a private key  
• A *solidity node* is a wallet server  
• A *seed node* is a full node that is designated in the witness node config
+ Super Representative produces blocks  
+ Other SRs validate the block  
+ Full nodes & seed nodes conduct most of the network traffic
+ Nodes pass new transactions to the witnesses
+ Newly created and unvalidated blocks are passed from the SR to the witnesses by the Seed nodes
+ A Solidity Node should have its own Full Node (slave node) to ensure data availability.
+ Seed nodes keep a copy of the blockchain and also pass new transactions to the witness producing the block.  
+ Solidity nodes can only access a validated copy of the blockchain, and not the pending transactions.

The end user interfaces with web-wallet client which connects to a Solidity node API. The solidity node gets its data from its slave node which in turn gets its data from the seed nodes.

