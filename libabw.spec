#
# Conditional build:
%bcond_without	static_libs	# static library

%define		apiversion	0.1
Summary:	A library for import of AbiWord files
Summary(pl.UTF-8):	Biblioteka do importowania plików AbiWorda
Name:		libabw
Version:	0.1.2
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://dev-www.libreoffice.org/src/libabw/%{name}-%{version}.tar.xz
# Source0-md5:	201f477df7ea90d362c389c145c0f352
URL:		http://www.freedesktop.org/wiki/Software/libabw/
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf >= 3.0.0
BuildRequires:	librevenge-devel >= 0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libabw is a library for import of AbiWord files.

%description -l pl.UTF-8
libabw to biblioteka do importowania plików AbiWorda.

%package devel
Summary:	Development files for libabw
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libabw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librevenge-devel >= 0.0
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0
Requires:	zlib-devel

%description devel
This package contains the header files for developing applications
that use libabw.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki i pliki nagłówkowe do tworzenia
aplikacji wykorzystujących bibliotekę libabw.

%package static
Summary:	Static libabw library
Summary(pl.UTF-8):	Statyczna biblioteka libabw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libabw library.

%description static -l pl.UTF-8
Statyczna biblioteka libabw.

%package apidocs
Summary:	API documentation for libabw library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libabw
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libabw library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libabw.

%package tools
Summary:	Tools to transform AbiWord files into other formats
Summary(pl.UTF-8):	Narzędzia do przekształcania plików AbiWorda do innych formatów
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform AbiWord files into other formats. Currently
supported: XHTML, raw, text.

%description tools -l pl.UTF-8
Narzędzia do przekształcania plików AbiWorda do innych formatów.
Obecnie obsługiwane są: XHTML, surowy, tekst.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# we install API docs directly from build
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libabw-%{apiversion}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libabw-%{apiversion}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libabw-%{apiversion}.so
%{_includedir}/libabw-%{apiversion}
%{_pkgconfigdir}/libabw-%{apiversion}.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libabw-%{apiversion}.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc docs/doxygen/html/*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abw2raw
%attr(755,root,root) %{_bindir}/abw2text
%attr(755,root,root) %{_bindir}/abw2html
