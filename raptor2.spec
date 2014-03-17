%define major 0
%define libname %mklibname %{name}_ %{major}
%define devname %mklibname -d %{name}

Summary:	Raptor RDF Parser Toolkit for Redland
Name:		raptor2
Version:	2.0.13
Release:	1
License:	LGPLv2
Group:		Development/Other
Url:		http://librdf.org/raptor/
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
Conflicts:	raptor < 2.0.0

%track
prog %name = {
	url = http://librdf.org/raptor/
	version = %{version}
	regex = "Latest version:	(__VER__) \("
}

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:	Dynamic libraries from %{name}
Group:		System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{devname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static --with-html-dir=/dev/null
%make

%install
%makeinstall_std

# cleanup
rm -rf %{buildroot}/dev/null

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_bindir}/rapper
%{_mandir}/man1/rap*
%{_mandir}/man3/libraptor2.3*

%files -n %{libname}
%{_libdir}/libraptor2.so.%{major}*

%files -n %{devname}
%{_libdir}/libraptor2.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

