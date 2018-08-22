====================
TRON Virtual Machine
====================

.. contents:: Table of contents
    :depth: 1
    :local:

Introduction
------------

TRON Virtual Machine (TVM) is a lightweight, Turing complete virtual machine developed for the TRON's ecosystem. Its goal is to provide millions of global developers with a custom-built blockchain system that is efficient, convenient, stable, secure and scalable.

The TVM supports DPOS and can connect seamlessly with the existing development ecosystem. The TVM will be compatible with EVM environments at the beginning, so that, instead of having to learn a new programming language, the developers can build, debug and execute smart contracts in a mixed environment with Solidity and other languages. Once you’ve built and uploaded your smart contract to TRON’s mainnet, it will be executed on the TVM of the SR node in order to be isolated from external connections.

Furthermore, the TVM covers the concept of Bandwidth. Different from the Gas Mechanism on Ethereum’s EVM, operations of transaction or smart contracts on the TVM are free, with no tokens consumed. Technically, the executable computational capacity of the TVM is not restricted by the total holding of tokens.

Features of TVM
~~~~~~~~~~~~~~~

1. Lightweight

    The TVM adopts a lightweight architecture with the intent of reducing resource consumption to guarantee system performance.

2. Stability and security

    With a meticulous design paradigm and fine-grained underlying operation code, the TVM can guarantee the preciseness of every step of a computation, which minimizes ambiguities. Out of security reasons, transfers and smart contracts execution cost only bandwidth points, and not TRX, which exempts TRON from being attacked like Ethereum due to its gas consumption mode. Stability of bandwidth consumption is achieved while the cost of each computational step is fixed.

3. Compatibility

    Currently the TVM is compatible with the EVM and it will also be with more mainstream VMs in the future. Thereby, all smart contracts on EVM are executable on TVM. Because it connects seamlessly to the existing development ecosystem, higher efficiency can be achieved by the developers. It's not necessary for them to learn a new programming language. They can use mainstream programming languages such as Solidity to develop, debug and compile smart contracts in the mixed environment, which greatly reduces development costs.

4. Developer-friendly

    Thanks to the TVM's bandwidth setup, development costs are reduced and developers can focus on the logic of their contract code. The TVM also offers convenience all-in-one interfaces for the deployment, triggering and viewing of contracts.

    The following interfaces are available on TRON Wallet-CLI:

    + deploycontract(password, contractAddress, ABI, code, data, value)
    + triggercontract(password, contractAddress, selector, data, value)
    + getcontract(contractAddress)

Developers can call these interfaces to deploy, trigger or check smart contracts.

How TVM works
~~~~~~~~~~~~~~

.. image:: https://github.com/tronprotocol/wiki/blob/master/docs/img/Virtual_Machine/虚拟机的副本.png
    :width: 842px
    :height: 915px
    :align: center


The above flowchart shows how TVM works:

Compilation of TRON smart contracts → Execution and computing engines of the VM → Interoperation service layer for external interfaces

Put simply, the flow is as follows:
+ Currently, the TVM is compatible mainly with Solidity. The compiler translates Solidity smart contracts into bytecode readable and executable by the TVM.
+ A virtual machine processes data through opcode, which is equivalent to the operation logic of a stack-based finite state machine.
+ The TVM accesses blockchain data and invokes the External Data interface through the interoperation layer.

Future development of TVM
~~~~~~~~~~~~~~~~~~~~~~~~~

1. More developer-friendly debugging tools

    Tron will be committed to the development of optimized debugging tools and the establishment of standardized symbol and data format for the improvement developers efficiency.

2. Fulfillment of diversified processing demands

    Different from the gas consumption mechanism for every transaction on EVM, there is no charge on TVM. Each operation only consumes bandwidth, which will be released within a certain period of time after the completion of the transaction. It takes developers very little effort to develop smart contracts with more complex logic. It is our belief that, besides being used for digital asset transactions, smart contracts could also be suitably applied to areas such as game development, financial risk modeling and scientific computing. The design of the TVM inherently supports multi-scenario tasks and further optimizations of processing speed, response time and floating point compatibility.

3. Improvement of Just-In-Time (JIT) compilation speed and integration of WebAssembly

    Improved JIT compilation speed is conducive to faster interpretation and optimized compilation of local code.  

Meanwhile, TRON is planning to further optimize its TVM based on the WebAssembly (WASM). WebAssembly, spearheaded by Apple, Google, Microsoft and Mozzila, is designed to break bottlenecks of current Web browsers and can be generated through compiling C/C++ and other programming languages.  

After the Integration of the WASM, the TVM will be able to provide high performance and high throughput for blockchain to cope with complex scenarios.

Guide for smart contract deployment on TVM
-----------------------------------------

1. Compile contract

    Contract compilation address: https://remix.ethereum.org

2. Get ABI and bytecode

.. code-block:: shell

    pragma solidity^0.4.11;

    contract Tron {
        uint256 tron;
        constructor() public { }


            function set(uint256 number) public returns(bool){
                tron = number;
                return true;
            }
    }

ABI: [{“constant":false,"inputs":[{"name":"number","type":"uint256"}],"name":"set","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]

ByteCode：

608060405234801561001057600080fd5b5060c48061001f6000396000f300608060405260043610603f5760
00357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe
47b1146044575b600080fd5b348015604f57600080fd5b50606c6004803603810190808035906020019092919
05050506086565b604051808215151515815260200191505060405180910390f35b60008160008190555060019
0509190505600a165627a7a723058209791df3f67e9af451c35d7ae55bda5e352764f6a38ea23fa850b1c1fe1
bc72e90029

3. Deploy contract

    Wallet-cli-vm branch: https://github.com/tronprotocol/wallet-cli/tree/wallet-cli-vm

    Java-tron-vm branch: https://github.com/tronprotocol/java-tron/tree/develop_vm

    Password: password of client-end wallet

    ContractAddress: customized contract address (in Tron’s required format)

    ABI: interface description

    Data: parameters of the initial function

    Value: reserve

    deploycontract(Password, ContractAddress, ABI, Code, Data, Value)

4. Invoke contract

    Selector: function selector

    Data: parameters

    triggercontract(Password, ContractAddress, Selector, Data, Value)

5. Check contract

    getcontract(ContractAddress)

    The above is an introduction of Tron Virtual Machine and a guide to deployment. We welcome everyone to check out TVM and give us your thoughts and suggestions. We will continue to perfect and update TVM for optimal performance on TRON main
