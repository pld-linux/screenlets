Summary:	Small applications that are similar to OS X's widgets on the Dashboard
Summary(pl.UTF-8):	Małe aplikacje podobne do widgetów na Dashboardzie w OS X
Name:		screenlets
Version:	0.0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.ryxperience.com/storage/screenlets-0.0.9.tar.bz2
# Source0-md5:	b8e1246dcdd47b2bfcb57b8db7ad28d7
URL:		http://forum.compiz-fusion.org/showthread.php?t=323
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small applications that are similar to OS X's widgets on the Dashboard.

%description -l pl.UTF-8
Małe aplikacje podobne do widgetów na Dashboardzie w OS X.

%prep
%setup -q

sed -i -e "s@'/usr/local'@'/usr'@g" src/lib/__init__.py setup.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--prefix %{_prefix}

%py_postclean %{py_sitescriptdir}/%{name}

rm $RPM_BUILD_ROOT%{_bindir}/screenletsd
rm $RPM_BUILD_ROOT%{_datadir}/screenlets/add-screenlet.py
rm $RPM_BUILD_ROOT%{_datadir}/screenlets/screenletsd.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO TODO-0.1.0
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info
%{_datadir}/screenlets
