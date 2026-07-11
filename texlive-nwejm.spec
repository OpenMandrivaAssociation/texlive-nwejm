%global tl_name nwejm
%global tl_revision 77980

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Support for the journal North-Western European Journal of Mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nwejm
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nwejm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle includes LaTeX classes and BibLaTeX styles files dedicated to
the new journal "North-Western European Journal of Mathematics": nwejm
for the complete issues of the journal, aimed at the NWEJM's team,
nwejmart, intended for the authors who wish to publish an article in the
NWEJM. This class's goal is to: faithfully reproduce the layout of the
nwejm, thus enabling the authors to be able to work their document in
actual conditions, provide a number of tools (commands and environments)
to facilitate the drafting of documents, in particular those containing
mathematical formulas.

