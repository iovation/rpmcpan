iovation Perl RPM Packager
==========================

This project manages the creation and maintenance of iovation's Perl 5 RPMs,
including all modules required for iovation Perl applications. It's designed
to be run directly from a Git clone. For example, to build Perl 5.20, run:

    ./bin/build_em --path /usr/local/perl520 --prefix perl520-

This will build Perl and all of the modules. If it has been built previously
from the same Git branch, then only SPEC files modified since the last run
will be used to create new RPMs. This is to keep the number of things that get
built on each run to a minimum.

To Do
-----
* Read the Perl version from `SPECS/perl.spec` to set the prefix and path.
* Build RPMs for spec files with no corresponding RPMS in the `yum` directory,
  even if they haven't been changed since the last run.

Author
------
* [David E. Wheeler](mailto:david.wheeler@iovation.com)
