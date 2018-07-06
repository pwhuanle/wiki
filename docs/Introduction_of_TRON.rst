============
Introduction
============

.. contents:: Table of contents
    :depth: 1
    :local:

What is TRON?
-------------

Architecture
~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/architecture.jpg
    :width: 700px
    :height: 700px
    :align: center

TRON adopts a 3-layer architecture comprised of storage layer, core layer and application layer.

**Storage Layer**

The tech team of TRON designed a unique distributed storage protocol consisting of block storage and state storage.

The notion of graph database was introduced into the design of the storage layer to better meet the need for diversified data storage in the real world.

**Core Layer**

Smart contract module, account management module and consensus module are three modules of the core layer. It’s TRON’s vision to base its functions on a stacked virtual machine and optimized instruction set.

In order to better serve the development of dAPPs, Java is designated as the language for smart contracts, which is to be further supplemented by other high-level programming languages.

In addition, innovations are made to TRON’s consensus on the basis of DPOS to fulfill its special needs.

**Application Layer**

Developers can utilize interfaces for the realization of diverse dAPPs and customized wallets.

The protocol of TRON adheres in entirety to Google Protobuf, intrinsically supporting multi-language extension.

Consensus
~~~~~~~~~

**Improved Consensus Mechanism based on DPOS**

High energy consumption, low efficiency and low TPS are always an issue with POW consensus, which is completely opposite from TRON’s values and design. Under the guidance of our architectural philosophy, we have chosen to adopt the POS mechanism as the basis of TRON consensus. Having gained knowledge on constructive ideas in the blockchain community through research, we made improvements to the DPOS mechanism to meet up with our demands, thereby coming up with the TRON consensus.

**Basic Rules of the Consensus Mechanism**

- Coin holders are to vote for nodes in accordance with their holding of coins with a ballot. And nodes are elected to become what are known as witnesses based on the result of the votes and certain other rules, which tries, to its utmost capacity, to strike a balance between speed of block production and the number of witnesses.

- Meanwhile, compensation will be made to unelected nodes, voters for both elected nodes and unelected nodes, in order to encourage them to run for future elections.

- Witnesses will produce valid blocks successively based on specific distribution rules and success to do so results in the highest reward.

- The vast majority of witnesses are chosen through votes and the rest are selected with an equal chance under a certain algorithm.

Storage Structure
~~~~~~~~~~~~~~~~~

**KhaosDB**

TRON has a KhaosDB in the full-node memory that can store all the new fork chains generated within a certain period of time and supports witnesses to switch their own active chain swiftly into a new main chain.

**Level DB**

Level DB will be initially adopted with the primary goal to meet the requirements of fast R/W and rapid development. After launching the main net, TRON will upgrade its database to an entirely customized one catered to its very own needs.

Token Module
~~~~~~~~~~~~

**Configuration**

Users can customize their own token through TKC (token configuration) functions.

Customizable parameters include, but are not exclusive to, token name, abbreviation, LOGO, total capitalization, exchange rate of TRX, starting date, expiring date, attenuation coefficient, controlled inflation model, inflation period, description, etc.

Users can chose to stay with the default parameters of the system if it’s their option to not customize their own.

**Issue/Deployment**

Users can issue their tokens after setting up the parameters (manually customized or system default).

System comes with operations and functions, and that allow issuers to deploy digital token, which has already been validated and customized. (Customized and validated tokens can proceed to function and operation setup for deployment.)

Customized token is deployed once witnesses successfully validate, and can be freely circulated on TRON network. (Once validated by the witness, customized token is successfully deployed, which enters into online circulation.)

**API**

API is mainly used for the development of client terminals. With API support, token issuance platform can be designed by developers themselves.

Smart Contract/ Virtual Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The smart contract module of TRON allows users to customize contracts to their own needs.

TRON is home to its own virtual machine on which Smart contract operates, allowing for developers to customize for diverse and complex functions.

Third Party Applications
~~~~~~~~~~~~~~~~~~~~~~~~

**Token Deployment Platform**

Third party developers are granted access to TRON’s network for the development of their own platforms. With the use of TRON’s token module, users of these platforms could also customize their own tokens.

**Wallet**

With the wallet users can view their holding of TRX as well as other assets, initiate or take transactions.

**Blockchain Explorer**

Blockchain explorer is used for the viewing of block records, a list of nodes, node deployment and more information on the real-time operation of Tron.

ERC20 Token Migration
~~~~~~~~~~~~~~~~~~~~~

Before the launch of TRON’s main net, the migration from ERC20 to TRX, the official token of TRON, will be initiated by TRON foundation. The migration exchange rate is 1:1. The specificities of migration entails further clarification, to which may involve revision might be made before official execution.

Community Plan
~~~~~~~~~~~~~~~

The community is always an integral part of any blockchain project, so it is our hope to evoke the members’ passion for full participation in TRON’s construction. This is a belief that we have unwaveringly held since the very inception of our project.

There are numerous ways for TRON’s community members to be a part of the project, for instance, through participation in core programming tasks or third-party development through APIs to be opened up by TRON. Furthermore, a wide variety of competitions open to all users will be held for LOGO design, essay writing, poster design, competitive programming, etc.

    - Providing Code Types
    - feat: A new feature
    - fix: A bug fix
    - docs: Files of revision
    - perf: A code change that improves performance
    - refactor: A code change that neither fixes a bug nor adds a feature
    - style: A change in text format (excessive blank space, format proofreading, missing punctuation marks, etc.)
    - test: Addition of missing tests or correction to existing tests

**Reward Plan**

We would like to offer reward to all those who have contributed to the progression and development of TRON’s network and community. A special committee is set up by TRON to conduct close assessment on all participants’ contribution, based on the result of which TRX tokens, gifts, and other forms of reward are offered.


Protocol
~~~~~~~~~

TRON adheres to the Google Protobuf protocol, which covers multiple aspects such as accounts, blocks and transfers.

There are 3 types of accounts: basic account, asset release account, and contract account. Each of those three types has five properties: name, type, address, balance and related asset.

A basic account can apply to be a witness, which possesses other attributes and parameters including voting statistics, public key, URL, history performance, etc.

A block typically consists of several transactions and a blockheader, which is comprised of basic block information like timestamp, root of Merkle tree, parent hash, signature, to name just a few.

There are eight categories of contract transaction: account creation contract, transfer contract, asset transfer contract, asset voting contract, witness voting contract, witness creation contract, asset issuance contract and deployment contract.

Each transaction contains several TXInputs, TXOutputs and other properties.

Signature is required for input, transaction and block header.

Inventory, protocol involved in transfers, is mainly used to inform recipient nodes of transmitted data.

Please find in the appendix the detailed protocol. The specificities of the protocol is subject to change with program upgrading, so please always make reference to the latest version available.

TRON Milestone
---------------

- 2017      Early-Stage

- 2017      TRON Foundation and TRONIX Presale

- 2018.3.31 The launch of testnet.

- 2018.5.31 The launch of mainnet.

- 2018.6.25 ERC20 Token --> TRX Migration completed

Community
---------

TRON community is driven by principles of sharing, equality, freedom of speech and personal expression where community members supporting each other. The TRON community social system provides all supporters and participants with more accessible and comprehensive resources and information on the projects of TRON. All participants will have full freedom with out of any restrictions in talent expression, new ideas suggestions, providing different opinions and taking discussion about different topics, as long as they follow community regulations and being actively engaged in community development at all levels.

Reddit
~~~~~~

To its host of supporters and developers converging here,TRON `reddit <https://www.reddit.com/r/TRONix/>`_ is the dream venue for brainstorming and the exchange of ideas. With a firm belief in the freedom of speech, TRON community as a non-profit community accommodates all perspectives, with the aim for all participants to achieve progress through sharing.

Current Official Subreddits:

    `/r/TRXTrading <https://www.reddit.com/r/TRXTrading/>`_  – TRON trading, price and market.

    `/r/tronsupport <https://www.reddit.com/r/tronsupport>`_ – Support for any TRON-related questions.

Slack
~~~~~

Keeping in touch with outstanding contributors on Github, the tech team of TRON communicates with and finds itself deeply inspired by developers on `slack <https://tronfoundation.slack.com/messages/C6DKKSU8G/details>`_ . The platform makes it easier for developers to discuss and solve technical problems together with the tech team of TRON in a timely fashion. Join us on Slack at our invitation or by your own request. We also welcome developers making a remarkable contribution to be a part of the TRON team.

Gitter Rooms
~~~~~~~~~~~~

Log on to gitter with your github account to participate in TRON’s discussions. Accessible Gitter channels revolve around the topic of a certain database. Please select a suitable channel and topic and maintain the relevance of your posts.

    `java-tron <https://github.com/tronprotocol/java-tron>`_  – about FullNode, the launch of mainnet, testnet.

    `wallet-web <https://github.com/tronprotocol/wallet-web>`_ – blockchain explorer and web wallet developed by community.

    `wallet-cli <https://github.com/tronprotocol/wallet-cli>`_  – the command line interface wallet.

TRON Forum
~~~~~~~~~~~

    http://tronsr.org/

TRON Foundation
---------------

Forging ahead with the development of new technologies and applications jointly with all developers, TRON Foundation is devoted to the healthy development of TRON ecosystem.

TRON Foundation open to the community
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    `Official Website <https://tron.network/en.html>`_

    `Twitter <https://twitter.com/tronfoundation>`_

    `Facebook <https://www.facebook.com/TRONFoundation>`_

    `Slack <https://tronfoundation.slack.com>`_

    `CoinMarketCap <https://coinmarketcap.com/currencies/tron/>`_

    `Github <https://github.com/tronprotocol>`_

    `Telegram <https://t.me/tronnetworkEN>`_

    `E-mail <service@tron.network>`_

Other community platforms for international usership.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    `TRON SOUTH KOREA <https://t.me/tronnetworkKR>`_

    `TRON RUSSIA <https://t.me/tronnetworkRU>`_

    `TRON SPAIN <https://t.me/tronnetworkES>`_

    `TRON ARABIC <https://t.me/tronnetworkAR>`_

Contributions
-------------

Contributing to java-tron
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/images/java-tron.jpg
    :width: 400px
    :height: 400px
    :align: center

Java-tron is an open source project.

It is the work of contributors. We appreciate your help!

Here are instructions to get you started. They are not perfect, so please let us know if anything feels wrong or incomplete.

Contribution Guidelines
~~~~~~~~~~~~~~~~~~~~~~~

**Pull requests**

First of all, java-tron follows gitflow workflow. Please open pull requests to the develop branch. Once approved, we will close the pull request and merge into master branch.

We are always happy to receive pull requests, and do our best to review them as fast as possible. Not sure if that typo is worth a pull request? Do it! We would appreciate it.

If your pull request is not accepted on the first try, don't be discouraged as it can be a possible oversight. Please explain your code as detailed as possible to make it easier for us to understand.

**Create issues**

Any significant improvement should be documented as a GitHub issue before anyone starts working on it.

When filing an issue, make sure to answer these three questions:

    - What did you do?
    - What did you expect to see?
    - What did you see instead?
    - Please check existing issues and docs first!

Please take a moment to check that your bug report or improvement proposal doesn't already exist. If it does, please add a quick "+1" or "I have this problem too". This will help prioritize the most common problems and requests.

Contributing to Crowdin
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.githubusercontent.com/tronprotocol/wiki/master/images/crowdin-logo-2.png
    :width: 400px
    :height: 400px
    :align: center

Contributors
~~~~~~~~~~~~

We would like to express our deepest gratitude to the following participants who have made great contributions to the community:

**TRON Github Contributor:**

    `Roy van Kaathoven <https://github.com/Rovak>`_

    `seanrobbins <https://github.com/seanrobbins>`_

    `AhnSinYong <https://github.com/AhnSinYong>`_

    `Jean-Philippe Quéméner <https://github.com/JohnnyQQQQ>`_

    `sdargutev <https://github.com/sdargutev>`_

    `ryukato <https://github.com/ryukato>`_

    `farukonder <https://github.com/farukonder>`_

    `nguyentruongtho <https://github.com/nguyentruongtho>`_

    `Blake Jackson <https://github.com/blaketastic2>`_

    `ruchern <https://github.com/ruchern>`_

    `jun-Sogang <https://github.com/jun-Sogang>`_

    `colbywhite <https://github.com/colbywhite>`_

    `svenanders <https://github.com/svenanders>`_

    `jromero <https://github.com/jromero>`_

    `jungrammer <https://github.com/jungrammer>`_

    `Eyesonly88 <https://github.com/Eyesonly88>`_

    `wailo <https://github.com/wailo>`_

    `xiaolin <https://github.com/xiaolin>`_

    `styk-tv <https://github.com/styk-tv>`_

    `khuezy <https://github.com/khuezy>`_

    `jackforest2014 <https://github.com/jackforest2014>`_

    `Yangdaidai <https://github.com/Yangdaidai>`_

    `James Michael DuPont <https://github.com/h4ck3rm1k3>`_

    `Kamil Zieliński <https://github.com/KamilZielinski>`_

    `Wendy Sanarwanto <https://github.com/WendySanarwanto>`_

    `Johnsavadkuhi <https://github.com/Johnsavadkuhi>`_

    `Francisco Pena <https://github.com/daiky00>`_

    `Fernando Sobreira <https://github.com/fbsobreira>`_

    `lazaro <https://github.com/lazarovicedo>`_

    `Shanadas <https://github.com/shanadas>`_

    `DevObs1 <https://github.com/DevObs1>`_

    `Daivy van de Graaf <https://github.com/Daivyy>`_

    `Jacob Schuster <https://github.com/Jacob8765>`_

    `Diogenes Buarque Ianakiara <https://github.com/dbuarque>`_

**Translation Contributor:**

    `fbsobreira <https://crowdin.com/profile/fbsobreira>`_

    `PiterSpain <https://crowdin.com/profile/PiterSpain>`_

    `Dev Obs <https://crowdin.com/profile/devobs1>`_

    `johnsavadkuhi <https://crowdin.com/profile/johnsavadkuhi>`_

    `JYW <https://crowdin.com/profile/JYW>`_

    `J4ck1986 <https://crowdin.com/profile/J4ck1986>`_

    `Felix <https://crowdin.com/profile/FlxGut>`_

    `Miimiis_Pets <https://crowdin.com/profile/Miimiis_Pets>`_

    `robmarti <https://crowdin.com/profile/robmarti>`_

    `Lorenzo Addazi <https://crowdin.com/profile/loradd>`_

    `tomcritic <https://crowdin.com/profile/tomcritic>`_

    `Uğur Civak <https://crowdin.com/profile/ugurcivak>`_

    `Lernaarias <https://crowdin.com/profile/Lernaarias>`_

    `El Petito Nicolas <https://crowdin.com/profile/salocinigrub>`_

    `khanhnd69 <https://crowdin.com/profile/khanhnd69>`_




