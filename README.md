iovation Perl RPM Packager
==========================

This project manages the creation and maintenance of iovation's Perl 5 RPMs,
including all modules required for iovation Perl applications. It's designed
to be run directly from a Git clone. To build it, just run:

    ./bin/build_em

This will build Perl and all of the modules. If it has been built previously
from the same Git branch, then only SPEC files modified since the last run
will be used to create new RPMs. This is to keep the number of things that get
built on each run to a minimum.

By default, the version of Perl will be read from `SPECS/perl.spec` and used
to create the install path and RPM name prefix. The resulting RPMs will have names
like `perl520-perl` and `perl520-Try-Tiny` and will all be installed by the
resulting RPMs in `/usr/local/perl520`. You can modify the path and prefix
with the `--path` and `--prefix` options, e.g.:

    ./bin/build_em --path /usr/local/iovperl520 --prefix iovperl520-

But you probably won't want to. You can also specify that the RPM dist variable
be set via the `--dist` option.

    ./bin/build_em --dist iov

And if you want to rebuild *all* of the RPMs, not just those that have had
their spec files changed, pass `--all`.

    ./bin/build_em --all

Author
------
* [David E. Wheeler](mailto:david.wheeler@iovation.com)
