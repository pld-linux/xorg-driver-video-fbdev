Summary:	X.org video driver for framebuffer device
Summary(pl.UTF-8):	Sterownik obrazu X.org dla framebuffera
Name:		xorg-driver-video-fbdev
Version:	0.5.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-fbdev-%{version}.tar.xz
# Source0-md5:	6e1c5a31290c2613c9265e222c767ce3
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.18
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.18
Provides:	xorg-driver-video
Obsoletes:	X11-driver-fbdev < 1:7.0.0
Obsoletes:	XFree86-FBDev < 4
Obsoletes:	XFree86-driver-fbdev < 1:7.0.0
Obsoletes:	xorg-xserver-Xfbdev < 1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for framebuffer device.

%description -l pl.UTF-8
Sterownik obrazu X.org dla framebuffera.

%prep
%setup -q -n xf86-video-fbdev-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/fbdev_drv.so
%{_mandir}/man4/fbdev.4*
