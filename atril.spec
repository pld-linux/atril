# TODO
# - atril.desktop provides mimetypes for all possible choices, yet some of
#   them are in subpackages (backend-foo). Are multiple .desktop files possible
#   for the same application?
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc documentation
%bcond_without	caja		# Caja plugin
%bcond_without	djvu		# DJVU support
%bcond_without	dvi		# DVI support
%bcond_without	epub		# ePub support
%bcond_without	ps		# PostScript support
%bcond_without	xps		# XPS support

Summary:	Atril - MATE Desktop document viewer for multiple document formats
Summary(pl.UTF-8):	Atril - przeglądarka dokumentów w wielu formatach dla środowiska MATE
Name:		atril
Version:	1.26.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	8d56fb4699cda95baff90b8d40e2d9ed
Patch0:		%{name}-kpathsea_config.patch
URL:		https://wiki.mate-desktop.org/mate-desktop/applications/atril/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.14.0
%{?with_caja:BuildRequires:	caja-devel >= 1.17.1}
%{?with_djvu:BuildRequires:	djvulibre-devel >= 3.5.17}
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gobject-introspection-devel >= 0.6
BuildRequires:	gtk+3-devel >= 3.22
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.13}
%{?with_epub:BuildRequires:	gtk-webkit4-devel >= 2.6.0}
%{?with_dvi:BuildRequires:	kpathsea-devel}
%{?with_xps:BuildRequires:	libgxps-devel >= 0.2.1}
BuildRequires:	libsecret-devel >= 0.15
%if %{with dvi} || %{with ps}
BuildRequires:	libspectre-devel >= 0.2.0
%endif
BuildRequires:	libtiff-devel >= 3.6
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxml2-devel >= 1:2.5.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.22.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	synctex-devel >= 1.21
BuildRequires:	t1lib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel >= 1.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.54.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+3 >= 3.22
Requires:	libsecret >= 0.15
Requires:	libtiff >= 3.6
Requires:	libxml2 >= 1:2.5.0
Requires:	xorg-lib-libSM >= 1.0.0
Suggests:	atril-backend-djvu
Suggests:	atril-backend-dvi
Suggests:	atril-backend-pdf
Suggests:	atril-backend-ps
Suggests:	atril-backend-xps
Suggests:	gtk+3-cups >= 3.22
Obsoletes:	mate-document-viewer < 1.8.0
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
Requires:	cairo >= 1.14.0
Requires:	glib2 >= 1:2.54.0
Requires:	gtk+3 >= 3.22
Requires:	synctex-libs >= 1.21
Obsoletes:	mate-document-viewer-libs < 1.8.0

%description libs
Atril shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone przeglądarki Atril.

%package devel
Summary:	Header files for Atril libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek przeglądarki Atril
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.54.0
Requires:	gtk+3-devel >= 3.22
Obsoletes:	mate-document-viewer-devel < 1.8.0

%description devel
Header files for Atril libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek przeglądarki Atril.

%package apidocs
Summary:	Atril API documentation
Summary(pl.UTF-8):	Dokumentacja API aplikacji Atril
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mate-document-viewer-apidocs < 1.8.0
BuildArch:	noarch

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
Obsoletes:	mate-document-viewer-backend-djvu < 1.8.0

%description backend-djvu
View DJVu documents with Atril.

%description backend-djvu -l pl.UTF-8
Przeglądanie dokumentów DjVu w przeglądarce Atril.

%package backend-dvi
Summary:	View DVI documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów DVI w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mate-document-viewer-backend-dvi < 1.8.0

%description backend-dvi
View DVI documents with Atril.

%description backend-dvi -l pl.UTF-8
Przeglądanie dokumentów DVI w przeglądarce Atril.

%package backend-epub
Summary:	View ePub documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów ePub w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2 >= 1:2.5.0
Requires:	gtk-webkit4 >= 2.6.0

%description backend-epub
View ePub documents with Atril.

%description backend-epub -l pl.UTF-8
Przeglądanie dokumentów ePub w przeglądarce Atril.

%package backend-pdf
Summary:	View PDF documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów PDF w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	poppler-glib >= 0.22.0
Obsoletes:	mate-document-viewer-backend-pdf < 1.8.0

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
Obsoletes:	mate-document-viewer-backend-ps < 1.8.0

%description backend-ps
View PostScript documents with Atril.

%description backend-ps -l pl.UTF-8
Przeglądanie dokumentów PostScript w przeglądarce Atril.

%package backend-xps
Summary:	View XPS documents with Atril
Summary(pl.UTF-8):	Przeglądanie dokumentów XPS w przeglądarce Atril
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	libgxps >= 0.2.1
Obsoletes:	mate-document-viewer-backend-xps < 1.8.0

%description backend-xps
View XPS documents with Atril.

%description backend-xps -l pl.UTF-8
Przeglądanie dokumentów XPS w przeglądarce Atril.

%package -n caja-extension-atril
Summary:	Atril extension for Caja file manager
Summary(pl.UTF-8):	Rozszerzenie Atril dla zarządcy plików Caja
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	caja >= 1.17.1
Obsoletes:	mate-file-manager-extension-atril < 1.8.0

%description -n caja-extension-atril
Shows Atril document properties in Caja file manager.

%description -n caja-extension-atril -l pl.UTF-8
Pokazuje właściwości dokumentu przeglądarki Atril w zarządcy plików
Caja.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_caja:--disable-caja} \
	--enable-comics \
	%{__enable_disable djvu} \
	%{__enable_disable dvi} \
	%{__enable_disable epub} \
	%{?with_apidocs:--enable-gtk-doc} \
	--enable-introspection \
	--enable-t1lib \
	--enable-pdf \
	--enable-pixbuf \
	%{__enable_disable ps} \
	--disable-schemas-compile \
	--disable-silent-rules \
	--disable-static \
	--enable-tiff \
	%{__enable_disable xps} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libatril*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/atril/3/backends/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,frp,ie,jv,ku_IQ,nqo,pms,ur_PK}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{ie,ku_IQ}

%find_lang atril --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f atril.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/atril
%attr(755,root,root) %{_bindir}/atril-previewer
%attr(755,root,root) %{_bindir}/atril-thumbnailer
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
%{_datadir}/atril
%{_datadir}/metainfo/atril.appdata.xml
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
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

%if %{with djvu}
%files backend-djvu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend
%endif

%if %{with dvi}
%files backend-dvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libdvidocument.so
%{_libdir}/atril/3/backends/dvidocument.atril-backend
%endif

%if %{with epub}
%files backend-epub
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libepubdocument.so
%{_libdir}/atril/3/backends/epubdocument.atril-backend
%endif

%files backend-pdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libpdfdocument.so
%{_libdir}/atril/3/backends/pdfdocument.atril-backend

%if %{with ps}
%files backend-ps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libpsdocument.so
%{_libdir}/atril/3/backends/psdocument.atril-backend
%endif

%if %{with xps}
%files backend-xps
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/atril/3/backends/libxpsdocument.so
%{_libdir}/atril/3/backends/xpsdocument.atril-backend
%endif

%if %{with caja}
%files -n caja-extension-atril
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libatril-properties-page.so
%{_datadir}/caja/extensions/libatril-properties-page.caja-extension
%endif
