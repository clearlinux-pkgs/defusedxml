#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : defusedxml
Version  : 0.7.1
Release  : 34
URL      : https://github.com/tiran/defusedxml/archive/v0.7.1/defusedxml-0.7.1.tar.gz
Source0  : https://github.com/tiran/defusedxml/archive/v0.7.1/defusedxml-0.7.1.tar.gz
Summary  : XML bomb protection for Python stdlib modules
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
===================================================
defusedxml -- defusing XML bombs and other exploits
===================================================

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
Provides: pypi(defusedxml)

%description python3
python3 components for the defusedxml package.


%prep
%setup -q -n defusedxml-0.7.1
cd %{_builddir}/defusedxml-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615216068
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/defusedxml
cp %{_builddir}/defusedxml-0.7.1/LICENSE %{buildroot}/usr/share/package-licenses/defusedxml/c0a4a8cdd88e9432b6dae397e751cfe61ba6ed88
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/defusedxml/c0a4a8cdd88e9432b6dae397e751cfe61ba6ed88

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
