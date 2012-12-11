Summary: 	Performance testing tool for the SIP protocol
Name: 	 	sipp
Version: 	1.0
Release: 	%mkrel 8
License:	GPL
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sipp.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/sipp/sipp.%{version}.tar.bz2
Source1:	reference.pdf.bz2
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel

%description
SIPp is a performance testing tool for the SIP protocol. It
includes a few basic SipStone user agent scenarios (UAC and UAS)
and establishes and releases multiple calls with the INVITE and
BYE methods. It can also reads XML scenario files describing any
performance testing configuration. It features the dynamic display
of statistics about running tests (call rate, round trip delay,
and message statistics), periodic CSV statistics dumps, TCP and
UDP over multiple sockets or multiplexed with retransmission
management, regular expressions and variables in scenario files,
and dynamically adjustable call rates.

SIPp can be used to test many real SIP equipements like SIP
proxies, B2BUAs, SIP media servers, SIP/x gateways, SIP PBX, 
... It is also very useful to emulate thousands of user agents
calling your SIP system. 

%prep

%setup -q -n %{name}

bzcat %{SOURCE1} > reference.pdf

%build

make \
    CFLAGS="%{optflags}" \
    CPPFLAGS="%{optflags}"

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 sipp %{buildroot}%{_bindir}/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* reference.pdf
%{_bindir}/sipp




%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-8mdv2010.0
+ Revision: 433836
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2009.0
+ Revision: 260696
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-6mdv2009.0
+ Revision: 252464
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-4mdv2008.1
+ Revision: 171107
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-3mdv2008.1
+ Revision: 127287
- kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2007.0
+ Revision: 115959
- Import sipp

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-2mdk
- rebuild

* Thu Oct 21 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0-1mdk
- initial mandrake package

