%define upstream_name    B-Compiling
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    Expose PL_compiling to perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/B/B-Compiling-%{upstream_version}.tar.gz

BuildRequires: perl(B)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel

%description
This module exposes the perl interpreter's PL_compiling variable to perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.20.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.20.0-4
+ Revision: 680491
- mass rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild
    - rebuild

* Sun Aug 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 417016
- import perl-B-Compiling


* Sun Aug 16 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

