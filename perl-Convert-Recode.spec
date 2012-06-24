%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Recode
Summary:	Convert::Recode perl module
Summary(pl):	Modu� perla Convert::Recode
Name:		perl-Convert-Recode
Version:	1.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
Requires:	recode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Recode is a front end to the GNU recode program.

%description -l pl
Convert::Recode jest nak�adk� dla programu GNU recode.

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
