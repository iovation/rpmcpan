%global sname perl
%define syssbindir /usr/sbin

Name:           perl%{plv}
Version:        %(echo %{version})
Release:        4.%{etime}%{dist}
Summary:        Practical Extraction and Reporting Language

Group:          Development/Languages
License:        GPL+ or Artistic
Url:            http://www.perl.org/
Source0:        http://cpan.metacpan.org/src/perl-%{version}.tar.bz2

BuildRequires:  db4-devel
BuildRequires:  groff
BuildRequires:  tcsh
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  procps
BuildRequires:  rsyslog
BuildRequires:  man
BuildRequires:  gdbm-devel

Requires(post): %{syssbindir}/update-alternatives
Requires(postun): %{syssbindir}/update-alternatives
Provides: iov-%{sname}
Provides: %{sname}%{plv}(:WITH_ITHREADS)
Provides: %{sname}%{plv}(:WITH_PERLIO)

# List of dual-life bin files. Update %ghost entries in %files if you update
# this list.
%if 0%{?plv} >= 522
%define dualbin corelist cpan json_pp pod2usage podchecker podselect prove shasum xsubpp enc2xs piconv encguess
%else
%define dualbin config_data corelist cpan json_pp pod2usage podchecker podselect prove shasum xsubpp enc2xs piconv encguess
%endif

# Filter requires on RPM 4.8.
# http://www.redhat.com/archives/rpm-list/2005-August/msg00034.html
# http://richdawe.livejournal.com/3102.html
%define _use_internal_dependency_generator 0
%define __find_provides bin/filter-provides perl%{plv}
%define __find_requires bin/filter-requires perl%{plv} 'Mac\\|VMS\\|perl >=\\|perl(Locale::Codes::\\|perl(unicore::Name\\|FCGI\\|DBD::SQLite\\|DBIx::Simple\\|Your::Module::Here)'

%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially
good at handling text. Perl's hallmarks are practicality and efficiency. While
it is used to do a lot of different things, Perl's most common applications
are system administration utilities and web programming. A large proportion of
the CGI scripts on the web are written in Perl. You need the perl package
installed on your system so that your system can handle Perl scripts.

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
%if %{?admin_email:1}%{!?admin_email:0}
  -Dperladmin=%{admin_email} \
  -Dcf_email=%{admin_email} \
%endif
  -Duseshrplib \
  -Dusemultiplicity \
  -Duseithreads
# Remove the version from @INC paths. Must be system Perl.
/usr/bin/perl -i -pe 's{/\Q%{version}}{}g' config.sh
make %{?_smp_mflags}

%check
JOBS=$(printf '%%s' "%{?_smp_mflags}" | sed 's/.*-j\([0-9][0-9]*\).*/\1/')
LC_ALL=C TEST_JOBS=$JOBS make test_harness

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Rename dual-life binfiles.
for binfile in %{dualbin}; do
    %{__mv} %{buildroot}%{_bindir}/$binfile %{buildroot}%{_bindir}/%{plv}$binfile
    touch %{buildroot}%{_bindir}/$binfile
done

%post
# Install dual-life binfile alternatives.
for binfile in %{dualbin}; do
    %{syssbindir}/update-alternatives --install %{_bindir}/$binfile $binfile \
    %{_bindir}/%{plv}$binfile 10
done

%postun
if [ $1 -eq 0 ] ; then
    # Remove dual-life binfile alternatives.
    for binfile in %{dualbin}; do
        %{syssbindir}/update-alternatives --remove $binfile %{_bindir}/%{plv}$binfile
    done
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Artistic AUTHORS Copying README Changes
%ghost %{_bindir}/config_data
%ghost %{_bindir}/corelist
%ghost %{_bindir}/cpan
%ghost %{_bindir}/instmodsh
%ghost %{_bindir}/json_pp
%ghost %{_bindir}/pod2usage
%ghost %{_bindir}/podchecker
%ghost %{_bindir}/podselect
%ghost %{_bindir}/prove
%ghost %{_bindir}/shasum
%ghost %{_bindir}/xsubpp
%ghost %{_bindir}/enc2xs
%ghost %{_bindir}/piconv
%ghost %{_bindir}/encguess
%{_prefix}/*

%changelog
* Fri May 8 2015 David E. Wheeler <david.wheeler@iovation.com> - %{version}-4
- Ghost dual-life scripts xsubpp, enc2xs, and piconv, provided by
  ExtUtils-ParseXS and Encode.

* Fri May 1 2015 David E. Wheeler <david.wheeler@iovation.com> - %{version}-3
- Remove version from @INC paths so that any minor version uses the same
  modules.

* Tue Nov 4 2014 David E. Wheeler <david.wheeler@iovation.com> - %{version}-2
- Ghost instmodsh.

* Wed Jul 16 2014 David E. Wheeler <david.wheeler@iovation.com> - %{version}-1
- Let's build a modern Perl.
