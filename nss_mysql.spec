Summary:	MySQL Name Service Switch Module
Summary(pl):	Modu³ NSS MySQL
Name:		nss_mysql
Version:	0.43
Release:	4
License:	GPL
Group:		Base
Source0:	http://savannah.nongnu.org/download/nss-mysql/nss-mysql.pkg/%{version}/nss-mysql-%{version}.tar.gz
# Source0-md5:	1b3e62509dec0904142a06c58e9b9473
Patch0:		%{name}-m4.patch
URL:		http://www.freesoftware.fsf.org/nss-mysql/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
NSS MySQL is a NSS library for MySQL. It features full groups, passwd
and shadow support.

%description -l pl
NSS MySQL jest bibliotek± NSS dla MySQL. Pozwala ona na przechowywanie
informacji typowych dla plików groups, passwd oraz shadow w bazie
MySQL.

%prep
%setup -q -n nss-mysql-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?debug:--enable-debug} \
	--enable-group \
	--enable-shadow \
	--with-mysql-lib=/usr/%{_lib} \
	--with-mysql-include=/usr/include/mysql

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README SHADOW THANKS TODO UPGRADE *.sql
%attr(755,root,root) %{_libdir}/*.so*
%attr(600,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/nss*.conf
