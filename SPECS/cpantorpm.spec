Name:           perl%{plv}-cpantorpm
Version:        1.00
Release:        1%{?dist}
Summary:        An RPM packager for perl modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/cpantorpm/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SB/SBECK/cpantorpm-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl%{plv}
Requires:       perl%{plv}

%description
This script automates the entire process of obtaining a perl module and
turning it into an RPM package. This includes the steps of obtaining the
module distribution, creating an RPM from it, and then making the package
available in various ways.

%prep
%setup -q -n cpantorpm-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install --destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{vendormandir}/man1/*

%changelog
* Wed Aug 6 2014 David E. Wheeler <david.wheeler@iovation.com> 1.00-1
- Initial packaging.
