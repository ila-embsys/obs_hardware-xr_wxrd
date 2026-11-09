#
# spec file for package wxrd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           wxrd
Version:        g80f40e3
Release:        0
Summary:        A prototype-quality standalone client for xrdesktop
License:        MIT
Url:            https://gitlab.freedesktop.org/xrdesktop/wxrd
Source:         %{name}-%{version}.tar.bz2
Patch1:         wxrd-0001-Fix-wlr-types-path.patch
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wlroots) >= 0.15.0
BuildRequires:  pkgconfig(wlroots) <= 0.16.0
BuildRequires:  pkgconfig(xrdesktop-0.16)
BuildRequires:  pkgconfig(wayland-scanner)

%description
A prototype-quality standalone client for xrdesktop based on wlroots and the wxrc codebase

%prep
%setup -q
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/wxrd

%changelog
