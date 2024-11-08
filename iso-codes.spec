#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v19
# autospec commit: f35655a
#
Name     : iso-codes
Version  : 4.17.0
Release  : 36
URL      : https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/v4.17.0/iso-codes-v4.17.0.tar.gz
Source0  : https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/v4.17.0/iso-codes-v4.17.0.tar.gz
Summary  : ISO country, language, script and currency codes and translations
Group    : Development/Tools
License  : LGPL-2.1
Requires: iso-codes-data = %{version}-%{release}
Requires: iso-codes-license = %{version}-%{release}
Requires: iso-codes-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : python3-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# iso-codes
https://salsa.debian.org/iso-codes-team/iso-codes
This project provides lists of various ISO standards (e.g. country,
language, language scripts, and currency names) in one place, rather
than repeated in many programs throughout the system.

%package data
Summary: data components for the iso-codes package.
Group: Data

%description data
data components for the iso-codes package.


%package dev
Summary: dev components for the iso-codes package.
Group: Development
Requires: iso-codes-data = %{version}-%{release}
Provides: iso-codes-devel = %{version}-%{release}
Requires: iso-codes = %{version}-%{release}

%description dev
dev components for the iso-codes package.


%package license
Summary: license components for the iso-codes package.
Group: Default

%description license
license components for the iso-codes package.


%package locales
Summary: locales components for the iso-codes package.
Group: Default

%description locales
locales components for the iso-codes package.


%prep
%setup -q -n iso-codes-v4.17.0
cd %{_builddir}/iso-codes-v4.17.0
pushd ..
cp -a iso-codes-v4.17.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726278487
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726278487
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iso-codes
cp %{_builddir}/iso-codes-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/iso-codes/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang iso_3166-1
%find_lang iso_3166
%find_lang iso_639-5
%find_lang iso_639_5
%find_lang iso_3166-3
%find_lang iso_639-2
%find_lang iso_639-3
%find_lang iso_639
%find_lang iso_639_3
%find_lang iso_15924
%find_lang iso_4217
%find_lang iso_3166-2
%find_lang iso_3166_2
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/iso-codes/json/iso_15924.json
/usr/share/iso-codes/json/iso_3166-1.json
/usr/share/iso-codes/json/iso_3166-2.json
/usr/share/iso-codes/json/iso_3166-3.json
/usr/share/iso-codes/json/iso_4217.json
/usr/share/iso-codes/json/iso_639-2.json
/usr/share/iso-codes/json/iso_639-3.json
/usr/share/iso-codes/json/iso_639-5.json
/usr/share/iso-codes/json/schema-15924.json
/usr/share/iso-codes/json/schema-3166-1.json
/usr/share/iso-codes/json/schema-3166-2.json
/usr/share/iso-codes/json/schema-3166-3.json
/usr/share/iso-codes/json/schema-4217.json
/usr/share/iso-codes/json/schema-639-2.json
/usr/share/iso-codes/json/schema-639-3.json
/usr/share/iso-codes/json/schema-639-5.json
/usr/share/xml/iso-codes/iso_15924.xml
/usr/share/xml/iso-codes/iso_3166-1.xml
/usr/share/xml/iso-codes/iso_3166-2.xml
/usr/share/xml/iso-codes/iso_3166-3.xml
/usr/share/xml/iso-codes/iso_3166.xml
/usr/share/xml/iso-codes/iso_3166_2.xml
/usr/share/xml/iso-codes/iso_4217.xml
/usr/share/xml/iso-codes/iso_639-2.xml
/usr/share/xml/iso-codes/iso_639-3.xml
/usr/share/xml/iso-codes/iso_639-5.xml
/usr/share/xml/iso-codes/iso_639.xml
/usr/share/xml/iso-codes/iso_639_3.xml
/usr/share/xml/iso-codes/iso_639_5.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/iso-codes.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iso-codes/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f iso_3166-1.lang -f iso_3166.lang -f iso_639-5.lang -f iso_639_5.lang -f iso_3166-3.lang -f iso_639-2.lang -f iso_639-3.lang -f iso_639.lang -f iso_639_3.lang -f iso_15924.lang -f iso_4217.lang -f iso_3166-2.lang -f iso_3166_2.lang
%defattr(-,root,root,-)

