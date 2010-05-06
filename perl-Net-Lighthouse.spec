%define upstream_name    Net-Lighthouse
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    a Perl interface to lighthouseapp.com
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(DateTime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Mouse)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::Mock::LWP)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(XML::TreePP)
BuildRequires: perl(YAML::Syck)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A Perl interface to lighthouseapp.com, by means of its official api.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


