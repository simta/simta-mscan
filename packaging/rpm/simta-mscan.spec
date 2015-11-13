Summary: A simple modular filter script for simta
Name: simta-mscan
Version: 1.4
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: https://github.com/simta
Source0: https://github.com/simta/simta-mscan/releases/download/%{version}/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: dash >= 0.5
BuildRequires: setup

%description
simta-mscan is used to filter incoming mail

%prep
%setup

%install
install -m 755 -d %{buildroot}%{_sbindir} %{buildroot}%{_sysconfdir}/mail/filters
install -m 755 simta-mscan %{buildroot}%{_sbindir}/simta-mscan

%files
%defattr(-,root,root,-)
%{_sysconfdir}/mail/filters
%{_sbindir}/simta-mscan

%changelog
* %(date "+%a %b %d %Y") (Automated RPM build) - %{version}-%{release}
- See git log for actual changes.
