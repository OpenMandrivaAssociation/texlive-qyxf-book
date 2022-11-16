Name:		texlive-qyxf-book
Version:	56319
Release:	1
Summary:	Book Template for Qian Yuan Xue Fu
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qyxf-book
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qyxf-book.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qyxf-book.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
qyxf-book is a LaTeX document class (template) developed by
Qian Yuan Xue Fu (QYXF), a student club of Xi'an Jiaotong
University (XJTU). Up to now, this template has been applied to
academic counselling material ("course helpers") written by
members of QYXF, including Solutions to University Physics:
https://qyxf.site/latest/Da Wu Ti Jie (Shang ).pdf Notes on
Computing Methods: https://qyxf.site/latest/Ji Suan Fang Fa Xie
Ying -v1.1.pdf Guide to Computer Programming:
https://qyxf.site/latest/Ji Suan Ji She Ji Cheng Xu Zhi Nan
.pdf Features of the template: Minimalistic document style, as
preferred for "course helpers". Several color schemes are
offered, and it is easy to customize your own scheme. Simple
interfaces for users to customize the style of preface, main
part and so on. Currently the template is only designed for
Chinese typesetting.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/qyxf-book
%doc %{_texmfdistdir}/doc/latex/qyxf-book

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
