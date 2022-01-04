#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : breeze
Version  : 5.23.5
Release  : 65
URL      : https://download.kde.org/stable/plasma/5.23.5/breeze-5.23.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.23.5/breeze-5.23.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: breeze-bin = %{version}-%{release}
Requires: breeze-data = %{version}-%{release}
Requires: breeze-lib = %{version}-%{release}
Requires: breeze-license = %{version}-%{release}
Requires: breeze-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : fftw-dev
BuildRequires : frameworkintegration-dev
BuildRequires : kcmutils-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kdecoration-dev
BuildRequires : ki18n-dev
BuildRequires : qtbase-dev mesa-dev

%description
Printer test page
Can be used by cups by replacing
/usr/share/cups/data/default-testpage.pdf

%package bin
Summary: bin components for the breeze package.
Group: Binaries
Requires: breeze-data = %{version}-%{release}
Requires: breeze-license = %{version}-%{release}

%description bin
bin components for the breeze package.


%package data
Summary: data components for the breeze package.
Group: Data

%description data
data components for the breeze package.


%package dev
Summary: dev components for the breeze package.
Group: Development
Requires: breeze-lib = %{version}-%{release}
Requires: breeze-bin = %{version}-%{release}
Requires: breeze-data = %{version}-%{release}
Provides: breeze-devel = %{version}-%{release}
Requires: breeze = %{version}-%{release}

%description dev
dev components for the breeze package.


%package lib
Summary: lib components for the breeze package.
Group: Libraries
Requires: breeze-data = %{version}-%{release}
Requires: breeze-license = %{version}-%{release}

%description lib
lib components for the breeze package.


%package license
Summary: license components for the breeze package.
Group: Default

%description license
license components for the breeze package.


%package locales
Summary: locales components for the breeze package.
Group: Default

%description locales
locales components for the breeze package.


%prep
%setup -q -n breeze-5.23.5
cd %{_builddir}/breeze-5.23.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641315665
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641315665
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/breeze
cp %{_builddir}/breeze-5.23.5/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/breeze/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/breeze-5.23.5/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/breeze/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/breeze-5.23.5/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/breeze/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/breeze-5.23.5/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/breeze/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/breeze-5.23.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/breeze/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/breeze-5.23.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/breeze/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/breeze-5.23.5/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/breeze/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/breeze-5.23.5/cursors/Breeze/COPYING %{buildroot}/usr/share/package-licenses/breeze/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/breeze-5.23.5/cursors/Breeze/COPYING-ICONS %{buildroot}/usr/share/package-licenses/breeze/4da8b3e7cf68bdf289e59afa90e3483c83bb6824
cp %{_builddir}/breeze-5.23.5/cursors/Breeze_Snow/COPYING %{buildroot}/usr/share/package-licenses/breeze/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/breeze-5.23.5/cursors/Breeze_Snow/COPYING-ICONS %{buildroot}/usr/share/package-licenses/breeze/4da8b3e7cf68bdf289e59afa90e3483c83bb6824
pushd clr-build
%make_install
popd
%find_lang breeze_kwin_deco
%find_lang breeze_style_config

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/breezetobreezelight
/usr/lib64/kconf_update_bin/kde4breeze

%files bin
%defattr(-,root,root,-)
/usr/bin/breeze-settings5

%files data
%defattr(-,root,root,-)
/usr/share/QtCurve/Breeze.qtcurve
/usr/share/color-schemes/Breeze.colors
/usr/share/color-schemes/BreezeDark.colors
/usr/share/color-schemes/BreezeHighContrast.colors
/usr/share/color-schemes/BreezeLight.colors
/usr/share/icons/Breeze_Snow/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/Breeze_Snow/cursors/00008160000006810000408080010102
/usr/share/icons/Breeze_Snow/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/Breeze_Snow/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/Breeze_Snow/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/Breeze_Snow/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/Breeze_Snow/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/Breeze_Snow/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/Breeze_Snow/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/Breeze_Snow/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/Breeze_Snow/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/Breeze_Snow/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/Breeze_Snow/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/Breeze_Snow/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/Breeze_Snow/cursors/alias
/usr/share/icons/Breeze_Snow/cursors/all-scroll
/usr/share/icons/Breeze_Snow/cursors/arrow
/usr/share/icons/Breeze_Snow/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/Breeze_Snow/cursors/bottom_left_corner
/usr/share/icons/Breeze_Snow/cursors/bottom_right_corner
/usr/share/icons/Breeze_Snow/cursors/bottom_side
/usr/share/icons/Breeze_Snow/cursors/cell
/usr/share/icons/Breeze_Snow/cursors/center_ptr
/usr/share/icons/Breeze_Snow/cursors/circle
/usr/share/icons/Breeze_Snow/cursors/closedhand
/usr/share/icons/Breeze_Snow/cursors/col-resize
/usr/share/icons/Breeze_Snow/cursors/color-picker
/usr/share/icons/Breeze_Snow/cursors/context-menu
/usr/share/icons/Breeze_Snow/cursors/copy
/usr/share/icons/Breeze_Snow/cursors/cross
/usr/share/icons/Breeze_Snow/cursors/crossed_circle
/usr/share/icons/Breeze_Snow/cursors/crosshair
/usr/share/icons/Breeze_Snow/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/Breeze_Snow/cursors/default
/usr/share/icons/Breeze_Snow/cursors/dnd-copy
/usr/share/icons/Breeze_Snow/cursors/dnd-move
/usr/share/icons/Breeze_Snow/cursors/dnd-no-drop
/usr/share/icons/Breeze_Snow/cursors/dnd-none
/usr/share/icons/Breeze_Snow/cursors/down-arrow
/usr/share/icons/Breeze_Snow/cursors/draft
/usr/share/icons/Breeze_Snow/cursors/e-resize
/usr/share/icons/Breeze_Snow/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/Breeze_Snow/cursors/ew-resize
/usr/share/icons/Breeze_Snow/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/Breeze_Snow/cursors/fleur
/usr/share/icons/Breeze_Snow/cursors/forbidden
/usr/share/icons/Breeze_Snow/cursors/grab
/usr/share/icons/Breeze_Snow/cursors/grabbing
/usr/share/icons/Breeze_Snow/cursors/h_double_arrow
/usr/share/icons/Breeze_Snow/cursors/half-busy
/usr/share/icons/Breeze_Snow/cursors/hand1
/usr/share/icons/Breeze_Snow/cursors/hand2
/usr/share/icons/Breeze_Snow/cursors/help
/usr/share/icons/Breeze_Snow/cursors/ibeam
/usr/share/icons/Breeze_Snow/cursors/left-arrow
/usr/share/icons/Breeze_Snow/cursors/left_ptr
/usr/share/icons/Breeze_Snow/cursors/left_ptr_help
/usr/share/icons/Breeze_Snow/cursors/left_ptr_watch
/usr/share/icons/Breeze_Snow/cursors/left_side
/usr/share/icons/Breeze_Snow/cursors/link
/usr/share/icons/Breeze_Snow/cursors/move
/usr/share/icons/Breeze_Snow/cursors/n-resize
/usr/share/icons/Breeze_Snow/cursors/ne-resize
/usr/share/icons/Breeze_Snow/cursors/nesw-resize
/usr/share/icons/Breeze_Snow/cursors/no-drop
/usr/share/icons/Breeze_Snow/cursors/not-allowed
/usr/share/icons/Breeze_Snow/cursors/ns-resize
/usr/share/icons/Breeze_Snow/cursors/nw-resize
/usr/share/icons/Breeze_Snow/cursors/nwse-resize
/usr/share/icons/Breeze_Snow/cursors/openhand
/usr/share/icons/Breeze_Snow/cursors/pencil
/usr/share/icons/Breeze_Snow/cursors/pirate
/usr/share/icons/Breeze_Snow/cursors/plus
/usr/share/icons/Breeze_Snow/cursors/pointer
/usr/share/icons/Breeze_Snow/cursors/pointing_hand
/usr/share/icons/Breeze_Snow/cursors/progress
/usr/share/icons/Breeze_Snow/cursors/question_arrow
/usr/share/icons/Breeze_Snow/cursors/right-arrow
/usr/share/icons/Breeze_Snow/cursors/right_ptr
/usr/share/icons/Breeze_Snow/cursors/right_side
/usr/share/icons/Breeze_Snow/cursors/row-resize
/usr/share/icons/Breeze_Snow/cursors/s-resize
/usr/share/icons/Breeze_Snow/cursors/sb_h_double_arrow
/usr/share/icons/Breeze_Snow/cursors/sb_v_double_arrow
/usr/share/icons/Breeze_Snow/cursors/se-resize
/usr/share/icons/Breeze_Snow/cursors/size-bdiag
/usr/share/icons/Breeze_Snow/cursors/size-fdiag
/usr/share/icons/Breeze_Snow/cursors/size-hor
/usr/share/icons/Breeze_Snow/cursors/size-ver
/usr/share/icons/Breeze_Snow/cursors/size_all
/usr/share/icons/Breeze_Snow/cursors/size_bdiag
/usr/share/icons/Breeze_Snow/cursors/size_fdiag
/usr/share/icons/Breeze_Snow/cursors/size_hor
/usr/share/icons/Breeze_Snow/cursors/size_ver
/usr/share/icons/Breeze_Snow/cursors/split_h
/usr/share/icons/Breeze_Snow/cursors/split_v
/usr/share/icons/Breeze_Snow/cursors/sw-resize
/usr/share/icons/Breeze_Snow/cursors/text
/usr/share/icons/Breeze_Snow/cursors/top_left_arrow
/usr/share/icons/Breeze_Snow/cursors/top_left_corner
/usr/share/icons/Breeze_Snow/cursors/top_right_corner
/usr/share/icons/Breeze_Snow/cursors/top_side
/usr/share/icons/Breeze_Snow/cursors/up-arrow
/usr/share/icons/Breeze_Snow/cursors/v_double_arrow
/usr/share/icons/Breeze_Snow/cursors/vertical-text
/usr/share/icons/Breeze_Snow/cursors/w-resize
/usr/share/icons/Breeze_Snow/cursors/wait
/usr/share/icons/Breeze_Snow/cursors/watch
/usr/share/icons/Breeze_Snow/cursors/wayland-cursor
/usr/share/icons/Breeze_Snow/cursors/whats_this
/usr/share/icons/Breeze_Snow/cursors/x-cursor
/usr/share/icons/Breeze_Snow/cursors/xterm
/usr/share/icons/Breeze_Snow/cursors/zoom-in
/usr/share/icons/Breeze_Snow/cursors/zoom-out
/usr/share/icons/Breeze_Snow/index.theme
/usr/share/icons/breeze_cursors/cursors/00000000000000020006000e7e9ffc3f
/usr/share/icons/breeze_cursors/cursors/00008160000006810000408080010102
/usr/share/icons/breeze_cursors/cursors/03b6e0fcb3499374a867c041f52298f0
/usr/share/icons/breeze_cursors/cursors/08e8e1c95fe2fc01f976f1e063a24ccd
/usr/share/icons/breeze_cursors/cursors/1081e37283d90000800003c07f3ef6bf
/usr/share/icons/breeze_cursors/cursors/3085a0e285430894940527032f8b26df
/usr/share/icons/breeze_cursors/cursors/3ecb610c1bf2410f44200f48c40d3599
/usr/share/icons/breeze_cursors/cursors/4498f0e0c1937ffe01fd06f973665830
/usr/share/icons/breeze_cursors/cursors/5c6cd98b3f3ebcb1f9c7f1c204630408
/usr/share/icons/breeze_cursors/cursors/6407b0e94181790501fd1e167b474872
/usr/share/icons/breeze_cursors/cursors/640fb0e74195791501fd1ed57b41487f
/usr/share/icons/breeze_cursors/cursors/9081237383d90e509aa00f00170e968f
/usr/share/icons/breeze_cursors/cursors/9d800788f1b08800ae810202380a0822
/usr/share/icons/breeze_cursors/cursors/a2a266d0498c3104214a47bd64ab0fc8
/usr/share/icons/breeze_cursors/cursors/alias
/usr/share/icons/breeze_cursors/cursors/all-scroll
/usr/share/icons/breeze_cursors/cursors/arrow
/usr/share/icons/breeze_cursors/cursors/b66166c04f8c3109214a4fbd64a50fc8
/usr/share/icons/breeze_cursors/cursors/bottom_left_corner
/usr/share/icons/breeze_cursors/cursors/bottom_right_corner
/usr/share/icons/breeze_cursors/cursors/bottom_side
/usr/share/icons/breeze_cursors/cursors/cell
/usr/share/icons/breeze_cursors/cursors/center_ptr
/usr/share/icons/breeze_cursors/cursors/circle
/usr/share/icons/breeze_cursors/cursors/closedhand
/usr/share/icons/breeze_cursors/cursors/col-resize
/usr/share/icons/breeze_cursors/cursors/color-picker
/usr/share/icons/breeze_cursors/cursors/context-menu
/usr/share/icons/breeze_cursors/cursors/copy
/usr/share/icons/breeze_cursors/cursors/cross
/usr/share/icons/breeze_cursors/cursors/crossed_circle
/usr/share/icons/breeze_cursors/cursors/crosshair
/usr/share/icons/breeze_cursors/cursors/d9ce0ab605698f320427677b458ad60b
/usr/share/icons/breeze_cursors/cursors/default
/usr/share/icons/breeze_cursors/cursors/dnd-copy
/usr/share/icons/breeze_cursors/cursors/dnd-move
/usr/share/icons/breeze_cursors/cursors/dnd-no-drop
/usr/share/icons/breeze_cursors/cursors/dnd-none
/usr/share/icons/breeze_cursors/cursors/down-arrow
/usr/share/icons/breeze_cursors/cursors/draft
/usr/share/icons/breeze_cursors/cursors/e-resize
/usr/share/icons/breeze_cursors/cursors/e29285e634086352946a0e7090d73106
/usr/share/icons/breeze_cursors/cursors/ew-resize
/usr/share/icons/breeze_cursors/cursors/fcf21c00b30f7e3f83fe0dfd12e71cff
/usr/share/icons/breeze_cursors/cursors/fleur
/usr/share/icons/breeze_cursors/cursors/forbidden
/usr/share/icons/breeze_cursors/cursors/grab
/usr/share/icons/breeze_cursors/cursors/grabbing
/usr/share/icons/breeze_cursors/cursors/h_double_arrow
/usr/share/icons/breeze_cursors/cursors/half-busy
/usr/share/icons/breeze_cursors/cursors/hand1
/usr/share/icons/breeze_cursors/cursors/hand2
/usr/share/icons/breeze_cursors/cursors/help
/usr/share/icons/breeze_cursors/cursors/ibeam
/usr/share/icons/breeze_cursors/cursors/left-arrow
/usr/share/icons/breeze_cursors/cursors/left_ptr
/usr/share/icons/breeze_cursors/cursors/left_ptr_help
/usr/share/icons/breeze_cursors/cursors/left_ptr_watch
/usr/share/icons/breeze_cursors/cursors/left_side
/usr/share/icons/breeze_cursors/cursors/link
/usr/share/icons/breeze_cursors/cursors/move
/usr/share/icons/breeze_cursors/cursors/n-resize
/usr/share/icons/breeze_cursors/cursors/ne-resize
/usr/share/icons/breeze_cursors/cursors/nesw-resize
/usr/share/icons/breeze_cursors/cursors/no-drop
/usr/share/icons/breeze_cursors/cursors/not-allowed
/usr/share/icons/breeze_cursors/cursors/ns-resize
/usr/share/icons/breeze_cursors/cursors/nw-resize
/usr/share/icons/breeze_cursors/cursors/nwse-resize
/usr/share/icons/breeze_cursors/cursors/openhand
/usr/share/icons/breeze_cursors/cursors/pencil
/usr/share/icons/breeze_cursors/cursors/pirate
/usr/share/icons/breeze_cursors/cursors/plus
/usr/share/icons/breeze_cursors/cursors/pointer
/usr/share/icons/breeze_cursors/cursors/pointing_hand
/usr/share/icons/breeze_cursors/cursors/progress
/usr/share/icons/breeze_cursors/cursors/question_arrow
/usr/share/icons/breeze_cursors/cursors/right-arrow
/usr/share/icons/breeze_cursors/cursors/right_ptr
/usr/share/icons/breeze_cursors/cursors/right_side
/usr/share/icons/breeze_cursors/cursors/row-resize
/usr/share/icons/breeze_cursors/cursors/s-resize
/usr/share/icons/breeze_cursors/cursors/sb_h_double_arrow
/usr/share/icons/breeze_cursors/cursors/sb_v_double_arrow
/usr/share/icons/breeze_cursors/cursors/se-resize
/usr/share/icons/breeze_cursors/cursors/size-bdiag
/usr/share/icons/breeze_cursors/cursors/size-fdiag
/usr/share/icons/breeze_cursors/cursors/size-hor
/usr/share/icons/breeze_cursors/cursors/size-ver
/usr/share/icons/breeze_cursors/cursors/size_all
/usr/share/icons/breeze_cursors/cursors/size_bdiag
/usr/share/icons/breeze_cursors/cursors/size_fdiag
/usr/share/icons/breeze_cursors/cursors/size_hor
/usr/share/icons/breeze_cursors/cursors/size_ver
/usr/share/icons/breeze_cursors/cursors/split_h
/usr/share/icons/breeze_cursors/cursors/split_v
/usr/share/icons/breeze_cursors/cursors/sw-resize
/usr/share/icons/breeze_cursors/cursors/text
/usr/share/icons/breeze_cursors/cursors/top_left_arrow
/usr/share/icons/breeze_cursors/cursors/top_left_corner
/usr/share/icons/breeze_cursors/cursors/top_right_corner
/usr/share/icons/breeze_cursors/cursors/top_side
/usr/share/icons/breeze_cursors/cursors/up-arrow
/usr/share/icons/breeze_cursors/cursors/v_double_arrow
/usr/share/icons/breeze_cursors/cursors/vertical-text
/usr/share/icons/breeze_cursors/cursors/w-resize
/usr/share/icons/breeze_cursors/cursors/wait
/usr/share/icons/breeze_cursors/cursors/watch
/usr/share/icons/breeze_cursors/cursors/wayland-cursor
/usr/share/icons/breeze_cursors/cursors/whats_this
/usr/share/icons/breeze_cursors/cursors/x-cursor
/usr/share/icons/breeze_cursors/cursors/xterm
/usr/share/icons/breeze_cursors/cursors/zoom-in
/usr/share/icons/breeze_cursors/cursors/zoom-out
/usr/share/icons/breeze_cursors/index.theme
/usr/share/icons/hicolor/scalable/apps/breeze-settings.svgz
/usr/share/kconf_update/breezetobreezelight.upd
/usr/share/kconf_update/kde4breeze.upd
/usr/share/kservices5/breezedecorationconfig.desktop
/usr/share/kservices5/breezestyleconfig.desktop
/usr/share/kstyle/themes/breeze.themerc
/usr/share/wallpapers/Next/contents/images/1024x768.png
/usr/share/wallpapers/Next/contents/images/1080x1920.png
/usr/share/wallpapers/Next/contents/images/1280x1024.png
/usr/share/wallpapers/Next/contents/images/1280x800.png
/usr/share/wallpapers/Next/contents/images/1366x768.png
/usr/share/wallpapers/Next/contents/images/1440x900.png
/usr/share/wallpapers/Next/contents/images/1600x1200.png
/usr/share/wallpapers/Next/contents/images/1680x1050.png
/usr/share/wallpapers/Next/contents/images/1920x1080.png
/usr/share/wallpapers/Next/contents/images/1920x1200.png
/usr/share/wallpapers/Next/contents/images/2560x1440.png
/usr/share/wallpapers/Next/contents/images/2560x1600.png
/usr/share/wallpapers/Next/contents/images/3200x1800.png
/usr/share/wallpapers/Next/contents/images/3200x2000.png
/usr/share/wallpapers/Next/contents/images/360x720.png
/usr/share/wallpapers/Next/contents/images/3840x2160.png
/usr/share/wallpapers/Next/contents/images/440x247.png
/usr/share/wallpapers/Next/contents/images/5120x2880.png
/usr/share/wallpapers/Next/contents/images/720x1440.png
/usr/share/wallpapers/Next/contents/images/base_size.png
/usr/share/wallpapers/Next/contents/images/vertical_base_size.png
/usr/share/wallpapers/Next/contents/screenshot.png
/usr/share/wallpapers/Next/metadata.desktop

%files dev
%defattr(-,root,root,-)
/usr/lib64/cmake/Breeze/BreezeConfig.cmake
/usr/lib64/cmake/Breeze/BreezeConfigVersion.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbreezecommon5.so.5
/usr/lib64/libbreezecommon5.so.5.23.5
/usr/lib64/qt5/plugins/kstyle_breeze_config.so
/usr/lib64/qt5/plugins/org.kde.kdecoration2/breezedecoration.so
/usr/lib64/qt5/plugins/styles/breeze.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/breeze/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/breeze/4da8b3e7cf68bdf289e59afa90e3483c83bb6824
/usr/share/package-licenses/breeze/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/breeze/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/breeze/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/breeze/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/breeze/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/breeze/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f breeze_kwin_deco.lang -f breeze_style_config.lang
%defattr(-,root,root,-)

