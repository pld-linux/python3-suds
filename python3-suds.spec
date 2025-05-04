#
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Python 2 SOAP client library
Summary(pl.UTF-8):	Biblioteka klienta SOAP dla Pythona 2
Name:		python3-suds
Version:	1.2.0
Release:	1
License:	LGPL v3+
Group:		Development/Languages/Python
#Source0Download: https://github.com/suds-community/suds/releases
Source0:	https://github.com/suds-community/suds/archive/v%{version}/suds-%{version}.tar.gz
# Source0-md5:	202af9679d27986db550d922112db170
URL:		https://github.com/suds-community/suds
BuildRequires:	python3-devel >= 1:3.2
%{?with_tests:BuildRequires:	python3-pytest}
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Suds is a lightweight SOAP Python client for consuming Web Services.

%description -l pl.UTF-8
Suds to lekka implementacja klienta SOAP dla języka Python.

%prep
%setup -q -n suds-%{version}

%build
topdir=$(pwd)
%py3_build

cd build-3
PYTHONPATH=$(pwd)/lib \
%{__python3} -m pytest ../tests

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md TODO.txt
%{py3_sitescriptdir}/suds
%{py3_sitescriptdir}/suds_community-%{version}-py*.egg-info
