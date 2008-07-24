%define module	RefDB-perlmod
%define name	perl-%{module}
%define version 1.2
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPLv2+
Group:		Development/Perl
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.gz
URL:		http://refdb.sourceforge.net
BuildRequires:  perl(Text::Iconv)
Provides:	perl(RefDB)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-root

%description
Perl component for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/RefDB
%{_mandir}/*/*

