%define base_name	kde-icons
%define theme_name	lush
%define version		0.1.0
%define name		%{base_name}-%{theme_name}
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lush icons for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{theme_name}-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=5483
Requires:	kdebase-progs
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Provides:	kdemoreartwork-%{theme_name}
Obsoletes:	kdemoreartwork-%{theme_name}

%description
Lush Icon set for KDE Desktop

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{theme_name}

%build
find -type f -exec chmod 644 {} \;

%install
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}
cp -r 16x16/ 22x22/ 32x32/ 48x48/ 64x64/ 128x128/ index.desktop $RPM_BUILD_ROOT/%{_datadir}/icons/%{theme_name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc author copying readme 
%{_iconsdir}/%{theme_name}-%{version}/*

