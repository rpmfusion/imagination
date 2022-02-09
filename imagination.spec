Name:           imagination          
Version:        3.6
Release:        4%{?dist}
Summary:        A lightweight and simple GTK based DVD slide show creator

Group:          Applications/Multimedia
License:        GPLv2
URL:            http://imagination.sourceforge.net/
Source0:        https://downloads.sourceforge.net/imagination/%{name}-%{version}.tar.gz

Patch0:         imagination-3.0-docfix.patch
# Fix icon references to not require gnome-icon-theme-legacy
Patch1:         imagination-3.0-icon_fix.patch

BuildRequires:  gtk3-devel
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
%patch0 -b .docfix
%patch1 -p1 -b .iconfix


%build
# Necessary due to patched configure.in
./autogen.sh
LDFLAGS=`pkg-config --libs gmodule-2.0`; export LDFLAGS
%configure
%make_build


%install
%make_install

# Move documentation so it will go in the right directory
rm -rf $(pwd)/_tmpdoc && mkdir $(pwd)/_tmpdoc
mv -f %{buildroot}%{_docdir}/%{name}/html $(pwd)/_tmpdoc/

# Remove unnecessary library files
rm %{buildroot}%{_libdir}/%{name}/*.la

%find_lang %{name}

desktop-file-validate %{buildroot}/%{_datadir}/applications/imagination.desktop


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
* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Sérgio Basto <sergio@serjux.com> - 3.6-1
- Update imagination to 3.6

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Sergio - 3.5.1-1
- Update imagination to 3.5.1

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 15 2018 Richard Shaw <hobbes1069@gmail.com> - 3.1-1
- Update to 3.1.

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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
