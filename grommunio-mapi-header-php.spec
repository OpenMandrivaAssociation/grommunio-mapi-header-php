Name:		grommunio-mapi-header-php
Version:	2.1
Release:	1
Source0:	https://github.com/grommunio/mapi-header-php/releases/download/%{version}/mapi-header-php-%{version}.tar.zst
Summary:	grommunio MAPI headers (PHP)
URL:		https://github.com/grommunio/mapi-header-php
License:	AGPL-3.0
Group:		Servers
BuildArch:	noarch
Requires:	php
Requires:	php-gromox

%description
mapi-headers-php is the central repository for PHP-based MAPI applications.
These header files are used by grommunio Web, grommunio Sync and grommunio
DAV, eliminating the bundling of headers.

%prep
%autosetup -p1 -n mapi-header-php-%{version}

%conf

%build

%install
%make_install

%files
%{_datadir}/php-mapi
