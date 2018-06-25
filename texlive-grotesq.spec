Name:		texlive-grotesq
Version:	20180303
Release:	1
Summary:	URW Grotesq font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/grotesq
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grotesq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/grotesq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The directory contains a copy of the Type 1 font "URW Grotesq
2031 Bold' released under the GPL by URW, with supporting files
for use with (La)TeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/urw/grotesq
%{_texmfdistdir}/fonts/map/dvips/grotesq
%{_texmfdistdir}/fonts/tfm/urw/grotesq
%{_texmfdistdir}/fonts/type1/urw/grotesq
%{_texmfdistdir}/fonts/vf/urw/grotesq
%{_texmfdistdir}/tex/latex/grotesq
%doc %{_texmfdistdir}/doc/fonts/grotesq

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
