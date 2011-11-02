Name:		texlive-namespc
Version:	20061222
Release:	1
Summary:	Rudimentary c++-like namespaces in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/namespc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The namespc package adds rudimentary c++-like namespace
functionality to LaTeX. It may be used to declare local LaTeX
commands, which can be made accessible in a later contexts
without defining them globally.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/namespc/namespc.sty
%doc %{_texmfdistdir}/doc/latex/namespc/README
%doc %{_texmfdistdir}/doc/latex/namespc/namespc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/namespc/namespc.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
