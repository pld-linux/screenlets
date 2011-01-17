Summary:	Small applications that are similar to OS X's widgets on the Dashboard
Summary(pl.UTF-8):	Małe aplikacje podobne do widgetów na Dashboardzie w OS X
Name:		screenlets
Version:	0.1.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	https://code.launchpad.net/screenlets/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	8bab8052ff5555481fdbe8a5a6310706
URL:		http://www.screenlets.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
Requires(post,postun):	desktop-file-utils
Requires:	python-gnome-desktop-keyring
Requires:	python-gnome-desktop-libwnck
Requires:	python-pyxdg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small applications that are similar to OS X's widgets on the
Dashboard.

%description -l pl.UTF-8
Małe aplikacje podobne do widgetów na Dashboardzie w OS X.

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--prefix %{_prefix}

# screenlets and screenlets-manager
%find_lang %{name} --all-name

%py_postclean %{py_sitescriptdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/screenlets
%attr(755,root,root) %{_bindir}/screenlets-daemon
%attr(755,root,root) %{_bindir}/screenlets-manager
%attr(755,root,root) %{_bindir}/screenlets-packager
%attr(755,root,root) %{_bindir}/screenletsd
%{_desktopdir}/screenlets-manager.desktop
%{_iconsdir}/screenlets.svg
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-*.egg-info
%{_datadir}/screenlets
%dir %{_datadir}/screenlets-manager
%attr(755,root,root) %{_datadir}/screenlets-manager/*.py
%{_datadir}/screenlets-manager/*.png
%{_datadir}/screenlets-manager/*.svg
%{_datadir}/screenlets-manager/prefs.js
