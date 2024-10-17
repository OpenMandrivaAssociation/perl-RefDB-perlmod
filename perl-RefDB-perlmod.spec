%define module	RefDB-perlmod

Name:		perl-%{module}
Version:	1.2
Release:	8
Summary:	%{module} module for perl
License:	GPLv2+
Group:		Development/Perl
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.gz
URL:		https://refdb.sourceforge.net

BuildRequires:	perl-devel
BuildRequires:	perl(Text::Iconv)
Provides:	perl(RefDB)
BuildArch:	noarch

%description
Perl component for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/RefDB
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-5mdv2010.0
+ Revision: 430533
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-4mdv2009.0
+ Revision: 258317
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-3mdv2009.0
+ Revision: 246354
- rebuild

* Thu Dec 27 2007 Adam Williamson <awilliamson@mandriva.org> 1.2-1mdv2008.1
+ Revision: 138563
- rebuild for new era
- slight spec clean
- new version 1.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.1-4mdv2008.0
+ Revision: 86824
- rebuild


* Wed Aug 23 2006 Stï¿½phane Tï¿½letchï¿½a <steletch@mandriva.org> 0.4.1-3
- tabs and spaces fixes

* Fri May 05 2006 Stéphane Téletchéa <steletch@mandriva.org> 0.4.1-2mdk
- Add Provides

* Thu May 04 2006 Stéphane Téletchéa <steletch@mandriva.org> 0.4.1-1mdk
+ New version which fixes some perl tests.

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdk
- Add BuildRequires

2006-05-02 Stéphane Téletchéa <steletch@mandriva.org> 0.4-1mdk
- Initial Mandriva release

