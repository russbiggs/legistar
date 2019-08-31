py-legistar
====================================

Python 3.7+ wrapper for the legistar API

====================================


**Example Usage**::

    from legistar import Legistar
    leg = Legistar('cabq') # legistar client for City of Albuquerque
    leg.action(42)
    # Action(id=42, guid=None, last_modified_utc=datetime.datetime(2014, 5, 24, 4, 9, 58, 777000), 
    # row_version='AAAAAAAAELQ=', name='Approve the Journal', active_flag=1, used_flag=0)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   client
   models



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`