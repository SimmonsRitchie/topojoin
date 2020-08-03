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



A lightweight utility to join CSV data to a topojson file. Produces a new topojson file with CSV properties added to
the properties of each feature.

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

By default TopoJoin will assume both files have a common field called 'id' that can be joined.

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

If you prefer, you can also import and call TopoJoin from a python script:


::

    from topojoin.topojoin import TopoJoin

    tj = TopoJoin("./example.json", "./example.csv", topo_key="GEOID", csv_key="fips")
    topojson_data = tj.join()


Or, to write to a file:

::

    from topojoin.topojoin import TopoJoin

    tj = TopoJoin("./example.json", "./example.csv", topo_key="GEOID", csv_key="fips")
    tj.join("joined.json")


Advanced usage
--------------

Command line
================

TopoJoin's actions can be modified in a number of ways by passing optional arguments. Here are its available options:

  -tk, --topokey TEXT     Key in CSV file that will be used to join with CSV
                          file  [default: id]

  -ck, --csvkey TEXT      Key in CSV file that will be used to join with
                          topojson file  [default: id]

  -cp, --csv_props TEXT   Comma separated list of fields in CSV file to merge
                          to each topojson feature (eg:
                          name,population,net_income). Defaults to including
                          all fields in CSV file.

  -o, --output_path TEXT  Output path of joined topojson file. Defaults to
                          current working directory.

  -q, --quiet             Disables stdout during program run
  --version               Show the version and exit.
  --help                  Show this message and exit.




For example:

::

    topojoin -tk GEOID -ck fips -o "mydir/my-custom-filename.json" example.json example.csv


TO DO
-----
- Prefix CSV keys if key name is already present in topojson props.
- Raise exception or prompt if CSV file has duplicate values in column specified by csv_key.

Alternatives
------------

- `py-geojoin <https://github.com/shawnbot/py-geojoin>`__
