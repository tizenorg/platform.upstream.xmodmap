#
# spec file for package xmodmap
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           xmodmap
Version:        1.0.7
Release:        0
License:        MIT
Summary:        Utility to modify keymaps and pointer button mappings in X
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        Xmodmap.template
Source2:        Xmodmap.remote.template
# PATCH-FIX-UPSTREAM xmodmap-includes.patch fdo#48696 dimstar@opensuse.org -- asprintf is only defined with _GNU_SOURCE.
Patch0:         xmodmap-includes.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
The xmodmap program is used to edit and display the keyboard modifier
map and keymap table that are used by client applications to convert
event keycodes into keysyms. It is usually run from the user's
session startup script to configure the keyboard according to personal
tastes.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/Xmodmap
install -m0644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/Xmodmap.remote

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%config %{_sysconfdir}/X11/Xmodmap
%config %{_sysconfdir}/X11/Xmodmap.remote
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1%{?ext_man}

%changelog
