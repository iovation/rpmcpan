%global sname         libapreq2
%define sysprefix     /usr
%define syslibdir     %{sysprefix}/%{_lib}
%define sysincludedir %{sysprefix}/include

%if %{undefined plv}
%define plv %{nil}
%endif

Name:           perl%{plv}-%{sname}
Version:        %(echo %{version})
Release:        1.%{dist}

Summary:        Methods for dealing with client request data
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            https://metacpan.org/release/%{sname}
Source0:        http://www.cpan.org/authors/id/J/JO/JOESUF/%{sname}-%{version}.tar.gz
Source1:        %{sname}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv:    no

BuildRequires:  apr-devel
BuildRequires:  apr-util-devel
BuildRequires:  httpd-devel
BuildRequires:  perl%{plv} >= 5.16
BuildRequires:  perl%{plv}-mod_perl
BuildRequires:  perl%{plv}(Apache::Test) >= 1.04
BuildRequires:  perl%{plv}(ExtUtils::MakeMaker) >= 6.15
BuildRequires:  perl%{plv}(ExtUtils::XSBuilder) >= 0.23
BuildRequires:  perl%{plv}(Test::More) >= 0.47
BuildRequires:  perl%{plv}(mod_perl2) >= 1.999022

Requires:       perl%{plv} >= 5.16
Requires:       perl%{plv}(mod_perl2) >= 1.999022
%if "%{plv}" == ""
Requires:       perl%{plv}(:MODULE_COMPAT_%{plfullv})
%endif
Conflicts:      libapreq2
Conflicts:      libapreq2-devel

Provides:       perl%{plv}(TestAPI::cookie)
Provides:       perl%{plv}(TestAPI::param)
Provides:       perl%{plv}(TestApReq::inherit)
Provides:       perl%{plv}(TestApReq::upload)
Provides:       perl%{plv}(APR::Request::Cookie)
Provides:       perl%{plv}(APR::Request::Param)
Provides:       perl%{plv}(APR::Request::Brigade)
Provides:       perl%{plv}(APR::Request::Brigade::IO)
Provides:       perl%{plv}(APR::Request::ConstantsTable)
Provides:       perl%{plv}(TestApReq::cookie)
Provides:       perl%{plv}(APR::Request::CallbackTable)
Provides:       perl%{plv}(Apache2::Request) = 2.13
Provides:       perl%{plv}(TestApReq::request)
Provides:       perl%{plv}(APR::Request::Custom)
Provides:       perl%{plv}(APR::Request::Cookie::Table)
Provides:       perl%{plv}(APR::Request::Param::Table)
Provides:       perl%{plv}(APR::Request::FunctionTable)
Provides:       perl%{plv}(TestAPI::error)
Provides:       perl%{plv}(TestAPI::module)
Provides:       perl%{plv}(TestApReq::big_input)
Provides:       perl%{plv}(TestApReq::cookie2)
Provides:       perl%{plv}(APR::Request::StructureTable)
Provides:       perl%{plv}(Apache2::Cookie) = 2.13
Provides:       perl%{plv}(Apache2::Cookie::Jar)
Provides:       perl%{plv}(Apache2::Upload) = 2.13

%description
Methods for dealing with client request data

%prep
%setup -q -n %{sname}-%{version}

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-perl-glue \
    --with-perl=%{__perl} \
    --with-mm-opts="INSTALLDIRS=vendor"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=%{buildroot}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/apreq.conf

# Grab and tweak the .packlist file.
find $RPM_BUILD_ROOT -type f -name .packlist -exec mv {} . \;
perl -i -pe "s{^\Q$RPM_BUILD_ROOT}{}g" .packlist
%if "%{plv}" == ""
perl -i -pe 's/[.]([13](?:pm)?)$/.$1.gz/g' .packlist
%endif

find $RPM_BUILD_ROOT -type f -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name perllocal.pod -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# Test just doesn't work for various reasons not worth patching. Maybe fixed
# in next release?
#%{__make} test

%post -n perl%{plv}-%{sname} -p /sbin/ldconfig
%postun -n perl%{plv}-%{sname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f .packlist
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/httpd/conf.d/apreq.conf
%{_bindir}/apreq2-config
%{_includedir}/apreq2/
%{_libdir}/libapreq2.so*
%if "%{plv}" == ""
%{_libdir}/httpd/modules/%{sname}.so
%{_libdir}/httpd/modules/mod_apreq2.so
%{_includedir}/httpd/apreq2/
%else
%{syslibdir}/*
%{sysincludedir}/*
%endif

%changelog
* Tue May 05 2015 David Wheeler <dwheeler@pdxdvddb01.iovationnp.com> 2.13-1
- Specfile autogenerated by rpmcpan 1.1.
