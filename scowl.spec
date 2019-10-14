#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scowl
Version  : 2019.10.06
Release  : 2
URL      : https://sourceforge.net/projects/wordlist/files/SCOWL/2019.10.06/scowl-2019.10.06.tar.gz
Source0  : https://sourceforge.net/projects/wordlist/files/SCOWL/2019.10.06/scowl-2019.10.06.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: scowl-data = %{version}-%{release}
Requires: scowl-license = %{version}-%{release}
Patch1: 0001-Fix-makefile.patch

%description
Spell Checking Oriented Word Lists (SCOWL)
Version 2019.10.06
Sun Oct 6 20:44:03 2019 -0400 [755d6dd]
by Kevin Atkinson (kevina@gnu.org)

%package data
Summary: data components for the scowl package.
Group: Data

%description data
data components for the scowl package.


%package license
Summary: license components for the scowl package.
Group: Default

%description license
license components for the scowl package.


%prep
%setup -q -n scowl-2019.10.06
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571068297
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1571068297
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scowl
cp %{_builddir}/scowl-2019.10.06/r/yawl/LICENSE %{buildroot}/usr/share/package-licenses/scowl/ce9e0928d4e7f35ab599f7f40c7d382eeeef4a18
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dict/words

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scowl/ce9e0928d4e7f35ab599f7f40c7d382eeeef4a18
