%define major 0
%define libname %mklibname %{name}_ %{major}
%define develname %mklibname -d %{name}

Summary:	Raptor RDF Parser Toolkit for Redland
Name:		raptor2
Version:	2.0.8
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


%changelog
* Fri Jun 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.0.8-1
+ Revision: 807503
- version update 2.0.8

* Mon Apr 23 2012 Oden Eriksson <oeriksson@mandriva.com> 2.0.7-1
+ Revision: 792771
- disable the yajl-devel dep for now
- 2.0.7
- fix deps
- various fixes

* Wed Nov 30 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.0.6-1
+ Revision: 735804
- version update 2.0.6

* Tue Sep 27 2011 Zé <ze@mandriva.org> 2.0.4-3
+ Revision: 701509
- bump release (since now includes gtk-doc in devel requires)
- fix devel provides to include release
- add gtk-doc into devel requires since its used by others that also need raptor2
-bump release
- avoid use of useless macros
- clean .la files
- add missing build require gtk-do

* Thu Aug 11 2011 Funda Wang <fwang@mandriva.org> 2.0.4-1
+ Revision: 693992
- new version 2.0.4

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-2
+ Revision: 686323
- avoid pulling 32 bit libraries on 64 bit arch

* Thu Jun 02 2011 Funda Wang <fwang@mandriva.org> 2.0.3-1
+ Revision: 682446
- update to new version 2.0.3

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-2
+ Revision: 669407
- mass rebuild

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 2.0.2-1
+ Revision: 647299
- update to new version 2.0.2

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2.0.0-3
+ Revision: 640211
- rebuild to obsolete old packages

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 2.0.0-2
+ Revision: 637009
- do not install docs so that it won't conflicts with raptor1

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 2.0.0-1
+ Revision: 636976
- import raptor2

