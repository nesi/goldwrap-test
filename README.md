Tests for goldwrap
==================

The tests are based on lettuce (Python tool for Behavior Driven Development (BDD))

Prerequisites
-------------
* Python v2.6, v2.7

For installing the dependencies: pip

Install package dependencies
----------------------------
pip install -r requirements.pip

Configure tests
---------------
Edit features/terrain.py to configure
* GOLDWRAP_PROTOCOL: protocol (http, https)
* GOLDWRAP_HOST: Name of the machine where goldwrap runs
* GOLDWRAP_PORT: Port at which goldwrap listens
* GOLDWRAP_BASE_PATH: Path where goldwrap is available
* TIMEOUT: Max time to wait for the REST calls

Run tests
---------
Run 'lettuce' in the top-level folder to run all features.
To run an individual feature, e.g. the login feature: 'lettuce features/user.feature'
To run the first scenario of a feature, e.g. the login feature: 'lettuce features/user.feature 1'

Note: The command 'lettuce' is available after the dependencies are installed.

Understand what is tested and how to add test cases
---------------------------------------------------
The tests are defined in features/*.feature in the Gherkin language.
As such they should be pretty straight-forward to read, and it should be relatively easy to add
new test cases for the given scenarios by adding rows to the 'Examples' table of a scenario.