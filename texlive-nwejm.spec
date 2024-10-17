Name:		texlive-nwejm
Version:	70597
Release:	1
Summary:	Support for the journal "North-Western European Journal of Mathematics"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nwejm
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle includes LaTeX classes and BibLaTeX styles files
dedicated to the new journal "North-Western European Journal of
Mathematics": nwejm for the complete issues of the journal,
aimed at the NWEJM's team, nwejmart, intended for the authors
who wish to publish an article in the NWEJM. This class's goal
is to: faithfully reproduce the layout of the nwejm, thus
enabling the authors to be able to work their document in
actual conditions, provide a number of tools (commands and
environments) to facilitate the drafting of documents, in
particular those containing mathematical formulas.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nwejm
%{_texmfdistdir}/tex/latex/nwejm
%doc %{_texmfdistdir}/doc/latex/nwejm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
