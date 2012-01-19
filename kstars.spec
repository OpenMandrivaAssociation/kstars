%define with_indilib 1
%define indilib_version 0.8
%define eigen_version 2.0.3
%define xplanet_version 1.2.1

Name: kstars
Summary: A Desktop Planetarium
Version: 4.8.0
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kstars
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: pkgconfig(eigen2) >= %eigen_version
BuildRequires: pkgconfig(cfitsio)
BuildRequires: xplanet >= %xplanet_version
BuildRequires: libfli-devel

%if %with_indilib
BuildRequires: pkgconfig(libindi) >= %{indilib_version}
Requires: indilib >= %{indilib_version}
%endif

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%files
%doc COPYING COPYING.DOC README README.ephemerides README.customize README.images README.planetmath README.timekeeping AUTHORS
%_kde_appsdir/kstars
%_kde_bindir/kstars
%_kde_libdir/libhtmesh.a
%_kde_iconsdir/*/*/apps/kstars.*
%_kde_datadir/applications/kde4/kstars.desktop
%_kde_datadir/config.kcfg/kstars.kcfg
%_kde_datadir/config/kstars.knsrc
%_kde_docdir/HTML/*/kstars

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches


%build

%cmake_kde4 	
%make

%install
%makeinstall_std -C build

