%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Text-Thesaurus-ISO perl module
Summary(pl):	Modu� perla Text-Thesaurus-ISO
Name:		perl-Text-Thesaurus-ISO
Version:	1.0
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Thesaurus-ISO-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-Thesaurus-ISO perl module. 

%description -l pl
Modu� perla Text-Thesaurus-ISO.

%prep
%setup -q -n Text-Thesaurus-ISO-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Thesaurus/ISO
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Text/Thesaurus/ISO.pm
%{perl_sitelib}/auto/Text/Thesaurus/ISO
%{perl_sitearch}/auto/Text/Thesaurus/ISO

%{_mandir}/man3/*
