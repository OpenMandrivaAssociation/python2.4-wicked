%define module		wicked
%define name		python2.4-%{module}
%define version		1.1.6
%define release		%mkrel 1
%define __python	%{_bindir}/python2.4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Compact syntax for doing wiki-like content
Group: 		Development/Python
License:	Python license
URL:		http://pypi.python.org/pypi/wicked/1.1.6
Source:		http://pypi.python.org/packages/source/w/wicked/%{module}-%{version}.tar.bz2
Requires:	python2.4
BuildRequires:	python2.4-devel
BuildRequires:	python2.4-setuptools
BuildArch:	noarch

%description
wicked is a compact syntax for doing wiki-like content linking and creation in
zope and plone.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record INSTALLED_FILES


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs/*.txt

