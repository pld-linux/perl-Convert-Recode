%define	pdir	Convert
%define	pnam	Recode
%include	/usr/lib/rpm/macros.perl
Summary:	Convert-Recode perl module
Summary(pl):	Modu³ perla Convert-Recode
Name:		perl-Convert-Recode
Version:	1.03
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
Requires:	recode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Recode is a front end to the GNU recode program.

%description -l pl
Convert-Recode jest nak³adk± dla programu GNU recode.

%prep
%setup -q -n Convert-Recode-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Convert/Recode.pm
%{_mandir}/man3/*
