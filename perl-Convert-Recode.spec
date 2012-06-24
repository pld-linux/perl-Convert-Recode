%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Recode
Summary:	Convert::Recode - make mapping functions between character sets
Summary(pl):	Convert::Recode - tworzenie funkcji odwzorowuj�cych zestawy znak�w
Name:		perl-Convert-Recode
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fac0f792e6ff23b8837750d35485c095
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
Requires:	recode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Convert::Recode Perl module can provide mapping functions between
character sets on demand.  It depends on GNU recode to provide the raw
mapping data.

%description -l pl
Modu� Perla Convert::Recode s�u�y do udost�pniania na ��danie funkcji
odwzorowania pomi�dzy zestawami znak�w. Jest on zale�ny od programu
GNU recode, kt�ry udost�pnia niskopoziomowe dane dla odwzorowa�.
jest nak�adk� dla programu GNU recode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Convert/Recode.pm
%{_mandir}/man3/*
