%define upstream_version 15.1.0
Name:           python3-constantly
Version:        %{upstream_version}
Release:        0
Summary:        A library that provides symbolic constant support
License:        MIT
URL:            https://github.com/sailfishos/python-constantly
Source0:        %{name}-%{version}.tar.gz
Source1:        _version.py
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed

%description
%{summary}. It includes collections and constants with text, numeric,
and bit flag values. Originally twisted.python.constants from the
Twisted project.

%prep
%autosetup -n %{name}-%{version}/upstream
# Remove bundled egg-info
rm -rf constantly.egg-info
# Patch correct version number
cp %{SOURCE1} constantly/_version.py
sed '/"version"/s/: ".*"/: "%{upstream_version}"/' -i constantly/_version.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/constantly
%{python3_sitelib}/constantly-%{upstream_version}-py%{python3_version}.egg-info/
