%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
%bcond_without indilib
%define indilib_version 2.0.0
%define xplanet_version 1.2.1

%global optflags %{optflags} -Wno-error=format-security

Summary:	A Desktop Planetarium
Name:		kstars
Version:	3.7.6
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/kstars
Source0:	https://download.kde.org/%{stable}/%{name}/%{name}-%{version}.tar.xz
Source10:	%{name}.rpmlintrc

Patch0:  https://invent.kde.org/education/kstars/-/merge_requests/1460.patch

BuildRequires:	xplanet >= %{xplanet_version}
BuildRequires:	cmake(QJSON)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
#BuildRequires:	cmake(KF6Init)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Plotting)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(Qt6DataVisualization)
BuildRequires:	cmake(StellarSolver)
BuildRequires:	libfli-devel
BuildRequires:	libnova-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(pthread-stubs)
BuildRequires:	pkgconfig(wcslib)
%if %{with indilib}
BuildRequires:	pkgconfig(libindi) >= %{indilib_version}
BuildRequires:	indilib-devel-static >= %{indilib_version}
# Without indilib installed, we get an error message, but
# kstars is still usable for people who don't have a telescope
# or similar device attached - so let's make it a soft dependency
Recommends:	indilib >= %{indilib_version}
%endif
BuildSystem:	cmake
BuildOption:	-DINDI_BUILD_UNITTESTS:BOOL=OFF
BuildOption:	-DBUILD_TESTING:BOOL=OFF
BuildOption:	-DBUILD_QT5:BOOL=OFF

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%install -a
# Translated info_url files get installed in the wrong place
mv %{buildroot}/kstars/* %{buildroot}%{_datadir}/kstars/
rmdir %{buildroot}/kstars

%files -f %{name}.lang
%doc README.md README.ephemerides README.customize README.images README.planetmath README.timekeeping AUTHORS 
%{_datadir}/applications/org.kde.kstars.desktop
%{_bindir}/kstars
%{_datadir}/metainfo/org.kde.kstars.appdata.xml
%{_datadir}/config.kcfg/kstars.kcfg
%{_iconsdir}/*/*/apps/kstars.*
%{_libdir}/libhtmesh.a
%{_datadir}/kstars
%{_datadir}/sounds/*.ogg
%{_datadir}/knotifications6/kstars.notifyrc
