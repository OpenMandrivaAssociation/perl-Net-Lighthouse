%define upstream_name    Net-Lighthouse
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	A Perl interface to lighthouseapp.com
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/bestpractical/net-lighthouse
Source0:	https://cpan.metacpan.org/authors/id/S/SU/SUNNAVY/Net-Lighthouse-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Mock::LWP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(XML::TreePP)
BuildRequires:	perl(YAML::Syck)
BuildArch:	noarch

%description
A Perl interface to lighthouseapp.com, by means of its official api.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654263
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 542874
- import perl-Net-Lighthouse


* Thu May 06 2010 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist
