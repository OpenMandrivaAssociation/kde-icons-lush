%define base_name	kde-icons
%define theme_name	lush
%define version		0.1.0
%define name		%{base_name}-%{theme_name}
%define release %mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lush icons for KDE Desktop
License:	GPL
Group:		Graphical desktop/KDE
Source:		%{theme_name}-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=5483
Requires:	kdebase3-progs
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.0-8mdv2011.0
+ Revision: 619899
- the mass rebuild of 2010.0 packages

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.1.0-7mdv2010.0
+ Revision: 438081
- rebuild

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.0-6mdv2009.1
+ Revision: 360335
- Fix Requires

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-5mdv2009.0
+ Revision: 247621
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.0-3mdv2008.1
+ Revision: 107279
- Fix Requires (kdebase-progs is a better require)
- import kde-icons-lush


* Tue Jul 11 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.1.0-3mdv2007.0
- Rebuild for new extension
- use mkrel

* Mon Apr 19 2004 Laurent Culioli <laurent@mandrake.org> 0.1.0-2mdk
- make rpmlint happy with perms
- new naming scheme

* Wed Aug 27 2003 Laurent Culioli <laurent@pschit.net> 0.1.0-1mdk
- initial package

