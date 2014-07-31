Name:           %{iov_prefix}-CGI
Version:        4.03
Release:        1%{?dist}
Summary:        Handle Common Gateway Interface requests and responses
License:        Perl
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI/
Source0:        http://cpan.metacpan.org/authors/id/L/LE/LEEJO/CGI.pm-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  %{iov_prefix}
Requires:       %{iov_prefix}

%description
CGI.pm is a stable, complete and mature solution for processing and preparing
HTTP requests and responses in Perl. Major features including processing form
submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers. Some
HTML generation utilities are included as well.

%prep
%setup -q -n CGI.pm-%{version}

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
* Thu Jul 31 2014 David E. Wheeler <david.wheeler@iovation.com> 4.03-1
- First attempt at building 4.03.
