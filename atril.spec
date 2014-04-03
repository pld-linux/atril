# TODO
# - atril.desktop provides mimetypes for all possible choices, yet some of
#   them are in subpackages (backend-foo). Are multiple .desktop files possible
#   for the same application?
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_without	caja		# Caja plugin
%bcond_with	gtk3		# use GTK+ 3.x instead of 2.x

Summary:	Atril - MATE Desktop document viewer for multiple document formats
Summary(pl.UTF-8):	Atril - przeglądarka dokumentów w wielu formatach dla środowiska MATE
Name:		atril
Version:	1.8.0
Release:	2
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	e7626e8e3cffe6ee256cc6cf7acb7524
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
%{?with_caja:BuildRequires:	caja-devel}
BuildRequires:	djvulibre-devel >= 3.5.17
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gobject-introspection-devel >= 0.6
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.24.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	kpathsea-devel
BuildRequires:	libgxps-devel >= 0.0.1
BuildRequires:	libsecret-devel >= 0.15
BuildRequires:	libspectre-devel >= 0.2.0
BuildRequires:	libtiff-devel >= 3.6
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	mate-common
BuildRequires:	mate-icon-theme-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.14.0
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	scrollkeeper
BuildRequires:	t1lib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.22.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Requires:	xorg-lib-libSM >= 1.0.0
Suggests:	atril-backend-djvu
Suggests:	atril-backend-dvi
Suggests:	atril-backend-pdf
Suggests:	atril-backend-ps
Suggests:	atril-backend-xps
%{!?with_gtk3:Suggests:	gtk+2-cups}
%{?with_gtk3:Suggests:	gtk+3-cups}
# sr@Latn vs. sr@latin
Obsoletes:	mate-document-viewer
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		backendsdir	%{_libdir}/atril/3/backends

%description
Atril is a document viewer for multiple document formats like PDF and
PostScript. Atril is a fork of Evince.

%description -l pl.UTF-8
Atril jest przeglądarką dokumentów w wielu formatach takich jak PDF
czy PostScript. Jest to odgałęzienie pakietu Evince.

%package libs
Summary:	Atril shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone przeglądarki Atril
Group:		X11/Libraries
Requires:	glib2 >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.22.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
Obsoletes:	mate-document-viewer-libs

%description libs
Atril shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone przeglądarki Atril.

%package devel
Summary:	Header files for Atril libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek przeglądarki Atril
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.26.0
%{!?with_gtk3:Requires:	gtk+2-devel >= 2:2.22.0}
%{?with_gtk3:Requires:	gtk+3-devel >= 3.0.0}
Obsoletes:	mate-document-viewer-devel

%description devel
Header files for Atril libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek przeglądarki Atril.

%package apidocs
Summary:	Atril API documentation
Summary(pl.UTF-8):	Dokumentacja API aplikacji Atril
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mate-document-viewer-apidocs
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Atril API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API aplikacji Atril.

%package backend-djvu
Summary:	View DJVu documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów DjVu w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	djvulibre >= 3.5.17
Obsoletes:	mate-document-viewer-backend-djvu

%description backend-djvu
View DJVu documents with Atril.

%description backend-djvu -l pl.UTF-8
Przeglądanie dokumentów DjVu w przeglądarce Atril.

%package backend-dvi
Summary:	View DVI documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów DVI w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mate-document-viewer-backend-dvi

%description backend-dvi
View DVI documents with Atril.

%description backend-dvi -l pl.UTF-8
Przeglądanie dokumentów DVI w przeglądarce Atril.

%package backend-pdf
Summary:	View PDF documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów PDF w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	poppler-glib >= 0.14.0
Obsoletes:	mate-document-viewer-backend-pdf

%description backend-pdf
View PDF documents with Atril.

%description backend-pdf -l pl.UTF-8
Przeglądanie dokumentów PDF w przeglądarce Atril.

%package backend-ps
Summary:	View PostScript documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów PostScript w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libspectre >= 0.2.0
Obsoletes:	mate-document-viewer-backend-ps

%description backend-ps
View PostScript documents with Atril.

%description backend-ps -l pl.UTF-8
Przeglądanie dokumentów PostScript w przeglądarce Atril.

%package backend-xps
Summary:	View XPS documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów XPS w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libgxps >= 0.0.1
Obsoletes:	mate-document-viewer-backend-xps

%description backend-xps
View XPS documents with Atril.

%description backend-xps -l pl.UTF-8
Przeglądanie dokumentów XPS w przeglądarce Atril.

%package -n caja-extension-atril
Summary:	Atril extension for Caja file manager
Summary(pl.UTF-8):	Rozszerzenie Atril dla zarządcy plików Caja
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	caja
Obsoletes:	mate-file-manager-extension-atril

%description -n caja-extension-atril
Shows Atril document properties in Caja file manager.

%description -n caja-extension-atril -l pl.UTF-8
Pokazuje właściwości dokumentu przeglądarki Atril w zarządcy plików
Caja.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_caja:--disable-caja} \
	--enable-comics \
	--enable-djvu \
	--enable-dvi \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-introspection \
	--enable-t1lib \
	--enable-pdf \
	--enable-pixbuf \
	--disable-silent-rules \
	--disable-static \
	--enable-tiff \
	%{?with_gtk3:--with-gtk=3.0} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatril*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/atril/3/backends/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cmn

# mate < 1.5 did not exist in pld, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/atril.convert

%find_lang atril --with-mate --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%scrollkeeper_update_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%scrollkeeper_update_postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f atril.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/atril
%attr(755,root,root) %{_bindir}/atril-previewer
%attr(755,root,root) %{_bindir}/atril-thumbnailer
%attr(755,root,root) %{_libexecdir}/atril-convert-metadata
%attr(755,root,root) %{_libexecdir}/atrild
%dir %{_libdir}/atril
%dir %{_libdir}/atril/3
%dir %{_libdir}/atril/3/backends
%attr(755,root,root) %{_libdir}/atril/3/backends/libcomicsdocument.so
%{_libdir}/atril/3/backends/comicsdocument.atril-backend
%attr(755,root,root) %{_libdir}/atril/3/backends/libpixbufdocument.so
%{_libdir}/atril/3/backends/pixbufdocument.atril-backend
%attr(755,root,root) %{_libdir}/atril/3/backends/libtiffdocument.so
%{_libdir}/atril/3/backends/tiffdocument.atril-backend
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/atril
%{_datadir}/thumbnailers/atril.thumbnailer
%{_mandir}/man1/atril.1*
%{_mandir}/man1/atril-previewer.1*
%{_mandir}/man1/atril-thumbnailer.1*
%{_desktopdir}/atril.desktop
%{_iconsdir}/hicolor/*x*/apps/atril.png
%{_iconsdir}/hicolor/scalable/apps/atril.svg

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatrildocument.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatrildocument.so.3
%attr(755,root,root) %{_libdir}/libatrilview.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libatrilview.so.3
%{_libdir}/girepository-1.0/AtrilDocument-1.5.0.typelib
%{_libdir}/girepository-1.0/AtrilView-1.5.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatrildocument.so
%attr(755,root,root) %{_libdir}/libatrilview.so
%{_datadir}/gir-1.0/AtrilDocument-1.5.0.gir
%{_datadir}/gir-1.0/AtrilView-1.5.0.gir
%{_includedir}/atril
%{_pkgconfigdir}/atril-document-1.5.0.pc
%{_pkgconfigdir}/atril-view-1.5.0.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/atril
%{_gtkdocdir}/libatrildocument-1.5.0
%{_gtkdocdir}/libatrilview-1.5.0
%endif

%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend

%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libdvidocument.so
%{_libdir}/atril/3/backends/dvidocument.atril-backend

%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libpsdocument.so
%{_libdir}/atril/3/backends/psdocument.atril-backend

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libpdfdocument.so
%{_libdir}/atril/3/backends/pdfdocument.atril-backend

%files backend-xps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libxpsdocument.so
%{_libdir}/atril/3/backends/xpsdocument.atril-backend

%if %{with caja}
%files -n caja-extension-atril
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libatril-properties-page.so
%endif
