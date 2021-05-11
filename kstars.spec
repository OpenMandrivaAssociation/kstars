%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
%bcond_without indilib
%define indilib_version 0.9.8
%define xplanet_version 1.2.1

%global optflags %{optflags} -Wno-error=format-security

Summary:	A Desktop Planetarium
Name:		kstars
Version:	3.5.3
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kstars
Source0:	http://download.kde.org/%{stable}/%{name}/%{name}-%{version}.tar.xz
Source10:	%{name}.rpmlintrc

BuildRequires:	xplanet >= %{xplanet_version}
BuildRequires:	cmake(QJSON)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Plotting)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(Qt5DataVisualization)
BuildRequires:	cmake(StellarSolver)
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(pthread-stubs)
BuildRequires:	pkgconfig(wcslib)
%if %{with indilib}
BuildRequires:	pkgconfig(libindi) >= %{indilib_version}
BuildRequires:	indilib-devel-static >= %{indilib_version}
Requires:	indilib >= %{indilib_version}
%endif

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%files -f %{name}.lang
%doc COPYING COPYING.DOC README.md README.ephemerides README.customize README.images README.planetmath README.timekeeping AUTHORS 
%{_datadir}/applications/org.kde.kstars.desktop
%{_bindir}/kstars
%{_datadir}/metainfo/org.kde.kstars.appdata.xml
%{_datadir}/config.kcfg/kstars.kcfg
%{_datadir}/knotifications5/kstars.notifyrc
%{_iconsdir}/*/*/apps/kstars.*
%{_libdir}/libhtmesh.a
%{_datadir}/kstars
%{_datadir}/sounds/*.ogg
#{_sysconfdir}/dbus-1/system.d/org.kde.kf5auth.kstars.conf
#{_libdir}/libexec/kauth/kauth_kstars_helper
#{_datadir}/dbus-1/system-services/org.kde.kf5auth.kstars.service
#{_datadir}/polkit-1/actions/org.kde.kf5auth.kstars.policy

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%cmake_kde5   \
              -DINDI_BUILD_UNITTESTS=OFF

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
