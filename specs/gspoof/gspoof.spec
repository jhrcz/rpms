# $Id$
# Authority: dag
# Upstream: Embyte <embyte@madlab.it>

Summary: Network tool to build and send TCP/IP packets
Name: gspoof
Version: 3.2
Release: 0
License: GPL
Group: Applications/Internet
URL: http://gspoof.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gspoof/gspoof-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet-devel >= 1.1.0

%description
Gspoof is a tool which make easier and accurate the building and sending
of TCP/IP packets. It works from console (command line) and has an
interface graphics written in GTK+ too.

%prep
%setup

%{__cat} <<EOF >gspoof.desktop
[Desktop Entry]
Name=Gspoof
Comment=Build and send crafted TCP/IP packets
Icon=gspoof.png
Exec=gspoof
Terminal=false
Type=Application
Categories=GNOME;Application;Network;
StartupNotify=true
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 3.1-0
- Initial package. (using DAR)
