===========
Quick Start
===========

.. contents:: Table of contents                                                           
  :depth: 1
  :local:

How to Build
------------

**Current Testnet p2p version: 32（resources/config.conf:node.p2p.verson = 32）**

**1, Getting the code**

Clone/Download the JAVA-TRON Implementation from Github

* Visit the JAVA-TRON github respository

  here: https://github.com/tronprotocol/java-tron

* Getting the source code. We use git and Github to maintain the source code. Clone the repository by:

.. code-block:: shell

    git clone https://github.com/tronprotocol/java-tron.git

* To use Git on the command line, you'll need to download, install, and configure Git on your computer. Please check `set up git <https://help.github.com/articles/set-up-git/>`_ and `fork a repo <https://help.github.com/articles/fork-a-repo/>`_.

* If you aren't familiar with using git, you can simply download `the project as a zip <https://github.com/tronprotocol/java-tron/archive/develop.zip>`_ and unpack it somewhere.

* For Mac, you can also install `Github for Mac <https://desktop.github.com/>`_ then `fork and clone our repository <https://guides.github.com/activities/forking/>`_.

**2, Installing dependencies**

* JDK 1.8 is required to be installed in the system.

* `Oracle JDK 8 <https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04>`_ (not Open JDK 8) is required to be installed in Linux Ubuntu system (e.g. Ubuntu 16.04.4 LTS).

**3, Download and Install IntelliJ IDEA**

* Install IDEA and launch the program once the process completes.

* Click through the prompts until you get to the "Welcome to IntelliJ IDEA" screen.

**4, Build in the Terminal**

.. code-block:: shell

    > cd java-tron
    > ./gradlew build

**5, Build an executable JAE**

.. code-block:: shell

    ./gradlew clean shadowJar

**6,  Build in IntelliJ IDEA (community version is enough)**

Import the JAVA-TRON Project into IDEA

* Select 'File' and navigate to the directory of the cloned (or downloaded) JAVA-TRON git project.

    ``File`` -> ``New`` -> ``Project from existing sources...``;

* Highlight build.gradle and select 'OK'.
    
    ``java-tron/build.gradle``;

* Check the box that says "Use auto-import".

* Select the radio button that says "Use gradle wrapper task configuration".

* Ensure that "Gradle JVM" is set to an instance of JDK 1.8.

* Select "OK" to import JAVA-TRON into IDEA.

* IntelliJ will open the project and start gradle syncing, which will take several minutes, depending on your network connection and your IntelliJ configuration

* After the syncing finished, select Gradle -> Tasks -> build, and then double click build option.

Running a Private Testnet
-------------------------

**Running a full node**

- In the Terminal

.. code-block:: shell

    ./gradlew run

- Use the executable JAE

.. code-block:: shell

    cd build/libs

    java -jar java-tron.jar

- In IntelliJ IDEA

    1. After the building finishes, locate ``FullNode`` in the project structure view panel, which is on the path ``java-tron/src/main/java/org.tron/program/FullNode``.

    2. Select ``FullNode``, right click on it, and select ``Run 'FullNode.main()``, then ``FullNod`` starts running.

**Running a Witness Node**

- In the Terminal

.. code-block:: shell

    ./gradlew run -Pwitness=true

Show Output

- Use the executable JAE

.. code-block:: shell

    cd build/libs

    java -jar java-tron.jar --witness true

- In IntelliJ IDEA

    1. Open the configuration panel:

    2. In the ``Program arguments``option, fill in ``--witness``:

     Then, run ``FullNode::main()`` again.

**Running multi-nodes**

To run TRON on more than one node, you need to specify several seed nodes ``IPs in config.conf in seed.node.ip.list``: For private testnet, the IPs are allocated by yourself.

Running a Public Testnet
---------------------------------------------------------
* Ensure that the version number is consistent with the version number of the test network. If it is not consistent, Please modify the node.p2p.version in the config.conf file, and delete the out-directory directory (if it exists)

**Running a Full Node**

* Use the executable JAR(Recommend the way)

```bash
cd build/libs
java -jar java-tron.jar
```
* In the Terminal

```bash
./gradlew run
```

It is almost the same as that does in the private testnet, except that the IPs in the ``config.conf`` are officially declared by TRON.

**Running a Super Representative Node**
* Use the executable JAR(Recommend the way)

```bash
cd build/libs
java -jar java-tron.jar -p yourself private key --witness -c yourself config.conf
Example:
java -jar java-tron.jar -p 650950B193DDDDB35B6E48912DD28F7AB0E7140C1BFDEFD493348F02295BD812 --witness -c /data/java-tron/config.conf

```

It is almost the same as that does in the private testnet, except that the IPs in the ``config.conf`` are officially declared by TRON.

