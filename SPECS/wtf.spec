%define debug_package %{nil}

%global gh_user     wtfutil
%global gh_name     wtf
%global gh_commit   2b19ccea1ca96a222fa6ef49f23b2763d325dc39
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

Name:           wtfutil
Version:        0.17.0
Release:        1%{?dist}
Summary:        A personal terminal-based dashboard utility, designed for displaying infrequently-needed, but very important, daily data.
Group:          Applications/System
License:        GNU
URL:            https://github.com/wtfutil/wtf
BuildRequires:  golang

%description
WTF is a personal information dashboard for your terminal, developed for those who spend
most of their day in the command line. It allows you to monitor systems, services, and
important information that you otherwise might keep browser tabs open for, the kinds of
things you don’t always need visible, but do check in on every now and then. Keep an eye
on your OpsGenie schedules, Google Calendar, Git and GitHub repositories, and New Relic
deployments. See who’s away in BambooHR, which Jira tickets are assigned to you, and what
time it is in Barcelona. It even has weather. And clocks. And emoji.

%prep
wget https://github.com/%{gh_user}/%{gh_name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
mv %{_builddir}/%{gh_name}-%{version} %{gh_name}
mkdir -p %{_builddir}/%{gh_name}-%{version}
cd %{gh_name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{gh_name}
make

%install
install -Dm0755 %{_builddir}/src/github.com/%{gh_user}/%{gh_name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Jul 16 2019 Jamie Curnow <jc@jc21.com> 0.17.0-1
- v0.17.0

* Mon Jul 15 2019 Jamie Curnow <jc@jc21.com> 0.16.1-1
- v0.16.1

* Fri Jul 12 2019 Jamie Curnow <jc@jc21.com> 0.16.0-1
- v0.16.0

* Thu Jul 11 2019 Jamie Curnow <jc@jc21.com> 0.15.0-1
- v0.15.0

* Wed Jul 10 2019 Jamie Curnow <jc@jc21.com> 0.14.0-1
- v0.14.0

* Thu Jun 27 2019 Jamie Curnow <jc@jc21.com> 0.13.0-1
- v0.13.0

* Mon Jun 24 2019 Jamie Curnow <jc@jc21.com> 0.12.0-1
- v0.12.0

* Fri Jun 7 2019 Jamie Curnow <jc@jc21.com> 0.11.0-1
- v0.11.0

* Mon May 20 2019 Jamie Curnow <jc@jc21.com> 0.10.3-1
- v0.10.3

* Mon May 20 2019 Jamie Curnow <jc@jc21.com> 0.10.2-1
- v0.10.2

* Thu May 16 2019 Jamie Curnow <jc@jc21.com> 0.10.1-1
- v0.10.1

* Tue May 14 2019 Jamie Curnow <jc@jc21.com> 0.10.0-1
- v0.10.0

* Fri May 10 2019 Jamie Curnow <jc@jc21.com> 0.9.2-1
- v0.9.2

* Tue May 7 2019 Jamie Curnow <jc@jc21.com> 0.9.1-1
- v0.9.1

* Tue Apr 30 2019 Jamie Curnow <jc@jc21.com> 0.8.0-1
- v0.8.0

* Wed Apr 24 2019 Jamie Curnow <jc@jc21.com> 0.7.1-1
- v0.7.1

* Tue Apr 23 2019 Jamie Curnow <jc@jc21.com> 0.7.0-1
- v0.7.0

* Thu Feb 28 2019 Jamie Curnow <jc@jc21.com> 0.5.0-1
- Initial spec

