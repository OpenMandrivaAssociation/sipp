Summary: 	Performance testing tool for the SIP protocol
Name: 	 	sipp
Version: 	1.0
Release: 	%mkrel 4
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


