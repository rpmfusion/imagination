Name:           imagination          
Version:        3.0
Release:        15%{?dist}
Summary:        A lightweight and simple GTK based DVD slide show creator

Group:          Applications/Multimedia
License:        GPLv2
URL:            http://imagination.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/imagination/imagination/%{version}/%{name}-%{version}.tar.gz
Patch0:         imagination-3.0-plugins.patch
Patch1:         imagination-3.0-docfix.patch
# Fix icon references to not require gnome-icon-theme-legacy
Patch2:         imagination-3.0-icon_fix.patch
# Fixed in upstream trunk
# http://imagination.svn.sourceforge.net/viewvc/imagination/trunk/configure.in?view=patch&r1=599&r2=598&pathrev=599
Patch3:         imagination-3.0-configure.in.patch

BuildRequires:  gtk2-devel
BuildRequires:  sox-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libxslt docbook-style-xsl
BuildRequires:  intltool
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  libtool

Requires:       ffmpeg
Requires:       hicolor-icon-theme
Requires:       gnome-icon-theme


%description
Imagination is a lightweight and simple DVD slide show maker written in C
language and built with the GTK+2 toolkit.


%prep
%setup -q
autoreconf -fiv
%patch0 -b .plugins
%patch1 -b .docfix
%patch2 -p1 -b .iconfix
%patch3 -p1 -b .conffix


%build
# Necessary due to patched configure.in
/bin/bash ./autogen.sh
LDFLAGS=`pkg-config --libs gmodule-2.0`; export LDFLAGS
%configure
make %{?_smp_mflags} V=1


%install
%make_install

# Move documentation so it will go in the right directory
rm -rf $(pwd)/_tmpdoc && mkdir $(pwd)/_tmpdoc
mv -f %{buildroot}%{_docdir}/%{name}/html $(pwd)/_tmpdoc/

# Remove unnecessary library files
rm %{buildroot}%{_libdir}/%{name}/*.la

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/imagination.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%license COPYING
%doc AUTHORS README _tmpdoc/*
%{_bindir}/imagination
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%{_libdir}/%{name}

%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Richard Shaw <hobbes1069@gmail.com> - 3.0-14
- Fix icon directory ownership.

* Thu Mar 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 3.0-13
- Run autoreconf

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.0-10
- Rebuilt for x264/FFmpeg

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.0-9
- Mass rebuilt for Fedora 19 Features

* Tue May 01 2012 Richard Shaw <hobbes1069@gmail.com> - 3.0-8
- Fix FTBFS.

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun May  1 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-6
- Fixed minor issues with spec file for packaging compliance.

* Sat Apr 23 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-5
- Added upstream patch to fix building for Fedora 13

* Mon Apr 18 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-4
- Patched to use new icon names instead of requiring a legacy package.

* Mon Apr 18 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-3
- Fixed missing icons thanks to https://bugzilla.rpmfusion.org/show_bug.cgi?id=1617#c3

* Sat Apr 16 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-2
- Updated spec file to correct documentation location.

* Thu Apr 14 2011 Richard Shaw <hobbes1069@gmail.com> - 3.0-1
- Build for initial release.
