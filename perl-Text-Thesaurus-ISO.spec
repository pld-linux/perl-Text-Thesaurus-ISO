#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Thesaurus-ISO
Summary:	Text::Thesaurus::ISO - A class to handle ISO thesaurii
Summary(pl):	Text::Thesaurus::ISO - klasa do obs³ugi tezaurusów ISO
Name:		perl-Text-Thesaurus-ISO
Version:	1.0
Release:	12
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module defines an abstract ROADS Thesaurus object and a number of
methods that operate on these objects.  These methods allow new
Thesaurus objects to be created, specify what Thesaurus file to use,
retrieve all the information from the thesaurus concerning a given
term, find broader terms for a given term and find narrower terms for
a given term.

%description -l pl
Ten modu³ definiuje abstrakcyjny obiekt ROADS Thesaurus oraz wiele
metod operuj±cych na tych obiektach. Metody te pozwalaj± na tworzenie
nowych obiektów Thesaurus, wskazywanie pliku, jaki ma byæ u¿ywany,
odczytywania wszystkich informacji z tezaurusa dotycz±cych podanego
wyra¿enia, szukania wyra¿enia bardziej ogólneg do podanego oraz
szukania wyra¿eñ o wê¿szym znaczeniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_sitelib}/Text/Thesaurus
%{perl_sitelib}/Text/Thesaurus/ISO.pm
# empty autosplit.ix
#%dir %{perl_sitelib}/auto/Text/Thesaurus
#%dir %{perl_sitelib}/auto/Text/Thesaurus/ISO
#%{perl_sitelib}/auto/Text/Thesaurus/ISO/autosplit.ix
%{_mandir}/man3/*
