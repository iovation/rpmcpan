#%define contentdir /var/www
%global sname         mod_perl
%define sysprefix     /usr
%define syslibdir     %{sysprefix}/%{_lib}
%define sysincludedir %{sysprefix}/include
%define sysbindir     %{sysprefix}/bin
%define apxs          %(which apxs)

%if %{undefined plv}
%define plv %{nil}
%endif

Name:           perl%{plv}-%{sname}
Version:        2.0.9
Release:        0.%{etime}%{dist}
Summary:        An embedded Perl interpreter for the Apache HTTP Server

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://perl.apache.org/
# Source0:        http://perl.apache.org/dist/%{sname}-%{version}.tar.gz
# Source0:        http://apache.osuosl.org/perl/%{sname}-%{version}.tar.gz
Source0:        http://people.apache.org/~stevehay/mod_perl-2.0.9-rc1.tar.gz
Source1:        perl.conf
%if "%{apxs}" == "/usr/sbin/apxs"
Patch1:         mod_perl-centos.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  perl%{plv}
BuildRequires:  perl%{plv}(ExtUtils::Embed)
BuildRequires:  perl-devel
BuildRequires:  httpd-devel >= 2.2.0
BuildRequires:  httpd
BuildRequires:  gdbm-devel
BuildRequires:  apr-devel >= 1.2.0
BuildRequires:  apr-util-devel
BuildRequires:  perl%{plv}(Tie::IxHash)
Requires:       perl%{plv}
Requires:       httpd-mmn = %(cat %{sysincludedir}/httpd/.mmn || echo missing)
Requires:       perl%{plv}(Linux::Pid)
Requires:       perl%{plv}(IPC::Run3)
%if "%{plv}" == ""
Requires:       perl%{plv}(:MODULE_COMPAT_%{plfullv})
%endif
Conflicts:      mod_perl
Conflicts:      mod_perl-devel

%define _use_internal_dependency_generator 0
%define __find_provides bin/filter-provides perl%{plv}
%define __find_requires bin/filter-requires perl%{plv} 'perl(\\(Apache2\\?::[^)]\\+\\|BSD::Resource\\|Data::Flow\\))'

%description
mod_perl incorporates a Perl interpreter into the Apache web server, so that
the Apache web server can directly execute Perl code. Mod_perl links the Perl
runtime library into the Apache web server and provides an object-oriented
Perl interface for the Apache C language API. The end result is a quicker CGI
script turnaround process, since no external Perl interpreter has to be
started.

Install mod_perl if you are installing the Apache web server and you would
like for it to directly incorporate a Perl interpreter.


%prep
%setup -q -n %{sname}-2.0.9-rc1
%if "%{apxs}" == "/usr/sbin/apxs"
%patch1 -p1
%endif

%build

for i in Changes SVN-MOVE; do
    iconv --from=ISO-8859-1 --to=UTF-8 $i > $i.utf8
    mv $i.utf8 $i
done

cd docs
for i in devel/debug/c.pod devel/core/explained.pod user/Changes.pod; do
    iconv --from=ISO-8859-1 --to=UTF-8 $i > $i.utf8
    mv $i.utf8 $i
done
cd ..

CFLAGS="$RPM_OPT_FLAGS -fpic" %{__perl} Makefile.PL </dev/null \
       INSTALLDIRS=vendor \
       MP_APXS=%{apxs} \
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

# Remove temporary and empty bootstrap files.
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

# Grab and tweak the .packlist file.
find $RPM_BUILD_ROOT -type f -name .packlist -exec mv {} . \;
perl -i -pe 's/[.]([13](?:pm)?)$/.$1*/g' .packlist
perl -i -pe '$_ = "" if /[.]bs/ && do { my $f = $_; chomp $f; !-e $f }' .packlist
perl -i -pe "s{^\Q$RPM_BUILD_ROOT}{}g" .packlist

# Fix permissions to avoid strip failures on non-root builds.
chmod -R u+w $RPM_BUILD_ROOT/*

# Install the config file
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/

# perl build script generates *.orig files, they get installed and later they
# break provides. We remove them here.
find "$RPM_BUILD_ROOT" -type f -name *.orig -exec rm -f {} \;

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files -f .packlist
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{syslibdir}/httpd/modules/%{sname}.so
%{sysincludedir}/httpd/*

%changelog
* Fri May 1 2015 David E. Wheeler <david.wheeler@iovation.com> - %{version}-2
- Updated to build from Subversion-derived tarball provided by the Fedora project.
- Require Linux::Pid and IPC::Run3
- Require ExtUtils::Embed and Tie::IxHash to build.
- Determine files to install based on the generated .packlist file.

* Thu Jul 31 2014 David E. Wheeler <david.wheeler@iovation.com> - %{version}-1
- Let's build a modern mod_perl.
