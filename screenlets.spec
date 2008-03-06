Summary:	Small applications that are similar to OS X's widgets on the Dashboard
Summary(pl.UTF-8):	Małe aplikacje podobne do widgetów na Dashboardzie w OS X
Name:		screenlets
Version:	0.0.12
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://code.launchpad.net/screenlets/trunk/0.0.12/+download/%{name}-%{version}.tar.gz
# Source0-md5:	dafcffd3a1441e910d60ebfb227ed189
URL:		http://www.screenlets.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	desktop-file-utils
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--prefix %{_prefix}

%py_postclean %{py_sitescriptdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TODO-0.1.0
%{_bindir}/screenlets-manager
%{_bindir}/screenlets-packager
%{_bindir}/screenletsd
%{_desktopdir}/screenlets-manager.desktop
%{_iconsdir}/screenlets.svg
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info
%{_datadir}/screenlets
%dir %{_datadir}/screenlets-manager
%{_datadir}/screenlets-manager/*.svg
%attr(755,root,root) %{_datadir}/screenlets-manager/*.py
