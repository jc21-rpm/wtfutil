%define debug_package %{nil}

%global gh_user     wtfutil
%global gh_name     wtf
%global gh_commit   48144b1b185887a38457c300d89982aeb430e851
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

Name:           wtfutil
Version:        0.38.0
Release:        1%{?dist}
Summary:        A personal terminal-based dashboard utility, designed for displaying infrequently-needed, but very important, daily data.
Group:          Applications/System
License:        GNU
URL:            https://github.com/wtfutil/wtf
Source:         https://github.com/%{gh_user}/%{gh_name}/archive/v%{version}.tar.gz
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
%setup -q -n wtf-%{version}

%build
make

%install
install -Dm0755 %{_builddir}/bin/wtf %{buildroot}%{_bindir}/wtf

%files
%{_bindir}/%{name}

%changelog
* Tue Jul 13 2021 Jamie Curnow <jc@jc21.com> 0.38.0-1
- v0.38.0

* Mon May 10 2021 Jamie Curnow <jc@jc21.com> 0.37.0-1
- v0.37.0

* Wed Mar 24 2021 Jamie Curnow <jc@jc21.com> 0.36.0-1
- v0.36.0

* Mon Jan 4 2021 Jamie Curnow <jc@jc21.com> 0.35.0-1
- v0.35.0

* Mon Nov 9 2020 Jamie Curnow <jc@jc21.com> 0.34.0-1
- v0.34.0

* Thu Oct 15 2020 Jamie Curnow <jc@jc21.com> 0.33.0-1
- v0.33.0

* Mon Jul 13 2020 Jamie Curnow <jc@jc21.com> 0.31.0-1
- v0.31.0

* Mon May 11 2020 Jamie Curnow <jc@jc21.com> 0.30.0-1
- v0.30.0

* Mon Apr 27 2020 Jamie Curnow <jc@jc21.com> 0.29.0-1
- v0.29.0

* Mon Mar 16 2020 Jamie Curnow <jc@jc21.com> 0.28.0-1
- v0.28.0

* Mon Feb 24 2020 Jamie Curnow <jc@jc21.com> 0.27.0-1
- v0.27.0

* Wed Feb 5 2020 Jamie Curnow <jc@jc21.com> 0.26.0-1
- v0.26.0

* Sat Dec 14 2019 Jamie Curnow <jc@jc21.com> 0.25.0-1
- v0.25.0

* Mon Nov 11 2019 Jamie Curnow <jc@jc21.com> 0.24.0-1
- v0.24.0

* Mon Oct 14 2019 Jamie Curnow <jc@jc21.com> 0.23.0-1
- v0.23.0

* Fri Sep 13 2019 Jamie Curnow <jc@jc21.com> 0.22.0-1
- v0.22.0

* Sun Sep 1 2019 Jamie Curnow <jc@jc21.com> 0.21.0-1
- v0.21.0

* Thu Aug 22 2019 Jamie Curnow <jc@jc21.com> 0.20.0-1
- v0.20.0

* Wed Jul 31 2019 Jamie Curnow <jc@jc21.com> 0.19.1-1
- v0.19.1

* Mon Jul 29 2019 Jamie Curnow <jc@jc21.com> 0.19.0-1
- v0.19.0

* Tue Jul 23 2019 Jamie Curnow <jc@jc21.com> 0.18.0-1
- v0.18.0

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

