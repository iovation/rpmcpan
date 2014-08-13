%define iov_email  jira-ops@iovaiton.com
%global sname perl

Name:           perl%{plv}
Version:        5.20.0
Release:        1%{?dist}
Summary:        Practical Extraction and Reporting Language

Group:          Development/Languages
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and Copyright Only and MIT and Public Domain and UCD
Url:            http://www.perl.org/
Source0:        http://cpan.metacpan.org/src/perl-%{version}.tar.bz2
# BuildRequires:  db4-devel, groff, tcsh, zlib-devel, bzip2-devel
# BuildRequires:  systemtap-sdt-devel
# BuildRequires:  procps, rsyslog

# Filter requires on RPM 4.8.
# http://www.redhat.com/archives/rpm-list/2005-August/msg00034.html
# http://richdawe.livejournal.com/3102.html
%define __find_requires bin/filter-requires perl%{plv} 'Mac\\|VMS\\|perl >=\\|perl(Locale::Codes::\\|perl(unicore::Name\\|FCGI)'

%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially
good at handling text. Perl's hallmarks are practicality and efficiency. While
it is used to do a lot of different things, Perl's most common applications
are system administration utilities and web programming. A large proportion of
the CGI scripts on the web are written in Perl. You need the perl package
installed on your system so that your system can handle Perl scripts.

%global perl_compat %{sname}(:MODULE_COMPAT_%{version})
Provides: iov-%{sname}
Provides: %{sname}%{plv}(:MODULE_COMPAT_%{version})
Provides: %{sname}%{plv}(:WITH_ITHREADS)
Provides: %{sname}%{plv}(:WITH_PERLIO)

%prep
%setup -q -n %{sname}-%{version}

%build
sh Configure -des \
  -Dprefix=%{_prefix} \
  -Dsiteprefix=%{_prefix} \
  -Dsiteman1dir=%{sitemandir}/man1 \
  -Dsiteman3dir=%{sitemandir}/man3 \
  -Dvendorprefix=%{_prefix} \
  -Dvendorman1dir=%{vendormandir}/man1 \
  -Dvendorman3dir=%{vendormandir}/man3 \
  -Duseshrplib \
  -Dusemultiplicity \
  -Duseithreads \
  -Dperladmin=%{iov_email} \
  -Dcf_email=%{iov_email}
make %{?_smp_mflags}

%check
JOBS=$(printf '%%s' "%{?_smp_mflags}" | sed 's/.*-j\([0-9][0-9]*\).*/\1/')
LC_ALL=C TEST_JOBS=$JOBS make test_harness

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Artistic AUTHORS Copying README Changes
%{_prefix}/*

%changelog
* Wed Jul 16 2014 David E. Wheeler <david.wheeler@iovation.com> - 5.20.0-1
- First attempt at building 5.20.0.
