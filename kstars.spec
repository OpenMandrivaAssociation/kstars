%bcond_without indilib
%define indilib_version 0.9.8
%define xplanet_version 1.2.1

Summary:	A Desktop Planetarium
Name:		kstars
Version:	15.04.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kstars
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
Source10:	%{name}.rpmlintrc
BuildRequires:	xplanet >= %{xplanet_version}
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5Gui)                                                                          
BuildRequires:  cmake(Qt5Qml)                                                                          
BuildRequires:  cmake(Qt5Quick)                                                                        
BuildRequires:  cmake(Qt5Xml)                                                                          
BuildRequires:  cmake(Qt5Sql)                                                                          
BuildRequires:  cmake(Qt5Svg)                                                                          
BuildRequires:  cmake(Qt5OpenGL)                                                                       
BuildRequires:  cmake(Qt5PrintSupport)                                                                 
BuildRequires:  cmake(Qt5Multimedia)                                                                   
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5DocTools)                                                                     
BuildRequires:  cmake(KF5GuiAddons)                                                                    
BuildRequires:  cmake(KF5WidgetsAddons)                                                                
BuildRequires:  cmake(KF5NewStuff)                                                                     
BuildRequires:  cmake(KF5DBusAddons)                                                                   
BuildRequires:  cmake(KF5I18n)                                                                         
BuildRequires:  cmake(KF5Init)                                                                         
BuildRequires:  cmake(KF5JobWidgets)                                                                   
BuildRequires:  cmake(KF5KIO)                                                                          
BuildRequires:  cmake(KF5WindowSystem)                                                                 
BuildRequires:  cmake(KF5XmlGui)                                                                       
BuildRequires:  cmake(KF5Plotting)                                                                     
BuildRequires:  cmake(KF5TextEditor)                                                                   
BuildRequires:  cmake(KF5IconThemes)   
BuildRequires:	libfli-devel
BuildRequires:	python-kde4-devel
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(eigen3)
BuildRequires:	pkgconfig(QJson)
%if %{with indilib}
BuildRequires:	pkgconfig(libindi) >= %{indilib_version}
BuildRequires:	indilib-devel-static >= %{indilib_version}
Requires:	indilib >= %{indilib_version}
%endif
Requires:	python-kde4

%description
KStars is a Desktop Planetarium for KDE. It provides an accurate graphical
simulation of the night sky, from any location on Earth, at any date and
time. The display includes 130,000 stars, 13,000 deep-sky objects,all 8
planets, the Sun and Moon, and thousands of comets and asteroids.

%files
%doc COPYING COPYING.DOC README README.ephemerides README.customize README.images README.planetmath README.timekeeping AUTHORS                                            
%doc %{_docdir}/HTML/*/kstars                                                                     
%{_datadir}/applications/org.kde.kstars.desktop                                                                                                                                          
%{_bindir}/kstars                                                                                      
%{_sysconfdir}/xdg/kstars.knsrc                                                                        
%{_datadir}/appdata/kstars.appdata.xml 
%{_datadir}/kxmlgui5/kstars/kstarsui.rc
%{_datadir}/kxmlgui5/kstars/fitsviewer.rc
%{_datadir}/config.kcfg/kstars.kcfg                                                                    
%{_iconsdir}/*/*/apps/kstars.*                                                                         
%{_libdir}/libhtmesh.a   

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

