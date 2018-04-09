#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : defusedxml
Version  : 0.5.0
Release  : 5
URL      : https://github.com/tiran/defusedxml/archive/v0.5.0.tar.gz
Source0  : https://github.com/tiran/defusedxml/archive/v0.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Python-2.0
Requires: defusedxml-python3
Requires: defusedxml-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
===================================================
defusedxml -- defusing XML bombs and other exploits
===================================================

%package python
Summary: python components for the defusedxml package.
Group: Default
Requires: defusedxml-python3

%description python
python components for the defusedxml package.


%package python3
Summary: python3 components for the defusedxml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the defusedxml package.


%prep
%setup -q -n defusedxml-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523288065
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
