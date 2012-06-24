%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Thesaurus-ISO
Summary:	Text::Thesaurus::ISO perl module
Summary(pl):	Modu� perla Text::Thesaurus::ISO
Name:		perl-Text-Thesaurus-ISO
Version:	1.0
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Thesaurus::ISO perl module.

%description -l pl
Modu� perla Text::Thesaurus::ISO.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
