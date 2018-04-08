===========
Running a Delegate.
===========

.. contents:: Table of contents
  :depth: 1
  :local:

The following steps serve as an introduction on how to become an actively delegate through our TRON blockchain explorer.

**Steps**

1. A registered account is required in TRON blockchain explorer.

* In order to use TRON blockchain explorer, you will need to register an account, please visit our website:

  http://git.razko.nl/wallet-web/#/login

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/Register.png
    :scale: 50%
    :align: center

2. A certain sum of TRX is required to be transferred to your new account.

* TRX for testing will be sent to your testing acoount once you successfully apply through account management.

3. Users can contact the TRON staff to get TRX for testing.

4. You can get started to apply to be a delegate.

* Click the button “ Apply_for_delegate” first.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/apply%20for%20delegate.png
    :width: 842
    :height: 400
    :align: center

* Provide your personal website address. The type of address is including but not limited to: website, blog, social media account, etc.

.. image:: https://raw.githubusercontent.com/ybhgenius/wiki/master/docs/img/intro/personal%20address.png
    :width: 746
    :height: 540
    :align: center

5. After approval voting, the top 21 delegates by total approval are selected. The state of active delegates is updated once every maintenance interval (1 day).

* Build in the Terminal

.. code-block:: shell

    ./gradlew run -Pwitness=true

* Use the executable JAE

.. code-block:: shell

    cd build/libs

    java -jar java-tron.jar --witness true

* In IntelliJ IDEA

Open the configuration panel:

In the Program arguments option, fill in --witness:

Then, run FullNode::main() again.





