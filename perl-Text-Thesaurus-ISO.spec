%include	/usr/lib/rpm/macros.perl
Summary:	Text-Thesaurus-ISO perl module
Summary(pl):	Modu³ perla Text-Thesaurus-ISO
Name:		perl-Text-Thesaurus-ISO
Version:	1.0
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Thesaurus-ISO-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Thesaurus-ISO perl module.

%description -l pl
Modu³ perla Text-Thesaurus-ISO.

%prep
%setup -q -n Text-Thesaurus-ISO-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Thesaurus/ISO.pm
%{perl_sitelib}/auto/Text/Thesaurus/ISO
%{_mandir}/man3/*
