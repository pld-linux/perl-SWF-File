#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SWF
%define	pnam	File
Summary:	SWF::File - create SWF file
Summary(pl):	SWF::File - tworzenie plików SWF
Name:		perl-SWF-File
Version:	0.36
Release:	0.2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-Data-TemporaryBag
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWF::File module can be used to make SWF (Macromedia Flash(R)) movie.
SWF::File is a subclass of SWF::BinStream::Write, so you can pack
SWF::Element::Tags in it.

%description -l pl
Modu³ SWF::File mo¿e byæ u¿ywany do tworzenia filmów SWF (Macromedia
Flash(R)). SWF::File to podklasa SWF::BinStream::Write, wiêc mo¿na w
niej umieszczaæ SWF::Element::Tags.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
# if module isn't noarch, use:
# %{__make} \
#	OPTIMIZE="%{rpmcflags}"

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
%{perl_vendorlib}/FIXME*
%{perl_vendorarch}/FIXME*
%{_mandir}/man3/*
