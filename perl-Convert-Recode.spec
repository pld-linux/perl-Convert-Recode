#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	Recode
Summary:	Convert::Recode - make mapping functions between character sets
Summary(pl):	Convert::Recode - tworzenie funkcji odwzorowuj±cych zestawy znaków
Name:		perl-Convert-Recode
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fac0f792e6ff23b8837750d35485c095
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	recode >= 3.5
Requires:	recode >= 3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Convert::Recode Perl module can provide mapping functions between
character sets on demand.  It depends on GNU recode to provide the raw
mapping data.

%description -l pl
Modu³ Perla Convert::Recode s³u¿y do udostêpniania na ¿±danie funkcji
odwzorowania pomiêdzy zestawami znaków. Jest on zale¿ny od programu
GNU recode, który udostêpnia niskopoziomowe dane dla odwzorowañ.
jest nak³adk± dla programu GNU recode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc Changes README
%{perl_vendorlib}/Convert/Recode.pm
%{_mandir}/man3/*
