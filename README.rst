MacGyver's Wireless Presenter
=============================

This script turns your smartphone into a wireless presenter.

Requirement
-----------

*  `Jython <http://www.jython.org/downloads.html>`_ 

*  Your laptop (or wherever you put your slides on) and smartphone
   must be on the same (high-speed, supposedly) subnet.

Usage
-----

Run ``remote.py`` under the same directory where ``index.html`` is placed.

::

   $ jython remote.py

or specify another port number::

   $ jython remote.py 1234

Type the URL that ``remote.py`` printed out in the browser 
of your smartphone (for instance, ``192.168.1.100:8000``)
and a control panel will show up.
Then focus on the window of your slides and you are good to go.

