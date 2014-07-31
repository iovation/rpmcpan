Name:           %{iov_prefix}-Try-Tiny
Version:        0.22
Release:        1%{?dist}
Summary:        Minimal try/catch with proper preservation of $@
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Try-Tiny/
Source0:        http://cpan.metacpan.org/authors/id/D/DO/DOY/Try-Tiny-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{iov_prefix}
BuildRequires:  %{iov_prefix}-Capture-Tiny
Requires:       %{iov_prefix}

%description
This module provides bare bones try/catch/finally statements that are
designed to minimize common mistakes with eval blocks, and NOTHING else.

%prep
%setup -q -n Try-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Jul 30 2014 David E. Wheeler <david.wheeler@iovation.com> 0.22-1
- Specfile autogenerated by cpanspec 1.78.
