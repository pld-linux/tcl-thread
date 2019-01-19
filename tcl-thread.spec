Summary:	Tcl Thread - extension to gain script-level access to Tcl threading capabilities
Summary(pl.UTF-8):	Tcl Thread - rozszerzenie pozwalające na dostęp do wątków Tcl-a z poziomu skryptów
Name:		tcl-thread
Version:	2.8.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://downloads.sourceforge.net/tcl/thread%{version}.tar.gz
# Source0-md5:	892525df65487985ac85415639909026
URL:		http://tcl.sourceforge.net/
BuildRequires:	tcl-devel >= 8.4
Requires:	tcl >= 8.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl Thread extension can be used to gain script-level access to Tcl
threading capabilities.

%description -l pl.UTF-8
Rozszerzenie Tcl Thread pozwala na dostęp do możliwości wątkowania
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
%doc ChangeLog README license.terms
%dir %{_libdir}/thread%{version}
%attr(755,root,root) %{_libdir}/thread%{version}/libthread*.so
%{_libdir}/thread%{version}/*.tcl
%{_includedir}/tclThread.h
%{_mandir}/mann/thread.n*
%{_mandir}/mann/tpool.n*
%{_mandir}/mann/tsv.n*
%{_mandir}/mann/ttrace.n*
