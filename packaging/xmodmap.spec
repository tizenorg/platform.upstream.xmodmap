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
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
The xmodmap program is used to edit and display the keyboard modifier
map and keymap table that are used by client applications to convert
event keycodes into keysyms. It is usually run from the user's
session startup script to configure the keyboard according to personal
tastes.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
install -m0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/X11/Xmodmap
install -m0644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/X11/Xmodmap.remote

%files
%defattr(-,root,root)
%doc COPYING
%config %{_sysconfdir}/X11/Xmodmap
%config %{_sysconfdir}/X11/Xmodmap.remote
%{_bindir}/xmodmap
%{_mandir}/man1/xmodmap.1%{?ext_man}

%changelog
