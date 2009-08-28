Summary:	Recover data from any device with bad sectors
Name:		dd_rhelp
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.kalysto.org/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	689e24f64e99a471c89eb3d7958f7530
URL:		http://www.kalysto.org/utilities/dd_rhelp/index.en.html
Requires:	ddrescue
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dd_rhelp allows users to retrieve, quickly and easily, recoverable
data from any device with bad sectors. It will copy it using dd_rescue
in all the appropriate ways (reverse copy, setting start and stop
offset accordingly to previously rescued data) to recover the maximum
data possible before spending time on bad sectors. It is
straightforward to use, supports ctrl-c at anytime, can resume a job
(or standalone dd_rescue job) by parsing the dd_rescue logs, and
displays a nice ASCII bar showing rescue progress.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install dd_rhelp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README* THANKS TODO doc/example.txt
%attr(755,root,root) %{_bindir}/dd_rhelp
