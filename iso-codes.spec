#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iso-codes
Version  : 4.7.0
Release  : 25
URL      : https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/iso-codes-4.7.0/iso-codes-iso-codes-4.7.0.tar.gz
Source0  : https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/iso-codes-4.7.0/iso-codes-iso-codes-4.7.0.tar.gz
Summary  : ISO country, language, script and currency codes and translations
Group    : Development/Tools
License  : LGPL-2.1
Requires: iso-codes-data = %{version}-%{release}
Requires: iso-codes-license = %{version}-%{release}
Requires: iso-codes-locales = %{version}-%{release}
BuildRequires : python3-dev

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
%setup -q -n iso-codes-iso-codes-4.7.0
cd %{_builddir}/iso-codes-iso-codes-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629931740
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1629931740
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iso-codes
cp %{_builddir}/iso-codes-iso-codes-4.7.0/COPYING %{buildroot}/usr/share/package-licenses/iso-codes/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang iso_3166-1
%find_lang iso_3166
%find_lang iso_3166-3
%find_lang iso_639-2
%find_lang iso_639-3
%find_lang iso_639
%find_lang iso_639_3
%find_lang iso_15924
%find_lang iso_4217
%find_lang iso_3166-2
%find_lang iso_3166_2
%find_lang iso_639-5
%find_lang iso_639_5

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

%files locales -f iso_3166-1.lang -f iso_3166.lang -f iso_3166-3.lang -f iso_639-2.lang -f iso_639-3.lang -f iso_639.lang -f iso_639_3.lang -f iso_15924.lang -f iso_4217.lang -f iso_3166-2.lang -f iso_3166_2.lang -f iso_639-5.lang -f iso_639_5.lang
%defattr(-,root,root,-)

