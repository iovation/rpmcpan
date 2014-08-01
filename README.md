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

Adding CPAN Distributions
-------------------------

To add a CPAN distribution, start by running `cpanspec`, like so:

    cpanspec --cpan http://cpan.metacpan.org --follow --noprefix \
        --packager 'Joe Blow <joe.blow@iovation.com>' -v Module::Name

Only use your own name and email address, of course. Copy the resulting
`*.spec` files into the `SPECS` directory and the downloaded tarballs into the
`SOURCES` directory (but don't add the tarballs to Git!). Then edit the spec
file, making the following changes:

* Prepend `%{iov_prefix}-` to the `Name` tag.
* Replace the `Requires` and `BuildRequires` tags that require Perl to instead
  require `%{iov_prefix}`.
* Delete any `BuildRequires` tags that require modules included in the Perl
  core.
* Change any `BuildRequires` tags that reference modules built by this project
  to require RPMs rather than modules. For example, replace `perl(Try::Tiny)`
  with `%{iov_prefix}-Try-Tiny`. This allows build dependency ordering to work
  correctly.
* In the `%prep` section, change the `%setup` macro to reference the full
  tarball name. That is, relace `%setup` with
  `%setup -f Dist-Name-%{version}`.
* Delete the `%doc` macro from the `%files` section. It tends to include a
  bunch of crap no one ever needs to see.
* Adjust the `%files` section to grab all the built files. For example, you
  might need to add `%{_bindir}/*` and `%{_mandir}/man1/*` if the distribution
  installs command-line applications.

With those changes in place, `git add SPECS` and run `./bin/build_em` until
the RPM or RPMs build. The run `rpm -qpl` on the resulting RPM or RPMs in the
`repo` directory to make sure no unexpected files were installed or installed
outside of `/usr/local/perl$version`. Commit the spec file(s) an push it!

Author
------
* [David E. Wheeler](mailto:david.wheeler@iovation.com)
