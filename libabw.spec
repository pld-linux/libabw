%define		apiversion	0.0
Summary:	A library for import of AbiWord files
Name:		libabw
Version:	0.0.1
Release:	1
License:	MPLv2.0
Group:		Libraries
URL:		http://www.freedesktop.org/wiki/Software/libabw/
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz
# Source0-md5:	92a82f736aeaf22204ee95bbbcdd69a1
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	gperf
BuildRequires:	libwpd-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{name} is a library for import of AbiWord files.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:	Tools to transform AbiWord files into other formats
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform AbiWord files into other formats. Currently
supported: XHTML, raw, text.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-werror \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la

# we install API docs directly from build
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS COPYING.MPL README
%attr(755,root,root) %{_libdir}/%{name}-%{apiversion}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}-%{apiversion}.so.0

%files devel
%defattr(644,root,root,755)
%doc ChangeLog docs/doxygen/html
%{_includedir}/%{name}-%{apiversion}
%attr(755,root,root) %{_libdir}/%{name}-%{apiversion}.so
%{_pkgconfigdir}/%{name}-%{apiversion}.pc

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/abw2raw
%attr(755,root,root) %{_bindir}/abw2text
%attr(755,root,root) %{_bindir}/abw2html
