%global tl_name grotesq
%global tl_revision 35859

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	URW Grotesq font pack for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/grotesq
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grotesq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/grotesq.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The directory contains a copy of the Type 1 font "URW Grotesq 2031 Bold'
released under the GPL by URW, with supporting files for use with
(La)TeX.

