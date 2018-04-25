====================
Super Representative
====================

.. contents:: Table of contents
    :depth: 1
    :local:

What is a Super Representative
------------------------------

Super Representatives can produce blocks and verify transactions. Meanwhile, Super Representatives can make an actual profit from creating blocks.

Users can get SR information form TRON blockchain exploerer, the detailed information shows as below:

- The account address of delegate.
- The total votes that delegate gets.
- The url of personal website.
- The total produced blocks of delegate.
- The total missed blocks of delegate.

How to Vote
-----------

The following steps serve as an introduction on how to vote for a Super Representative through our TRON blockchain explorer.

**Steps**

1, A registered account is required in TRON blockchain explorer.

* In order to use TRON blockchain explorer, you will need to register an account, please visit our website:

    https://tronscan.org/#/login

* Direct visit to Tron blockchain explorer and the Web wallet can be made through

    https://tronscan.org

2, Tick off the follow three items, then click the button “Create Account”.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/create_account.png
    :scale: 50%
    :align: center

3, A certain sum of TRX is required in your new account.

* 10000 TRX for testing will be sent to your testing account. Please click the button "Request TRX for testing".

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/request_for_testing.png
    :width: 842px
    :height: 486px
    :align: center

4, Vote for delegate  .

* Click the button "Votes" in account options.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/votes.png
    :width: 842px
    :height: 450px
    :align: center

5, You can vote for all the delegates. Please choose the number of TRX and submit your votes.

**Rules:**

- The maximum number of votes is no more than the user’s amount of TRX holding at a given time.
- Each account can vote for several delegates for several times.
- The final votes will be tallied at 24 o'clock and the list of delegates will be updated.
- TRX for testing will not be consumed in the voting process.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/submit_vote.png
    :width: 841px
    :height: 572px
    :align: center

Running a Super Representative
------------------------------

The following steps serve as an introduction on how to become a Super Representative through our TRON blockchain explorer.

**Steps**

1, A registered account is required in TRON blockchain explorer.  

* In order to use TRON blockchain explorer, you will need to register an account, please visit our website:  

    https://tronscan.org/#/login

* Direct visit to Tron blockchain explorer and the Web wallet can be made through

    https://tronscan.org

2, Tick off the follow three items, then click the button “Create Account”.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/create_account.png
    :scale: 50%
    :align: center

3, A certain sum of TRX is required in your new account.  

* 10000 TRX for testing will be sent to your testing account. Please click the button "Request TRX for testing".

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/request_for_testing.png
    :width: 842px
    :height: 486px
    :align: center

4, You can get started to apply to be a delegate.  

* Click the button “ Apply_for_delegate” first.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/apply_for_super_representative.png
    :width: 842px
    :height: 486px
    :align: center

5, Provide your personal website address. The type of address includes but is not limited to: website, blog, social media account, etc.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/personal_address.png
    :height: 466px
    :width: 646px
    :align: center

6, Vote for delegate  .

* Click the button "Votes" in account options.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/votes.png
    :width: 842px
    :height: 450px
    :align: center

7, You can vote for all the delegates.

* The maximum number of votes is no more than the user’s amount of TRX holding at a given time. Please choose the number of TRX and submit your votes.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/submit_vote.png
    :width: 841px
    :height: 572px
    :align: center

8, After approval voting, the top 27 SRs by total approval are selected. The state of active SRs is updated once every maintenance interval (1 day).

9, Running you Super Representative Node
## Prepare dependencies

* JDK 1.8 (JDK 1.9+ are not supported yet)
* On Linux Ubuntu system (e.g. Ubuntu 16.04.4 LTS), ensure that the machine has [__Oracle JDK 8__](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04), instead of having __Open JDK 8__ in the system. If you are building the source code by using __Open JDK 8__, you will get [__Build Failed__](https://github.com/tronprotocol/java-tron/issues/337) result.

## Getting the code

* Use Git from the Terminal, see the [Setting up Git](https://help.github.com/articles/set-up-git/) and [Fork a Repo](https://help.github.com/articles/fork-a-repo/) articles.
** develop branch: the newnest code 
** master branch: more stable than develop.
In the shell command, type:
```bash
git clone https://github.com/tronprotocol/java-tron.git
```
* Build in the Terminal

```bash
cd java-tron
./gradlew build
```
## Running a Super Representative Node

* Ensure that the version number is consistent with the version number of the test network. If it is not consistent, Please modify the node.p2p.version in the config.conf file, and delete the out-directory directory (if it exists)

* Use the executable JAR(Recommend the way)

```bash
cd build/libs
java -jar java-tron.jar -p yourself private key --witness -c yourself config.conf(Example：/data/java-tron/config.conf)
Example:
java -jar java-tron.jar -p 650950B193DDDDB35B6E48912DD28F7AB0E7140C1BFDEFD493348F02295BD812 --witness -c /data/java-tron/config.conf

```
