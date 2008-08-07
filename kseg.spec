Summary:	KSEG is a free interactive geometry system
Summary(hu.UTF-8):	KSEG egy ingyenes, interaktív geometriai rendszer
Summary(pl.UTF-8):	KSEG jest darmowym interaktywnym systemem geometrycznym
Name:		kseg
Version:	0.403
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.mit.edu/~ibaran/%{name}-%{version}.tar.gz
# Source0-md5:	5474516091e5c4206179cfa03bb7c263
Source1:	%{name}.desktop
Patch0:		%{name}-emptyConstructionList.patch
URL:		http://www.mit.edu/~ibaran/kseg.html
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSEG allows you to interactively create a geometrical construction,
similar to what you can do with a straight edge and compass. Points
may be inserted on the page with right mouse-button clicks, and then
used to form segments, lines, circles, or other geometrical objects.
At any time you can drag existing points around, and watch how the
constructed objects respond.

%description -l hu.UTF-8
KSEG egy program, amellyel interaktívan készíthetsz geometriai
ábrékat, hasonlóan, ahogy a valóságban is tennéd. Pontokat rakhatsz le
a lapra az egér jobb gombjával, és ezeket használhatod fel szakaszok,
vonalaok, körök, vagy bármely más geometriai objektumokhoz. Bármikor
mozgathatod a lerakott pontokat, és láthatod, hogy a készített
objektumok hogyan változnak.

%description -l pl.UTF-8
KSEG pozwala na interaktywne tworzenie konstrukcji geometrycznych,
podobnie jak możesz robić z brzegami. Punkty mogą być wstawiane na
stronie przez kliknięcie prawym przyciskiem, a potem używane do
tworzenia segmentów, linii, okręgów i innych geometrycznych obiektów.
W dowolnym momencie możesz przenosić istniejące punkty i oglądać jak
wygląda zmieniany obiekt.

%prep
%setup -q -n %{name}

%patch0 -p1

%build
qmake
%{__make} \
	QTDIR=%{_prefix} \
	CCFLAGS="%{rpmcflags} -c -fno-rtti -fno-exceptions" \
	CC="%{__cxx}" \
	QTINCLUDE="-I/usr/include/qt"

%install
rm -rf $RPM_BUILD_ROOT
install -D kseg $RPM_BUILD_ROOT%{_bindir}/kseg

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* AUTHORS*
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
%{_desktopdir}/kseg.desktop
