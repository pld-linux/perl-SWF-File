#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SWF
%define	pnam	File
Summary:	SWF::File - create SWF file
Summary(pl.UTF-8):   SWF::File - tworzenie plików SWF
Name:		perl-SWF-File
Version:	0.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YS/YSAS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7319b35179edd24958fe1a92be8b3a0b
URL:		http://search.cpan.org/dist/SWF-File/
%{?with_tests:BuildRequires:	perl-Data-TemporaryBag >= 0.08}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Data-TemporaryBag >= 0.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF::File module can be used to make SWF (Macromedia Flash(R)) movie.
SWF::File is a subclass of SWF::BinStream::Write, so you can pack
SWF::Element::Tags in it.

%description -l pl.UTF-8
Moduł SWF::File może być używany do tworzenia filmów SWF (Macromedia
Flash(R)). SWF::File to podklasa SWF::BinStream::Write, więc można w
niej umieszczać SWF::Element::Tags.

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
%doc Changes README
%attr(755,root,root) %{_bindir}/dumpswf.plx
%dir %{perl_vendorlib}/SWF
%{perl_vendorlib}/SWF/*.pm
%dir %{perl_vendorlib}/SWF/BinStream
%{perl_vendorlib}/SWF/BinStream/*.pm
%dir %{perl_vendorlib}/SWF/BinStream/Codec
%{perl_vendorlib}/SWF/BinStream/Codec/*.pm
%{_mandir}/man3/*
