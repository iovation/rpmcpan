%if %{undefined plv}
%global plv %{nil}
%endif

%if "%{plv}" == ""
%define rpmname sqitch
%else
%define rpmname perl%{plv}-sqitch
%endif

Name:           %{rpmname}
Version:        %(echo %{version})
Release:        1.%{etime}%{dist}
Summary:        Sane database change management
License:        MIT
Group:          Development/Libraries
URL:            http://sqitch.org/
Source0:        http://www.cpan.org/modules/by-module/App/App-Sqitch-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       sqitch
BuildRequires:  perl >= 1:v5.10.0
BuildRequires:  perl%{plv}(Capture::Tiny) >= 0.12
BuildRequires:  perl%{plv}(Carp)
BuildRequires:  perl%{plv}(Class::XSAccessor) >= 1.18
BuildRequires:  perl%{plv}(Clone)
BuildRequires:  perl%{plv}(Config)
BuildRequires:  perl%{plv}(Config::GitLike) >= 1.11
BuildRequires:  perl%{plv}(constant)
BuildRequires:  perl%{plv}(DateTime)
BuildRequires:  perl%{plv}(DateTime::TimeZone)
BuildRequires:  perl%{plv}(DBI)
BuildRequires:  perl%{plv}(Devel::StackTrace) >= 1.30
BuildRequires:  perl%{plv}(Digest::SHA)
BuildRequires:  perl%{plv}(Encode)
BuildRequires:  perl%{plv}(Encode::Locale)
BuildRequires:  perl%{plv}(File::Basename)
BuildRequires:  perl%{plv}(File::Copy)
BuildRequires:  perl%{plv}(File::HomeDir)
BuildRequires:  perl%{plv}(File::Path)
BuildRequires:  perl%{plv}(File::Spec)
BuildRequires:  perl%{plv}(File::Temp)
BuildRequires:  perl%{plv}(Getopt::Long)
BuildRequires:  perl%{plv}(Hash::Merge)
BuildRequires:  perl%{plv}(IO::Pager)
BuildRequires:  perl%{plv}(IPC::Run3)
BuildRequires:  perl%{plv}(IPC::System::Simple) >= 1.17
BuildRequires:  perl%{plv}(List::Util)
BuildRequires:  perl%{plv}(List::MoreUtils)
BuildRequires:  perl%{plv}(Locale::TextDomain) >= 1.20
BuildRequires:  perl%{plv}(Module::Build) >= 0.35
BuildRequires:  perl%{plv}(Moo) >= 1.002000
BuildRequires:  perl%{plv}(Moo::Role)
BuildRequires:  perl%{plv}(Moo::sification)
BuildRequires:  perl%{plv}(namespace::autoclean) >= 0.16
BuildRequires:  perl%{plv}(parent)
BuildRequires:  perl%{plv}(overload)
BuildRequires:  perl%{plv}(Path::Class) >= 0.33
BuildRequires:  perl%{plv}(PerlIO::utf8_strict)
BuildRequires:  perl%{plv}(Pod::Escapes)
BuildRequires:  perl%{plv}(Pod::Find)
BuildRequires:  perl%{plv}(Pod::Usage)
BuildRequires:  perl%{plv}(POSIX)
BuildRequires:  perl%{plv}(Scalar::Util)
BuildRequires:  perl%{plv}(StackTrace::Auto)
BuildRequires:  perl%{plv}(strict)
BuildRequires:  perl%{plv}(String::Formatter)
BuildRequires:  perl%{plv}(String::ShellQuote)
BuildRequires:  perl%{plv}(Sub::Exporter)
BuildRequires:  perl%{plv}(Sub::Exporter::Util)
BuildRequires:  perl%{plv}(Sys::Hostname)
BuildRequires:  perl%{plv}(Template::Tiny) >= 0.11
BuildRequires:  perl%{plv}(Term::ANSIColor) >= 2.02
BuildRequires:  perl%{plv}(Test::Deep)
BuildRequires:  perl%{plv}(Test::Dir)
BuildRequires:  perl%{plv}(Test::Exception)
BuildRequires:  perl%{plv}(Test::File)
BuildRequires:  perl%{plv}(Test::File::Contents) >= 0.20
BuildRequires:  perl%{plv}(Test::MockModule) >= 0.05
BuildRequires:  perl%{plv}(Test::More) >= 0.94
BuildRequires:  perl%{plv}(Test::NoWarnings) >= 0.083
BuildRequires:  perl%{plv}(Throwable) >= 0.200009
BuildRequires:  perl%{plv}(Time::HiRes)
BuildRequires:  perl%{plv}(Try::Tiny)
BuildRequires:  perl%{plv}(Type::Library) >= 0.040
BuildRequires:  perl%{plv}(Type::Tiny::XS) >= 0.010
BuildRequires:  perl%{plv}(Type::Utils)
BuildRequires:  perl%{plv}(Types::Standard)
BuildRequires:  perl%{plv}(URI)
BuildRequires:  perl%{plv}(URI::db) >= 0.15
BuildRequires:  perl%{plv}(User::pwent)
BuildRequires:  perl%{plv}(utf8)
BuildRequires:  perl%{plv}(warnings)
Requires:       perl%{plv}(Class::XSAccessor) >= 1.18
Requires:       perl%{plv}(Clone)
Requires:       perl%{plv}(Config)
Requires:       perl%{plv}(Config::GitLike) >= 1.11
Requires:       perl%{plv}(constant)
Requires:       perl%{plv}(DateTime)
Requires:       perl%{plv}(DateTime::TimeZone)
Requires:       perl%{plv}(Devel::StackTrace) >= 1.30
Requires:       perl%{plv}(Digest::SHA)
Requires:       perl%{plv}(Encode)
Requires:       perl%{plv}(Encode::Locale)
Requires:       perl%{plv}(File::Basename)
Requires:       perl%{plv}(File::Copy)
Requires:       perl%{plv}(File::HomeDir)
Requires:       perl%{plv}(File::Path)
Requires:       perl%{plv}(File::Temp)
Requires:       perl%{plv}(Getopt::Long)
Requires:       perl%{plv}(Hash::Merge)
Requires:       perl%{plv}(IO::Pager)
Requires:       perl%{plv}(IPC::Run3)
Requires:       perl%{plv}(IPC::System::Simple) >= 1.17
Requires:       perl%{plv}(List::Util)
Requires:       perl%{plv}(List::MoreUtils)
Requires:       perl%{plv}(Locale::TextDomain) >= 1.20
Requires:       perl%{plv}(Moo) => 1.002000
Requires:       perl%{plv}(Moo::Role)
Requires:       perl%{plv}(Moo::sification)
Requires:       perl%{plv}(namespace::autoclean) >= 0.16
Requires:       perl%{plv}(parent)
Requires:       perl%{plv}(overload)
Requires:       perl%{plv}(Path::Class)
Requires:       perl%{plv}(PerlIO::utf8_strict)
Requires:       perl%{plv}(Pod::Escapes)
Requires:       perl%{plv}(Pod::Find)
Requires:       perl%{plv}(Pod::Usage)
Requires:       perl%{plv}(POSIX)
Requires:       perl%{plv}(Scalar::Util)
Requires:       perl%{plv}(StackTrace::Auto)
Requires:       perl%{plv}(strict)
Requires:       perl%{plv}(String::Formatter)
Requires:       perl%{plv}(String::ShellQuote)
Requires:       perl%{plv}(Sub::Exporter)
Requires:       perl%{plv}(Sub::Exporter::Util)
Requires:       perl%{plv}(Sys::Hostname)
Requires:       perl%{plv}(Template::Tiny) >= 0.11
Requires:       perl%{plv}(Term::ANSIColor) >= 2.02
Requires:       perl%{plv}(Throwable) >= 0.200009
Requires:       perl%{plv}(Try::Tiny)
Requires:       perl%{plv}(Type::Library) >= 0.040
Requires:       perl%{plv}(Type::Tiny::XS) >= 0.010
Requires:       perl%{plv}(Type::Utils)
Requires:       perl%{plv}(Types::Standard)
Requires:       perl%{plv}(URI)
Requires:       perl%{plv}(URI::db) >= 0.15
Requires:       perl%{plv}(User::pwent)
Requires:       perl%{plv}(utf8)
Requires:       perl%{plv}(warnings)

%define etcdir %(%{__perl} -MConfig -E 'say "$Config{prefix}/etc"')

%description
This application, `sqitch`, provides a simple yet robust interface for
database change management. The philosophy and functionality is inspired by
Git.

%prep
%setup -q -n App-Sqitch-%{version}

%build
%{__perl} Build.PL installdirs=vendor destdir=$RPM_BUILD_ROOT
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# Grab and tweak the .packlist file.
find $RPM_BUILD_ROOT -type f -name .packlist -exec mv {} . \;
perl -i -pe 's/[.]([13](?:pm)?)$/.$1*/g' .packlist
perl -i -pe "s{^\Q$RPM_BUILD_ROOT}{}g" .packlist

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files -f .packlist
%defattr(-,root,root,-)
%doc Changes META.json README.md
%config %{etcdir}/*

%package pg
Summary:        Sane database change management for PostgreSQL
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       postgresql >= 8.4.0
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::Pg) >= 2.0.0
Provides:       sqitch-pg

%description pg
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch PostgreSQL support.

%files pg
# No additional files required.

%package sqlite
Summary:        Sane database change management for SQLite
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       sqlite
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::SQLite) >= 1.37
Provides:       sqitch-sqlite

%description sqlite
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch SQLite support.

%files sqlite
# No additional files required.

%package oracle
Summary:        Sane database change management for Oracle
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       oracle-instantclient11.2-sqlplus
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::Oracle) >= 1.23
Provides:       sqitch-oracle

%description oracle
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch Oracle support.

%files oracle
# No additional files required.

%package mysql
Summary:        Sane database change management for MySQL
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       mysql >= 5.0.0
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::mysql) >= 4.018
Requires:       perl%{plv}(MySQL::Config)
Provides:       sqitch-mysql

%description mysql
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch MySQL support.

%files mysql
# No additional files required.

%package firebird
Summary:        Sane database change management for Firebird
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       firebird >= 2.5.0
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::Firebird) >= 1.11
Requires:       perl%{plv}(Time::HiRes)
Requires:       perl%{plv}(Time::Local)
BuildRequires:  firebird >= 2.5.0
Provides:       sqitch-firebird

%description firebird
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqitch Firebird support.

%files firebird
# No additional files required.

%package vertica
Summary:        Sane database change management for Vertica
Group:          Development/Libraries
Requires:       sqitch >= %{version}
Requires:       libverticaodbc.so
Requires:       /opt/vertica/bin/vsql
Requires:       perl%{plv}(DBI)
Requires:       perl%{plv}(DBD::ODBC) >= 1.43
Provides:       sqitch-vertica

%description vertica
Sqitch provides a simple yet robust interface for database change management.
The philosophy and functionality is inspired by Git. This package bundles the
Sqitch Vertica support.

%files vertica
# No additional files required.

%changelog
* Thu Feb 11 2016 David E. Wheeler <david.wheeler@iovation.com> 0.9994-2
- Add perl(Pod::Escapes) to work around missing dependencies in Pod::Simple.
  https://github.com/perl-pod/pod-simple/issues/84.

* Fri Jan 8 2016 David E. Wheeler <david.wheeler@iovation.com> 0.9994-1
- Reduced required MySQL version to 5.0.
- Upgrade to v0.9994.

* Mon Aug 17 2015 David E. Wheeler <david.wheeler@iovation.com> 0.9993-1
- Upgrade to v0.9993.

* Wed May 20 2015 David E. Wheeler <david.wheeler@iovation.com> 0.9992-1
- Upgrade to v0.9992.
- Add perl(DateTime::TimeZone).
- Add Provides.
- Replace requirement for firebird-classic with firebird.
- Replace requirement for vertica-client with /opt/vertica/bin/vsql and
  libverticaodbc.so.

* Fri Mar 3 2015 David E. Wheeler <david.wheeler@iovation.com> 0.9991-1
- Upgrade to v0.9991.
- Reduced required MySQL version to 5.1.

* Thu Feb 12 2015 David E. Wheeler <david.wheeler@iovation.com> 0.999-1
- Upgrade to v0.999.

* Thu Jan 15 2015 David E. Wheeler <david.wheeler@iovation.com> 0.998-1
- Upgrade to v0.998.
- Require Path::Class v0.33 when building.

* Tue Nov 4 2014 David E. Wheeler <david.wheeler@iovation.com> 0.997-1
- Upgrade to v0.997.

* Fri Sep 5 2014 David E. Wheeler <david.wheeler@iovation.com> 0.996-1
- Upgrade to v0.996.
- Remove Moose and Mouse dependencies.
- Add Moo dependencies.
- Add Type::Library and related module dependencies.
- Switch from Digest::SHA1 to Digest::SHA.
- Require the Moo-backed version of Config::GitLike.
- Remove Role module dependencies.
- Require URI::db v0.15.
- Add sqitch-vertica.

* Sun Jul 13 2014 David E. Wheeler <david.wheeler@iovation.com> 0.995-1
- Upgrade to v0.995.

* Thu Jun 19 2014 David E. Wheeler <david.wheeler@iovation.com> 0.994-1
- Upgrade to v0.994.

* Wed Jun 4 2014 David E. Wheeler <david.wheeler@iovation.com> 0.993-1
- Upgrade to v0.993.

* Tue Mar 4 2014 David E. Wheeler <david.wheeler@iovation.com> 0.992-1
- Upgrade to v0.992.

* Thu Jan 16 2014 David E. Wheeler <david.wheeler@iovation.com> 0.991-1
- Upgrade to v0.991.
- Remove File::Which from sqitch-firebird.

* Fri Jan 4 2014 David E. Wheeler <david.wheeler@iovation.com> 0.990-1
- Upgrade to v0.990.
- Add sqitch-firebird.
- Add target command and arguments.
- Add support for arbitrary change script templating.
- Add --open-editor option.

* Thu Nov 21 2013 David E. Wheeler <david.wheeler@iovation.com> 0.983-1
- Upgrade to v0.983.
- Require DBD::Pg 2.0.0 or higher.

* Wed Sep 18 2013 David E. Wheeler <david.wheeler@iovation.com> 0.982-2
- No longer include template files ending in .default in the RPM.
- All files in the etc dir now treated as configuration files.
- The etc and inc files are no longer treated as documentation.

* Wed Sep 11 2013 David E. Wheeler <david.wheeler@iovation.com> 0.982-1
- Upgrade to v0.982.
- Require Clone.

* Thu Sep 5 2013 David E. Wheeler <david.wheeler@iovation.com> 0.981-1
- Upgrade to v0.981.

* Tue Aug 28 2013 David E. Wheeler <david.wheeler@iovation.com> 0.980-1
- Upgrade to v0.980.
- Require Encode::Locale.
- Require DBD::SQLite 1.37.
- Require PostgreSQL 8.4.0.
- Remove FindBin requirement.
- Add sqitch-mysql.

* Wed Jul 3 2013 David E. Wheeler <david.wheeler@iovation.com> 0.973-1
- Upgrade to v0.973.

* Fri May 31 2013 David E. Wheeler <david.wheeler@iovation.com> 0.972-1
- Upgrade to v0.972.

* Sat May 18 2013 David E. Wheeler <david.wheeler@iovation.com> 0.971-1
- Upgrade to v0.971.

* Wed May 8 2013 David E. Wheeler <david.wheeler@iovation.com> 0.970-1
- Upgrade to v0.970.
- Add sqitch-oracle.

* Tue Apr 23 2013 David E. Wheeler <david.wheeler@iovation.com> 0.965-1
- Upgrade to v0.965.

* Mon Apr 15 2013 David E. Wheeler <david.wheeler@iovation.com> 0.964-1
- Upgrade to v0.964.

* Thu Apr 12 2013 David E. Wheeler <david.wheeler@iovation.com> 0.963-1
- Upgrade to v0.963.
- Add missing dependency on Devel::StackTrace 1.30.
- Remove dependency on Git::Wrapper.

* Tue Apr 10 2013 David E. Wheeler <david.wheeler@iovation.com> 0.962-1
- Upgrade to v0.962.

* Tue Apr 9 2013 David E. Wheeler <david.wheeler@iovation.com> 0.961-1
- Upgrade to v0.961.

* Mon Apr 8 2013 David E. Wheeler <david.wheeler@iovation.com> 0.960-2
- Add missing dependency on Git::Wrapper.

* Fri Apr 5 2013 David E. Wheeler <david.wheeler@iovation.com> 0.960-1
- Upgrade to v0.960.
- Add sqitch-sqlite.

* Thu Feb 21 2013 David E. Wheeler <david.wheeler@iovation.com> 0.953-1
- Upgrade to v0.953.

* Fri Jan 12 2013 David E. Wheeler <david.wheeler@iovation.com> 0.952-1
- Upgrade to v0.952.

* Mon Jan 7 2013 David E. Wheeler <david.wheeler@iovation.com> 0.951-1
- Upgrade to v0.951.

* Thu Jan 3 2013 David E. Wheeler <david.wheeler@iovation.com> 0.950-1
- Upgrade to v0.950.

* Fri Dec 3 2012 David E. Wheeler <david.wheeler@iovation.com> 0.940-1
- Upgrade to v0.940.

* Fri Oct 12 2012 David E. Wheeler <david.wheeler@iovation.com> 0.938-1
- Upgrade to v0.938.

* Tue Oct 9 2012 David E. Wheeler <david.wheeler@iovation.com> 0.937-1
- Upgrade to v0.937.

* Tue Oct 9 2012 David E. Wheeler <david.wheeler@iovation.com> 0.936-1
- Upgrade to v0.936.

* Tue Oct 2 2012 David E. Wheeler <david.wheeler@iovation.com> 0.935-1
- Upgrade to v0.935.

* Fri Sep 28 2012 David E. Wheeler <david.wheeler@iovation.com> 0.934-1
- Upgrade to v0.934.

* Thu Sep 27 2012 David E. Wheeler <david.wheeler@iovation.com> 0.933-1
- Upgrade to v0.933.

* Wed Sep 26 2012 David E. Wheeler <david.wheeler@iovation.com> 0.932-1
- Upgrade to v0.932.

* Tue Sep 25 2012 David E. Wheeler <david.wheeler@iovation.com> 0.931-1
- Upgrade to v0.931.

* Fri Aug 31 2012 David E. Wheeler <david.wheeler@iovation.com> 0.930-1
- Upgrade to v0.93.

* Thu Aug 30 2012 David E. Wheeler <david.wheeler@iovation.com> 0.922-1
- Upgrade to v0.922.

* Wed Aug 29 2012 David E. Wheeler <david.wheeler@iovation.com> 0.921-1
- Upgrade to v0.921.

* Tue Aug 28 2012 David E. Wheeler <david.wheeler@iovation.com> 0.920-1
- Upgrade to v0.92.

* Tue Aug 28 2012 David E. Wheeler <david.wheeler@iovation.com> 0.913-1
- Upgrade to v0.913.

* Mon Aug 27 2012 David E. Wheeler <david.wheeler@iovation.com> 0.912-1
- Upgrade to v0.912.

* Wed Aug 23 2012 David E. Wheeler <david.wheeler@iovation.com> 0.911-1
- Upgrade to v0.911.

* Wed Aug 22 2012 David E. Wheeler <david.wheeler@iovation.com> 0.91-1
- Upgrade to v0.91.

* Mon Aug 20 2012 David E. Wheeler <david.wheeler@iovation.com> 0.902-1
- Upgrade to v0.902.

* Mon Aug 20 2012 David E. Wheeler <david.wheeler@iovation.com> 0.901-1
- Upgrade to v0.901.

* Mon Aug 13 2012 David E. Wheeler <david.wheeler@iovation.com> 0.82-2
- Require Config::GitLike 1.09, which offers better encoding support an other
  bug fixes.

* Fri Aug 03 2012 David E. Wheeler <david.wheeler@iovation.com> 0.82-2
- Specfile autogenerated by cpanspec 1.78.
