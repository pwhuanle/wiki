==================
Account Management
==================

.. contents:: Table of contents
    :depth: 1
    :local:

Accounts
--------

Keyfiles
--------

Creating an account
--------------------

Accounts cannot be created directly. New accounts can only be created by making transfers to inexistent accounts, with a minimum transfer of 1 TRX.

Command line operation flow example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    cd wallet-cli

    ./gradlew build

    ./gradlew run -Pcmd

    RegisterWallet 123456      (password = 123456)

    login 123456

    getAddress                 (Print ``address = f286522619d962e6f93235ca27b2cb67a9e5c27b``, backup it)

    BackupWallet 123456        (Print ``priKey = 22be575f19b9ac6e94c7646a19a4c89e06fe99e2c054bd242c0af2b6282a65e9``, backup it) (BackupWallet2Base64 option)

    getbalance                 (Print 'Balance = 0')

    //set genesis.block.assets address to yours. restart java-tron.

    getbalance

    assetIssue 123456 testAssetIssue00001 10000000000000000 1 100 2018-4-1 2018-4-30 1 just-test https://github.com/tronprotocol/wallet-cli/

    getaccount  f286522619d962e6f93235ca27b2cb67a9e5c27b

    (Print balance: 9999900000

    asset {

    key: "testAssetIssue00001"

    value: 10000000000000000

    })

    (cost trx 1000 trx for assetIssue)

    (You can query the trx balance and other asset balances for any account )

    TransferAsset 123456 649DDB4AB82D558AD6809C7AB2BA43D1D1054B3F testAssetIssue00001 10000

Migration
---------

Timeline
~~~~~~~~

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/TRX_Migration/Timeline的副本.png
    :width: 842
    :height: 274
    :align: center

1.Launch Prep (Now – 5/31)

- Complete mainnet function testing.
- Complete wallet product testing.
- Complete blockchain explorer testing.

2.Mainnet Testing (6/1 – 6/24)

- 6/1 – 6/24 (GMT+8), maintain stable operations after mainnet launch. Data wipe on June 24 (GMT+8).

- Users get test tokens from designated links and test on mainnet’s TRON wallet. Community developers test mainnet functions.

Mainnet testing period: June 1, 2018 00:00 (GMT+8) – June 24, 2018 23:59 (GMT+8).

Mainnet will launch after the mainnet testing period. Genesis block will launch on June 25, 2018 00:00 (GMT+8).

3.Genesis Block & Token Migration

Official launch of the genesis block will be on June 25 00:00 (GMT+8).

Token migration:

- Exchanges: ERC20 TRX tokens will be transferred to TRON. TRON will transfer mainnet tokens to exchanges.

- SR: Express TRX migration channel for Super Representative candidates can ensure unimpeded application for candicacy and a certain amount of initial votes.

4.SR Elections & Rewards

Users vote for SR candidates using wallets. SRs are responsible for transaction packaging and block generation.

Developer Guide
~~~~~~~~~~~~~~~

- Please note that you have to finish development before May 31st (GMT+8).
- Please note that the mainnet testing will be from June 1 to June 24 (GMT+8) and please participate.
- Please submit your wallet versions to TRON before June 15th (GMT+8).

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/TRX_Migration/Gudiance_for_developer的副本.png
    :width: 842
    :height: 276
    :align: center

1.	Completion of development: Before May 31st (GMT+8)

Announce the github address of each wallet, download the links for community and users to test and experiment.

2.	Wallet test iteration: June 1-June 24 (GMT+8)

Promote wallets for community and users to test and experiment, get feedback and iterate wallets.

3.	Select the official recommended wallet for each platform (June 15, GMT+8)

On June 15th (GMT+8), the TRON team will review and select the official recommended wallet for each platform. The official recommended wallets can be submitted at any time, and TRON can add recommendations at any time.

4.	Wallet officially launched (June 25, GMT+8)

TRX users vote for SR candidates using wallets.

Exchange Guide
~~~~~~~~~~~~~~

- Please take note of token migration order.
- Please note that TRX withdrawals will be suspended from June 21st to June 24th (GMT+8). Both TRX deposits and withdrawals on exchanges will be suspended on June 25th (GMT+8). Deposits and withdrawals of TRX will resume on June 26th.
- Please contact Tron Foundation to receive mainnet tokens.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/TRX_Migration/Gudiance_for_exchange的副本.png
    :width: 842
    :height: 457
    :align: center

1.	TRX withdrawals will not be allowed:

TRX withdrawals will not be allowed from June 21st to 24th (GMT+8).

2.	TRX deposits and withdrawals on exchanges will not be allowed:

Deposits and withdrawals are not allowed on June 25th (GMT+8).

3.	ERC20 TRX tokens will be transferred to TRON. TRON will transfer mainnet tokens to exchanges:

Exchanges will transfer ECT20 TRX tokens to TRON and TRON will burn them and transfer mainnet tokens to exchanges.

4.	System is updated and supports deposits and withdrawals of mainnet tokens:

Exchanges update their systems which supports the wallet function of mainnet tokens instead of the function of ERC20 TRX.

5.	A notice will be published on resumed deposit and withdrawal functions:

After confirmation of exchanges, deposits and withdrawals of TRX will resume.

6.	Permanent token-exchange counter:

Permanent token-exchange counter designated by TRON will retain the deposit channel for ERC20 TRX. Users can migrate from ERC20 TRX to mainnet tokens on a regular basis.

.. Note:: Exchanges don’t need snapshots and don’t need to suspend trading of TRX.

SR Guide
~~~~~~~~

- Please pay deposit before May 31st (GMT+8).
- Please take part in the mainnet test voting and run test nodes from June 1st to June 24th (GMT+8).
- Please call on your supporters to vote on June 26th.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/TRX_Migration/Gudiance_for_SRs的副本.png
    :width: 842
    :height: 245
    :align: center

1.	Campaigning 4/27-5/31 (GMT+8)

SR election campaigning period allows SRs to attract more votes from TRX holders.

2.	Candidates transfer deposit:

Candidates will be informed on May 15th (GMT+8) to transfer

200K TRX to Tron Foundation by May 31st as deposit. Deposit will be returned to designated Tron mainnet addresses at midnight June 25th (GMT+8).

3.	Election test period: 6/1 - 6/24 (GMT+8)

Supporters can do test voting. Run test nodes and generate blocks.

4.	Candidates’ deposit is returned:
Deposit will be returned to designated Tron mainnet addresses at midnight June 25th (GMT+8).

5.	Apply to become an SR candidate using the wallet and call on supporters to vote.

6.	Become official SRs:

27 candidates who receive most votes will become official SRs. They are eligible to generate blocks and get rewards in TRX.

Users Guide
~~~~~~~~~~~

- Please keep an eye on token migration.
- Please note that the test voting will be from June 1 to June 24 (GMT+8).
- Please note that the official voting will be on June 26 (GMT+8).

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/TRX_Migration/Gudiance_for_user的副本.png
    :width: 842
    :height: 183
    :align: center

There are three scenarios:

1. If your TRX is held on an exchange, no action is required.

2. If your TRX is held in a wallet, please follow the steps below:

- From June 21 to June 24 (GMT+8), TRX withdrawals on exchanges will be suspended. Users must deposit TRX to an exchange before June 24, 2018 (GMT+8).
- On June 25 (GMT+8), both TRX deposits and withdrawals on exchanges will be suspended.
- Withdraw TRX to wallets and vote.

From June 26th (GMT+8), deposits and withdrawals of TRX will resume. Users need to withdraw TRX and transfer to wallets  in order to vote.

3. If your TRX is held in a wallet and you were not aware of the migration notice, or see the notice after June 25th, please visit our permanent token-exchange counter to exchange your tokens for mainnet TRX.

4. If your TRX is held in a wallet and you were not aware of the migration notice, or saw the migration notice after June 25th, please visit our permanent token-exchange counter to exchange your tokens for Mainnet TRX.

.. Note:: User's token migration is not perceptible. Please deposit TRX to an exchange before June 25th (GMT+8), and TRX's normal trading will not be affected.

Transition manual for exchanges and TRX
---------------------------------------

It is suggested that exchanges deploy a Full Node and a Solidity Node in Tron blockchain for improved security. The Full Node will synchronize all data in the blockain, while the Solidity Node will only synchronize data from irreversible blocks already confirmed. Transaction broadcasting can be conducted through the Full Node. With the Solidity Node, users can check their account balance.

1，The prerequisite of Full Node and Solidity Node deployment:

- Installation of JDK 1.8 (JDK 1.9 not supported for the moment).

- For Linux Ubuntu systems, please make sure to install Oracle JDK 8 instead of OPEN JDK 8.

2，The deployment of Full Node is as follows:

.. code-block:: shell

    git clone https://github.com/tronprotocol/java-tron.git

    cd java-tron

    ./gradlew clean shadowJar

    ./gradlew run

With these, the Full Node is set up and ready for the synchronization of blockchain data, which is complete upon the alert of “Sync Block Completed!!!”.

3，The deployment of Solidity Node is as follows:

.. code-block:: shell

    git clone https://github.com/tronprotocol/java-tron.git

    cd java-tron

    ./gradlew clean shadowJar

    ./gradlew run -PmainClass=org.tron.program.SolidityNode

With these, the Full Node is set up and ready for the synchronization of blockchain data, which is complete upon the alert of “Sync with trust node Completed!!!”.

4，Connecting grpc-gateway to SolidityNode (optional step)

- Install go1.10.1

.. code-block:: shell

    go get -u github.com/tronprotocol/grpc-gateway

    cd $GOPATH/src/github.com/tronprotocol/grpc-gateway

    go run tron_http/main.go

GRPC interface is available on Solidity Node, providing Http interface for gRPC interface through grpc-gateway. Please note that this is an optional step providing Http interface for gRPC interface for the convenience of users.

5，Account generation

- Random generation of 32 byte secret key d:

.. code-block:: shell

    d = ab586052ebbea85f3342dd213abbe197ab3fd70c5edf0b2ceab52bd4143e1a52

- Calculating public key with private key: ecc SECP256K1N curve，P = d*G public key P

.. code-block:: shell

    P = 5ed0ec89eaec33d359b0632624b299d1174ee2aec5a625a3ce9145dd2ba4e48e049327d454fbf7ec700a9464f87dc4b73a592e27fd0d6d1fe7faf302e9f63306

- Calculating address with public key：sha3-256(P)

.. code-block:: shell

    Hash = c7bcfe2713a76a15afa7ed84f25675b364b0e45e2668c1cdd59370136ad8ec2f

- Reserve the last 20 bytes of Hash

.. code-block:: shell

    End20Bytes = f25675b364b0e45e2668c1cdd59370136ad8ec2f

- Add a0(testNet) or b0(mainNet) before End20Bytes

.. code-block:: shell

    address = a0f25675b364b0e45e2668c1cdd59370136ad8ec2f

- Convert address to base58check format：(bip-13)

.. code-block:: shell

    hash0 = sha256(address);
    //hash0=cd398dae4f5294804c83093ee043c13fa3037603a4e7d76ed895bb3aa316e93
    hash1 = sha256(hash0);
    //hash1=7e5ff07e733c2bb52e56cef8cfb5af6f61e50d515eb3a57e38b5889a1f653ac8

- checkSum = the first 4 bytes of hash0

.. code-block:: shell

    //checkSum = 7e5ff07e
    addressCheckSum = address || checksum
    //addressCheckSum = //a0f25675b364b0e45e2668c1cdd59370136ad8ec2f7e5ff07e
    addressbase58 = base58Encode(addressCheckSum)
    //addressbase58=
    //27mAse8NBVPM4M7Mpp5sxZcLcYkpSqrcoHX

.. Note:: All addresses of transactions and bock storage should be in byte[] as it has 14 bytes less than the base58check format (21 vs 35). Besides the initial address and the witness address in the configuration file, which adopt the base58check format, all other addresses in blockchain nodes should maintain their original format. Where it involves input and output for the wallet, format conversion has to be made, but what is presented to users should be in base58check format. Addresses should be validated before being converted to base58check format.

6，Connecting with Solidity Node or grpc-gateway to check your balance

With the address generated in step 5, connect with Solidity Node to view balance through gRPC interface GetAccount. Or you can access http://localhost:8080/Wallet/GetAccount interface for your balance through grpc-gateway.