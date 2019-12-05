#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : defusedxml
Version  : 0.6.0
Release  : 19
URL      : https://github.com/tiran/defusedxml/archive/v0.6.0/defusedxml-0.6.0.tar.gz
Source0  : https://github.com/tiran/defusedxml/archive/v0.6.0/defusedxml-0.6.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Python-2.0
Requires: defusedxml-license = %{version}-%{release}
Requires: defusedxml-python = %{version}-%{release}
Requires: defusedxml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
# defusedxml -- defusing XML bombs and other exploits
[![Latest
Version](https://img.shields.io/pypi/v/defusedxml.svg)](https://pypi.org/project/defusedxml/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/defusedxml.svg)](https://pypi.org/project/defusedxml/)
[![Travis
CI](https://travis-ci.org/tiran/defusedxml.svg?branch=master)](https://travis-ci.org/tiran/defusedxml)
[![codecov](https://codecov.io/github/tiran/defusedxml/coverage.svg?branch=master)](https://codecov.io/github/tiran/defusedxml?branch=master)
[![PyPI
downloads](https://img.shields.io/pypi/dm/defusedxml.svg)](https://pypistats.org/packages/defusedxml)
[![Code style:
black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the defusedxml package.
Group: Default

%description license
license components for the defusedxml package.


%package python
Summary: python components for the defusedxml package.
Group: Default
Requires: defusedxml-python3 = %{version}-%{release}

%description python
python components for the defusedxml package.


%package python3
Summary: python3 components for the defusedxml package.
Group: Default
Requires: python3-core

%description python3
python3 components for the defusedxml package.


%prep
%setup -q -n defusedxml-0.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557084225
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/defusedxml
cp LICENSE %{buildroot}/usr/share/package-licenses/defusedxml/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/defusedxml/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
