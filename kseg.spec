Summary:	KSEG is a free interactive geometry system
Summary(pl):	KSEG jest darmowym interaktywnym systemem geometrycznym
Name:		kseg
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.mit.edu/~ibaran/%{name}-%{version}.tar.gz
Patch0:		%{name}-DEBIAN.patch
URL:		http://www.mit.edu/~ibaran/kseg.html
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
KSEG allows you to interactively create a geometrical construction,
similar to what you can do with a straight edge and compass. Points
may be inserted on the page with right mouse-button clicks, and then
used to form segments, lines, circles, or other geometrical objects.
At any time you can drag existing points around, and watch how the
constructed objects respond.

%description -l pl
KSEG pozwala na interaktywne tworzenie konstrukcji geometrycznych,
podobnie jak mo¿esz robiæ z brzegami. Punkty moga byæ wstawiane na
stronie przez klikniêcie prawym przyciskiem, a potem u¿ywane do
tworzenia segmentów, lini, okrêgów i innych geometrycznych obiektów. W
dowolnym momencie mo¿esz przenosiæ istniej±ce punkty i ogl±daæ jak
wygl±da zmianiany obiekt.

%prep
%setup -q
%patch0 -p1

%build
%{__make} QTDIR=%{_prefix}/ CCFLAGS="%{rpmcflags} -c -fno-rtti -fno-exceptions -L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -D kseg $RPM_BUILD_ROOT/%{_bindir}/kseg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* AUTHORS* ChangeLog*
%attr(755,root,root) %{_bindir}/*
