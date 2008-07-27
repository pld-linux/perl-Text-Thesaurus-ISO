#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Thesaurus-ISO
Summary:	Text::Thesaurus::ISO - a class to handle ISO thesaurii
Summary(pl.UTF-8):	Text::Thesaurus::ISO - klasa do obsługi tezaurusów ISO
Name:		perl-Text-Thesaurus-ISO
Version:	1.0
Release:	15
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd33a2bdae9519806b941ea8063fb1f5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module defines an abstract ROADS Thesaurus object and a number of
methods that operate on these objects.  These methods allow new
Thesaurus objects to be created, specify what Thesaurus file to use,
retrieve all the information from the thesaurus concerning a given
term, find broader terms for a given term and find narrower terms for
a given term.

%description -l pl.UTF-8
Ten moduł definiuje abstrakcyjny obiekt ROADS Thesaurus oraz wiele
metod operujących na tych obiektach. Metody te pozwalają na tworzenie
nowych obiektów Thesaurus, wskazywanie pliku, jaki ma być używany,
odczytywania wszystkich informacji z tezaurusa dotyczących podanego
wyrażenia, szukania wyrażenia bardziej ogólnego do podanego oraz
szukania wyrażeń o węższym znaczeniu.

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
%doc README
%dir %{perl_vendorlib}/Text/Thesaurus
%{perl_vendorlib}/Text/Thesaurus/ISO.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/Text/Thesaurus
#%dir %{perl_vendorlib}/auto/Text/Thesaurus/ISO
#%%{perl_vendorlib}/auto/Text/Thesaurus/ISO/autosplit.ix
%{_mandir}/man3/*
