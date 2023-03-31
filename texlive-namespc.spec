Name:		texlive-namespc
Version:	15878
Release:	2
Summary:	Rudimentary c++-like namespaces in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/namespc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The namespc package adds rudimentary c++-like namespace
functionality to LaTeX. It may be used to declare local LaTeX
commands, which can be made accessible in a later contexts
without defining them globally.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
