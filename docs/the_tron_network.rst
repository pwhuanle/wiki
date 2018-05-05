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

• A *node* is a server that shares information on the p2p blockchain  
• A *witness node* is a node that is configured with a private key and is available to produce blocks.  
• A *super representative*  (aka Super Delegate) is a witness node that has been elected to produce blocks  
• Full Node (aka seed node) runs without a private key  
• Solidity node is a wallet server  
- Super Representative produces blocks  
- Other SRs validate the block  
- Full nodes are specified in the witness node's config file so only trusted nodes are used.  
- Full nodes keep a copy of the blockchain and also pass new transactions to the witness producing the block.  
- Solidity nodes only keep a copy of the blockchain, and not the pending transactions. All info available to the wallet is validated.  

The TRON Network is built on a system of ascending levels of trust. 

