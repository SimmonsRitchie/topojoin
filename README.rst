========
TopoJoin
========


.. image:: https://img.shields.io/pypi/v/topojoin.svg
        :target: https://pypi.python.org/pypi/topojoin

.. image:: https://img.shields.io/travis/SimmonsRitchie/topojoin.svg
        :target: https://travis-ci.com/SimmonsRitchie/topojoin

.. image:: https://readthedocs.org/projects/topojoin/badge/?version=latest
        :target: https://topojoin.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



A lightweight utility to left join topojson data with CSV data.

* Free software: MIT
* Documentation: https://topojoin.readthedocs.io.

Install
----------

::

    pip install topojoin


Basic usage
-----------

Command line
============

In the command line, enter the topojoin command followed by the path to your topojson file and your CSV file.

By default topojoin will assume both files have a common field called 'id' that can be joined.

::

    topojoin example.json example.csv

    >> Joining example.csv to example.json...
    >> CSV key 'id' will be joined with topojson key 'id'
    >> Joined data saved to: joined.json

To define the join keys, use the '-tk' option for the key in your topojson file and the '-ck' option for the key in
your CSV file:

::

    topojoin -tk GEOID -ck fips example.json example.csv

    >> Joining example.csv to example.json...
    >> CSV key 'fips' will be joined with topojson key 'GEOID'
    >> Joined data saved to: joined.json


Programmatic
============

If you prefer, you can also import and call topojson from a python script:


::

    from topojoin.topojoin import TopoJoin

    topo_obj = TopoJoin("./example.json", "./example.csv", topo_key="GEOID", csv_key="fips")
    topojson_data = topo_obj.join()


Or, to write to a file:

::

    from topojoin.topojoin import TopoJoin

    topo_obj = TopoJoin("./example.json", "./example.csv", topo_key="GEOID", csv_key="fips")
    topo_obj.join("joined.json")


Advanced usage
--------------

Command line
================

topojoin's actions can be modified in a number of ways by passing optional arguments. Here are its available options:

  -tk, --topokey TEXT     Key in CSV file that will be used to join with CSV
                          file  [default: id]

  -ck, --csvkey TEXT      Key in CSV file that will be used to join with
                          topojson file  [default: id]

  -o, --output_path PATH  Key in CSV file that will be used to join with CSV
                          file  [default: /Volumes/Dan_T5/development/PythonPr
                          ojects/utilities/2020/topojoin/topojoin/joined.json]

  -q, --quiet             Disables stdout during program run
  --version               Show the version and exit.
  --help                  Show this message and exit.


For example:

::

    topojoin -tk GEOID -ck fips -o "mydir/my-custom-filename.json" example.json example.csv
