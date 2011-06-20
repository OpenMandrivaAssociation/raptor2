%define name    raptor2
%define version 2.0.3
%define release %mkrel 2

%define major	0
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname -d %{name}

Summary:   	Raptor RDF Parser Toolkit for Redland
Name:      	%{name}
Version:   	%{version}
Release:   	%{release}
License: 	GPL LGPL
Group:     	Development/Other
Source:    	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
URL:       	http://librdf.org/raptor/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:  curl-devel
Conflicts:	raptor < 2.0.0

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n	%{libname}
Dynamic libraries from %{name}.

%package -n	%{develname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{develname}
Libraries and includes files for developing programs based on %{name}.

%prep
%setup -qn %{name}-%{version}

%build
%configure2_5x --disable-static --with-html-dir=/dev/null
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%if "%{_lib}" == "lib64"
perl -pi -e "s|-L/usr/lib\b|-L%{_libdir}|g" %{buildroot}%{_libdir}/*.la
%endif

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE.txt NEWS README
%{_mandir}/man1/rap*
%{_mandir}/man3/libraptor2.3*
%{_bindir}/rapper

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
