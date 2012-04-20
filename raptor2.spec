%define major	0
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname -d %{name}

Summary:   	Raptor RDF Parser Toolkit for Redland
Name:      	raptor2
Version:   	2.0.7
Release:   	1
License: 	GPL LGPL
Group:     	Development/Other
Source0:    	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
URL:       	http://librdf.org/raptor/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	libxml2-devel >= 2.6.8
BuildRequires:	libxslt-devel >= 1.0.18
BuildRequires:	curl-devel >= 7.12.0
BuildRequires:	gtk-doc
BuildRequires:	yajl-devel
Conflicts:	raptor < 2.0.0

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:         Dynamic libraries from %{name}
Group:           System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	gtk-doc
Requires:	%{libname} >= %{version}
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

# clean .la files
rm -f %{buildroot}%{_libdir}/*.la

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
