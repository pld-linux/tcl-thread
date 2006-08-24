Summary:	Tcl Thread - extension to gain script-level access to Tcl threading capabilities
Summary(pl):	Tcl Thread - rozszerzenie pozwalaj±ce na dostêp do w±tków Tcl-a z poziomu skryptów
Name:		tcl-thread
Version:	2.6.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sourceforge.net/tcl/thread%{version}.tar.gz
# Source0-md5:	ca4c4175e0dee8153b940ed4e0dc07bd
URL:		http://tcl.sourceforge.net/
BuildRequires:	tcl-devel >= 8.4
Requires:	tcl >= 8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl Thread extension can be used to gain script-level access to Tcl
threading capabilities.

%description -l pl
Rozszerzenie Tcl Thread pozwala na dostêp do mo¿liwo¶ci w±tkowania
Tcl-a z poziomu skryptów.

%prep
%setup -q -n thread%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/thread%{version}
%attr(755,root,root) %{_libdir}/thread%{version}/libthread*.so
%{_libdir}/thread%{version}/*.tcl
%{_mandir}/mann/*.n*
