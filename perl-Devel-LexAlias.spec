#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-Devel-LexAlias
Version  : 0.05
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-LexAlias-0.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-LexAlias-0.05.tar.gz
Summary  : alias lexical variables
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-LexAlias-perl = %{version}-%{release}
Requires: perl(Devel::Caller)
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::Caller)
BuildRequires : perl(PadWalker)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-Devel-LexAlias package.
Group: Development
Provides: perl-Devel-LexAlias-devel = %{version}-%{release}
Requires: perl-Devel-LexAlias = %{version}-%{release}

%description dev
dev components for the perl-Devel-LexAlias package.


%package perl
Summary: perl components for the perl-Devel-LexAlias package.
Group: Default
Requires: perl-Devel-LexAlias = %{version}-%{release}

%description perl
perl components for the perl-Devel-LexAlias package.


%prep
%setup -q -n Devel-LexAlias-0.05
cd %{_builddir}/Devel-LexAlias-0.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::LexAlias.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
