%define major 0
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname -d %{name}

Summary:	Raptor RDF Parser Toolkit for Redland
Name:		raptor2
Version:	2.0.9
Release:	2
License:	GPL LGPL
Group:		Development/Other
URL:		http://librdf.org/raptor/
Source0:	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	gtk-doc
Conflicts:	raptor < 2.0.0

%track
prog %name = {
	url = http://librdf.org/raptor/
	version = %version
	regex = "Latest version: (__VER__) \("
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

%package -n	%{develname}
Summary:	Header files and static libraries from %{name}
Group:		Development/C
Requires:	gtk-doc
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static --with-html-dir=/dev/null
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# cleanup
rm -rf %{buildroot}/dev/null

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_mandir}/man1/rap*
%{_mandir}/man3/libraptor2.3*
%{_bindir}/rapper

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
