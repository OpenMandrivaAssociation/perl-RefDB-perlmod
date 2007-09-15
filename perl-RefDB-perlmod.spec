%define module	RefDB-perlmod
%define name	perl-%{module}
%define version 0.4.1
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.bz2
Url:		http://refdb.sourceforge.net
BuildRequires:  perl(Text::Iconv)
Provides:	perl(RefDB)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
Perlmod package for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes version
%{perl_vendorlib}/RefDB
%{_mandir}/*/*

