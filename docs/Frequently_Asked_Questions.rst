==================================
Frequently Asked Question about SR
==================================

.. contents:: Table of contents
    :depth: 1
    :local:

Questions regarding the Full Node in private networks
----------------------------------------------

1. Do I need to delete other addresses when replacing genesis.block.witnesses under config.conf with the address string given upon registration on https://trxscan.org/?

2. After replacing the seed.node.ip.list with the IP-address of my own public network and entering the command "java -jar java-tron.jar", how can I test if the deployment has been successful? Are there any testing interfaces or commands such as the "redis" command (which sends a ping to a server and gets a ping back from the server) for a successfull deployment?

Questions regarding the Super Node in private networks
-----------------------------------------------

1. On a private network-environment, what relation exists between a Super Node and a Full Node? Is it preffered to deploy a Super Node over a Full Node?

2. As user voting is determining Super Node selection in private networks, do i need to submit any application materials to the TRON foundation to be approved as a Super Node?

3. Why is data in private environments continously synchronized and why is the journal still continously updated to all other nodes? What is the difference between a private and a public environment then?

Questions regarding operations in public networks
-----------------------------------------

1. Which amount of memory is currently supported by the java software? What performance does a processor need to have in order to run the node software?

2. What amount of data traffic can I expect? Has the data to be spread out to many hosts or will it be enough to just provide several nodes myself?

3. Q: What ports should be opened to be externally accessible? 
    A: Ports 18888 and 50051.

4. Upon successful token issuance, how do I change the status from “not started yet” to “participate”?

Questions regarding error occurances/messages for Super Nodes
-----------------------------------------

1. How can I interpret the following error message?
    
    17:02:42.699 INFO [o.t.c.s.WitnessService] Try Produce Block  17:02:42.699 INFO [o.t.c.s.WitnessService] Not sync 

Questions regarding block generation by Super Nodes
-----------------------------------------

1. Q: Do Super Nodes produce blocks in rotation? At what speed are the blocks produced? Will my node be removed from the list of Super Nodes if no heartbeat message is sent to the network for 24 hours? 
    A: Yes, Super Nodes are taking turns in producing blocks. Within the current testing environment the block production rate is 1 Block per 5 seconds. TRON will calculate the miss rate of the Super Node and, in case of its production rate being too low, it will be removed from the list.

2. Q: If a Super Node cannot connect to the TRON network, how long will it take to be able to connect to the network again? 
    A: As long as a voting cycle to recover service, but its block production rate will be taken into permanent record.

3. Q: What’s the formula of the miss rate of Super Nodes’ block production? 
    A: “The number of blocks which supposedly should have been produced but weren’t” will be taken into count. The number will keep accumulating and not be cleared.

4. F: Ist die Testversion oder der Quellcode des Super Node Servers verfügbar? 
    A: Yes, they are open-source and can be found at https://github.com/tronprotocol/java-tron.

5. Q: How do I know if my test Super Node is running?

6. Q: Based on this command: java -jar java-tron.jar -p yourself private key --witness -c yourself config.conf(Example：/data/java-tron/config.conf, how do I know that I am running a Super Node?

7. Q: What are some command-line commands that can generate an address to be sent to TRON? Is web wallet the only way?

8. Q: If we want to test block production and other functions of the Super Node, do we need your votes to first become elected? 
    A: We will vote for you during your test trial.

9. Q: How do we know if our own node has produced any blocks? 

10. Q: Will block production speed be 1 block / 5 seconds initially when the main-net launches? What is the expected timeline for this speed to reach 1 block / 3 seconds? A: As soon as the main-net launches, the block production speed will be 1 block / 3 seconds.

11. Q: Is the TRON Foundation planning to halve the reward of TRX per block that is given out as reward? If so, when? 
    A: The TRON Foundation is currently not planning to halve the TRX reward per block in the future.

12. Q: If any of the 27 nodes malfunctions, will it be detected automatically and disqualified from elections? Will it remain as a Super Representative if such thing occur? If it won't, how and when it can regain the status? 
    A: An event of incompetency & missed block rates will be kept permanently and will be public. We expect voters to make a rational judgement by not voting for that particular SR in future voting cycles.
    
Questions on the Super Representative election
-----------------------------------------

1. Q: Why I can't see any votes for my node at https://tronscan.org/#/network even though I’ve just submitted 2 million votes for it in the current voting round? 
    A: Results are updated every 6 hours, and announced only after current round of voting ends.

2. Q:The amount of votes one holds is equivalent to the amount of his/her holding of TRX, so one vote can be made for one TRX, right? And votes can be casted to more than one Super Representative candidate? 
    A: Every TRX equals one vote can only be casted for one candidate.

3. Q: Since TRX is required to obtain the right to vote, do we need to deposit a certain amount of TRX into Tronscan wallet?
    A: Yes, TRX deposit is needed for application for witness node and for voting.

4. Q: Is there a threshold for the daily election of 27 Super Representatives? Or is it encouraged to compete freely? 
   A: Free competition. Solicit the votes if you want them.

5. Q: Will TRX rewards be distributed evenly among these 27 Super Representatives or based on their hashrate? 
   A: As they produce blocks in rotation, the distribution of reward is irrelevant to hashrate.

6. Q: If large mining operations run for the election, is hashrate exceeding 50% a possibility? 
   A: No.

7. At the speed of one block every 3 seconds, 32 TRX per block will be rewarded to the corresponding node, right? Based on the number of transactions on TRON’s public blockchain, will blocks be produced every second?

8. Q: What does the community support plan in the guidelines refer to? 
   A: it can be understood as the budget and attention to community development.

9. Q: Does voting consume TRX? 
   A: Voting does not consume your TRX.

10. Q: Does the status of Super Representatives only last for 24 hours? 
    A: Yes. But if the results of the next election remains the same, the status will be maintained.

11. Q: Information on my node is not included in either of the two configuration nodes, namely build/resources/main/config.conf and build/resources/main/config.conf in the wallet. Is it still possible to discover my node and proceed to block production? 
    A: Set your own private key in the configuration file. With a successful vote a block will be produced.

12. Q: How should I configurate my node after I’ve generated my private key? A: Find localwitness within the configuration file and set your private key for the voting account.

Others
----------------------------------------------

1. Q: Where can I find the file for RPC interface? 
   A: https://github.com/tronprotocol/documentation/tree/master/TRX

2. Q: How do I specify the data storage directory when I activate my node? 
   A: Currently we can’t specify data storage directory yet. This function will be made possible in the upcoming version.

3. Q: Can nodes serve as wallets? 
   A: There is a RPC interface for wallet on nodes, but no command can call the wallet directly. Wallets on full nodes can be used through the wallet-cli(commandline wallet) on another repo.

4. Q: I don’t need to calculate my own address with the private key generated according to the file, do I? 
   A: You don’t have to worry about private key generation once you’ve successfully registered for an account. All you need to do is log in with you pin-code to access your address.

5. Q: Is there a specific file to the calling of API like Bitcoin and Ethereum do? 
   A: We are still enlarging our collection of files which is not yet adequate. A new file on rpc-api for wallet has just been added to the Documentation repository.

6. Can Solidity Node and Full Node be employed on the same machine? Since we can’t specify data directory, will there be consequences to the two nodes’ sharing data?

7. Q: Without Txid, how can we tell the users to inquire the transaction after our transfer? 
   A: For now there is no transaction id or service charge. Transaction id is in development.

8. Q: Do Solidity Nodes synchronize blocks in accordance with Full Nodes? 
   A: Yes.

9. Q: Is gateway for the connection to Solidity Nodes? 
   A: Solidity Nodes are set up for the storage of irrevocable blocks, a few blocks behind Full Nodes, so they are more suitable for the confirmation of transfer. You can connect to both Solidity Node and Full Node through gateway.

10. Q: Listaccounts is a list of all addresses in the network? 
    A: For now, yes. But we are uncertain if that’s going to change, because we need to further think it through as the address base if enourmous.

11. Q:  How many decimal places is there for the balance? 
    A: Six.

12. Q: Is the machines of the nodes in Beijing? Is the wall an issue? 
    A: Only 39.106.220.120 is in Beijing. The rest are in the US, Europe and Hong Kong.

13. Q: Can token holders hold trx on tron.network for main-net conversion. If not what other wallets may be capable, or if only exchanges.
    A: No wallets are capable. Only exchanges.

14. Q: In regards to TRON wallets, how many wallets are currently created.
    A: As far as I know, we already have a cli wallet, a web wallet and an ios wallet. And I believe after the programming contest there will be plenty well-designed wallets.

15. Q:Is 25Gbps a requirement or is 10Gbps satisfactory, or what is the threshold that is acceptable?
    A: There is no hard requirement for the network TRON Power(TP). The specification we gave is just an advice.

16. Q: The people outside of the top 27 but in the top 100, are they ranked in order, 28-100 or is there an algorithm to just select who would be next if someone is voted out?
    A: For testnet we now just simply pick top 27 nodes with most votes. For mainnet and future testnet we may chose a different algorithm to add some randomness to part of the SR election.

17. Q: Is a well formed technical plan all we need, or must we have the hardware before applying.
    A: The technical plan has two parts:1 before June 26 the first election & 2 after June 26 the first election. The second part just need the plan. For the first part you can only have the plan for now but only after you have hardware we can test your node and tell everyone "yes, they do have a test node."Applying to be a SR has no direct connection to qualifying a SR.
    
For the specific definition of API, please refer to the following link:
----------------------------------------------------------------------

https://github.com/tronprotocol/java-tron/blob/develop/src/main/protos/api/api.proto

Frequently used APIs:
---------------------

Get general info of the wallet (similar to bitcoin getinfo)

GetAccount

Get balance of an address (similar to bitcoin getbalance)

GetAccount

Create a new address (similar to bitcoin getnewaddress)

You can create an address at the local system.

And you can create a new address on blockchain by calling rpc api createAccount, TransferAsset or CreateTransaction (TransferContract) to make a transfer from an existing account to the new address.

Retrieve the list of transaction history by address (similar to bitcoin listtransactions)

GetTransactionsFromThis

GetTransactionsToThis

check address is valid or not (regex or API command)

Local check--- After decode58check at local, you can get a 21-byte byte array starting with 0x41.

If you want to verify whether an address exists on the blockchain, you can call GetAccount.
