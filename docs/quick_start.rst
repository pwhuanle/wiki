===========
Quick Start
===========

.. contents:: Table of contents                                                           
  :depth: 1
  :local:


**Current Testnet p2p version: 32（resources/config.conf:node.p2p.verson = 32）**

**1, Clone/Download the JAVA-TRON Implementation from Github**

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

**4, Import the JAVA-TRON Project into IDEA**

* Select 'File' and navigate to the directory of the cloned (or downloaded) JAVA-TRON git project.

    ``File`` -> ``New`` -> ``Project from existing sources...``;

* Highlight build.gradle and select 'OK'.
    
    ``java-tron/build.gradle``;

* Check the box that says "Use auto-import".

* Select the radio button that says "Use gradle wrapper task configuration".

* Ensure that "Gradle JVM" is set to an instance of JDK 1.8.

* Select "OK" to import JAVA-TRON into IDEA.

* IDEA will now begin to build the project (wait until finished doing stuff).

**5, Contribution**

Contributions are greatly welcomed. Please check `CONTRIBUTING.md <https://github.com/tronprotocol/java-tron/blob/develop/CONTRIBUTING.md>`__ for details on submitting patches and the contribution workflow.

**6, Servers**

+----------------+-----------------+---------------------+
| IP             | Location        | Description         |
+================+=================+=====================+
| 47.254.16.55   | Silicon Valley  | Witness Node        |
+----------------+-----------------+---------------------+
| 47.254.18.49   | Silicon Valley  | Witness Node        |
+----------------+-----------------+---------------------+
| 18.188.111.53  | Ohio            | Witness Node        |
+----------------+-----------------+---------------------+
| 54.219.41.56   | California      | Witness Node        |
+----------------+-----------------+---------------------+
| 35.169.113.187 | Virginia        | Witness Node        |
+----------------+-----------------+---------------------+
| 34.214.241.188 | Oregon          | Witness Node        |
+----------------+-----------------+---------------------+
| 47.254.146.147 | Frankfurt       | Witness Node        |
+----------------+-----------------+---------------------+
| 47.254.144.25  | Frankfurt       | Witness Node        |
+----------------+-----------------+---------------------+
| 47.91.246.252  | Hongkong        | Witness Node        |
+----------------+-----------------+---------------------+
| 47.91.216.69   | Hongkong        | Witness Node        |
+----------------+-----------------+---------------------+
| 39.106.220.120 | Beijing         | Witness Node        |
+----------------+-----------------+---------------------+
| 47.95.14.107   | Beijing         | Blockchain Explorer |
+----------------+-----------------+---------------------+

**7, Links**

* TRON Website: https://tron.network/
* GitHub: https://github.com/tronprotocol/java-tron/
* Community Telegram Group: https://t.me/tronnetworkEN/
* Slack Workspace: https://tronfoundation.slack.com/