===========
Start Private Blockchain
===========

.. contents:: Table of contents
  :depth: 1
  :local:

Private blockchain. Start a witness node locally, starting from the genesis block and not connecting or synchronizing with other nodes or testnet.

**Configuration instructions**

1. The configuration file is located at ``resource/config.conf``;
2. The parameter ``seed.node.ip.list`` is used to specify seed nodes(Synchronize main chain);
3. The parameter ``genesis.block.witnesses`` is used to specify the initial witnesses. It currently contains 11 default witnesses;
4. The parameter ``node.p2p.version`` is used to indicate the main chain, the testnet is configured as 0;
5. The parameter ``localWitness`` is used to specify this node's account holder and its private key, the witness needs to be in ``genesis.block.witnesses``;
6. Add ``--witness`` to the startup parameter to specify this node as the witness node.

**Modify configuration**

1. ``seed.node.ip.list``, Do not need to connect to other nodes, modify it to null here;
2. ``genesis.block.witnesses``, At least 2 are reserved here, one of which is used as a local witness;
3. ``node.p2p.version``, Modify to other values, such as 100, for different links from other networks;
4. ``localWitness``, Specify the node's account holder and its private key, the information could Intercepted from the genesis.block.witnesses;
5. Add ``--witness`` to the startup parameter to specify this node as the witness node;
6. Start the service(``./gradlew run -Pwitness``).