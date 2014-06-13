# revision 15878
# category Package
# catalog-ctan /fonts/urw/grotesq
# catalog-date 2007-11-03 13:04:21 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-grotesq
Version:	20071103
Release:	7
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
%{_texmfdistdir}/dvips/grotesq/config.ugq
%{_texmfdistdir}/fonts/afm/urw/grotesq/ugqb8a.afm
%{_texmfdistdir}/fonts/map/dvips/grotesq/ugq.map
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8a.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw/grotesq/ugqbo8t.tfm
%{_texmfdistdir}/fonts/type1/urw/grotesq/ugqb8a.pfb
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb7t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb8c.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqb8t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbc7t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbc8t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo7t.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo8c.vf
%{_texmfdistdir}/fonts/vf/urw/grotesq/ugqbo8t.vf
%{_texmfdistdir}/tex/latex/grotesq/ot1ugq.fd
%{_texmfdistdir}/tex/latex/grotesq/t1ugq.fd
%{_texmfdistdir}/tex/latex/grotesq/ts1ugq.fd
%doc %{_texmfdistdir}/doc/fonts/grotesq/grotesq.txt
%doc %{_texmfdistdir}/doc/fonts/grotesq/readme.grotesq

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20071103-2
+ Revision: 752449
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20071103-1
+ Revision: 718587
- texlive-grotesq
- texlive-grotesq
- texlive-grotesq
- texlive-grotesq

