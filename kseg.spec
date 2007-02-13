# TODO: 
#	- kill _applnkdir
#	- fix build
Summary:	KSEG is a free interactive geometry system
Summary(pl.UTF-8):	KSEG jest darmowym interaktywnym systemem geometrycznym
Name:		kseg
Version:	0.3
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.mit.edu/~ibaran/%{name}-%{version}.tar.gz
# Source0-md5:	b7302130aa57f0707402340cbf0c7070
Source1:	%{name}.desktop
Patch0:		%{name}-DEBIAN.patch
Patch1:		%{name}-qt_headers.patch
URL:		http://www.mit.edu/~ibaran/kseg.html
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSEG allows you to interactively create a geometrical construction,
similar to what you can do with a straight edge and compass. Points
may be inserted on the page with right mouse-button clicks, and then
used to form segments, lines, circles, or other geometrical objects.
At any time you can drag existing points around, and watch how the
constructed objects respond.

%description -l pl.UTF-8
KSEG pozwala na interaktywne tworzenie konstrukcji geometrycznych,
podobnie jak możesz robić z brzegami. Punkty mogą być wstawiane na
stronie przez kliknięcie prawym przyciskiem, a potem używane do
tworzenia segmentów, linii, okręgów i innych geometrycznych obiektów. W
dowolnym momencie możesz przenosić istniejące punkty i oglądać jak
wygląda zmieniany obiekt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	QTDIR=%{_prefix}/ \
	CCFLAGS="%{rpmcflags} -c -fno-rtti -fno-exceptions" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -D kseg $RPM_BUILD_ROOT{%{_bindir}/kseg,%{_applnkdir}/Scientific/Mathematics}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Mathematics/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* AUTHORS* ChangeLog*
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/Mathematics/*
