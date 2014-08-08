#%define contentdir /var/www
%global sname         mod_perl
%define sysprefix     /usr
%define syslibdir     %{sysprefix}/%{_lib}
%define sysincludedir %{sysprefix}/include
%define sysbindir     %{sysprefix}/bin
%define syssbindir    %{sysprefix}/sbin

Name:           %{iov_prefix}-%{sname}
Version:        2.0.8
Release:        1%{?dist}
Summary:        An embedded Perl interpreter for the Apache HTTP Server

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://perl.apache.org/
# Source0:        http://perl.apache.org/dist/%{sname}-%{version}.tar.gz
Source0:        http://apache.osuosl.org/perl/%{sname}-%{version}.tar.gz
Source1:        perl.conf
# Source2:        filter-requires.sh
# Source3:        filter-provides.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{iov_prefix}
BuildRequires:  httpd-devel >= 2.2.0
BuildRequires:  httpd
BuildRequires:  gdbm-devel
BuildRequires:  apr-devel >= 1.2.0
BuildRequires:  apr-util-devel
Requires:       %{iov_prefix}
Requires:       httpd-mmn = %(cat %{sysincludedir}/httpd/.mmn || echo missing)
Conflicts:      mod_perl

%define __find_requires bin/filter-requires %{iov_prefix} 'perl(\\(Apache2\\?::[^)]\\+\\|BSD::Resource\\|Data::Flow\\))'

%description
mod_perl incorporates a Perl interpreter into the Apache web server,
so that the Apache web server can directly execute Perl code.
Mod_perl links the Perl runtime library into the Apache web server and
provides an object-oriented Perl interface for Apache's C language
API.  The end result is a quicker CGI script turnaround process, since
no external Perl interpreter has to be started.

Install mod_perl if you're installing the Apache web server and you'd
like for it to directly incorporate a Perl interpreter.


%prep
%setup -q -n %{sname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS -fpic" %{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor \
	MP_APXS=%{syssbindir}/apxs \
	MP_APR_CONFIG=%{sysbindir}/apr-1-config
make -C src/modules/perl %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS -fpic"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{syslibdir}/httpd/modules
make install \
    PERL_INSTALL_ROOT=$RPM_BUILD_ROOT \
    MODPERL_AP_LIBEXECDIR=$RPM_BUILD_ROOT%{syslibdir}/httpd/modules \
    MODPERL_AP_INCLUDEDIR=$RPM_BUILD_ROOT%{sysincludedir}/httpd

# Remove the temporary files.
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

# Fix permissions to avoid strip failures on non-root builds.
chmod -R u+w $RPM_BUILD_ROOT/*

# Install the config file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_bindir}/*
%{syslibdir}/httpd/modules/%{sname}.so
%{sysincludedir}/httpd/*
%{perl_vendorlib}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Apache2/
%{perl_vendorarch}/Bundle/
%{perl_vendorarch}/APR/
%{perl_vendorarch}/ModPerl/
%{perl_vendorarch}/*.pm
%{vendormandir}/man3/*

%changelog
* Thu Jul 31 2014 David E. Wheeler <david.wheeler@iovation.com> - 2.0.8-1
- First attempt at building 2.0.8.
