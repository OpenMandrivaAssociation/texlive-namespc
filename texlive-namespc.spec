# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/namespc
# catalog-date 2006-12-22 14:37:19 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-namespc
Version:	20061222
Release:	9
Summary:	Rudimentary c++-like namespaces in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/namespc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/namespc.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061222-2
+ Revision: 754246
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061222-1
+ Revision: 719099
- texlive-namespc
- texlive-namespc
- texlive-namespc
- texlive-namespc

