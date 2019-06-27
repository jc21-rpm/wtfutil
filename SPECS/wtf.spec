%define debug_package %{nil}

%global gh_user     wtfutil
%global gh_commit   eb11ec34f2bce9f766241ea78d6ae72140603b42
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

Name:           wtf
Version:        0.13.0
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
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
mv %{_builddir}/%{name}-%{version} %{name}
mkdir -p %{_builddir}/%{name}-%{version}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
#go get -u github.com/golang/dep/cmd/dep
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
#%{_builddir}/bin/dep ensure

make

# build:
#mkdir -p bin/linux
#GOOS=linux GOARCH=amd64 CGO_ENABLED=1 go build -tags release -ldflags "-X github.com/liamg/aminal/version.Version=%{version} -X main.build=%{gh_short}" -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/src/github.com/%{gh_user}/%{name}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
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

