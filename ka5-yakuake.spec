#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		qtver		5.15.2
%define		kaname		yakuake
Summary:	KDE Terminal Emulator
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	7826f44253d1a1de895c839fa6f4d5e2
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yakuake.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yakuake
%{_desktopdir}/org.kde.yakuake.desktop
%{_datadir}/dbus-1/services/org.kde.yakuake.service
%{_iconsdir}/hicolor/128x128/apps/yakuake.png
%{_iconsdir}/hicolor/16x16/apps/yakuake.png
%{_iconsdir}/hicolor/22x22/apps/yakuake.png
%{_iconsdir}/hicolor/256x256/apps/yakuake.png
%{_iconsdir}/hicolor/32x32/apps/yakuake.png
%{_iconsdir}/hicolor/48x48/apps/yakuake.png
%{_iconsdir}/hicolor/64x64/apps/yakuake.png
%{_datadir}/knotifications5/yakuake.notifyrc
%{_datadir}/metainfo/org.kde.yakuake.appdata.xml
%{_datadir}/yakuake
%{_datadir}/knsrcfiles/yakuake.knsrc
