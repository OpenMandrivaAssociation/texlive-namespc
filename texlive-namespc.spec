%global tl_name namespc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Rudimentary C++-like namespaces in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/namespc
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The namespc package adds rudimentary C++-like namespace functionality to
LaTeX. It may be used to declare local LaTeX commands, which can be made
accessible in a later contexts without defining them globally.

