%global fontname fontawesome
%global fontconf 60-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	4.1.0
Release:	2%{?dist}
Summary:	Iconic font set
License:	OFL
URL:		http://fontawesome.io/
Source0:	http://fontawesome.io/assets/font-awesome-%{version}.zip
Source1:	%{name}-fontconfig.conf
Source2:	README-Trademarks.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	ttembed
Requires:	fontpackages-filesystem


%description
Font Awesome gives you scalable vector icons that can instantly be
customized — size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains OpenType and TrueType font files which are typically used
locally.

%package web
License:	MIT
Requires:	%{fontname}-fonts = %{version}-%{release}
Summary:	Iconic font set, web files

%description web
Font Awesome gives you scalable vector icons that can instantly be
customized — size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format versions 1, Embedded OpenType and SVG font files which are
typically used on the web.

%prep
%setup -q -n font-awesome-%{version}
cp -p %SOURCE2 .

%build
ttembed fonts/*.ttf fonts/*.otf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*.ttf fonts/*.otf fonts/*.woff fonts/*.svg fonts/*.eot %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/font-awesome-web/
cp -a css less scss %{buildroot}%{_datadir}/font-awesome-web/

# files:
%_font_pkg -f %{fontconf} *.ttf *.otf
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%doc README-Trademarks.txt

%files web
%{_datadir}/font-awesome-web/
%{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%changelog
* Tue Jun 19 2018 Petr Vobornik <pvoborni@redhat.com> - 4.1.0-2
- Resolves #1492884: include .svg, .woff, .eot font files in web package

* Fri Sep 12 2014 Petr Vobornik <pvoborni@redhat.com> - 4.1.0-1
- initial RHEL package
