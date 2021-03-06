#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	User
Summary:	User - API for locating user information regardless of OS
Summary(pl.UTF-8):	User - API do znajdowania informacji o użytkowniku niezależnie od systemu operacyjnego
Name:		perl-User
Version:	1.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/User/%{pdir}-%{version}.tar.gz
# Source0-md5:	53193e6c37b6d9efb726caf59a8aead7
URL:		http://search.cpan.org/dist/User/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is allows applications to retrieve per-user
characteristics.

%description -l pl.UTF-8
Ten moduł pozwala aplikacjom na pozyskanie informacji o użytkowniku.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/User.pm
%{_mandir}/man3/*
