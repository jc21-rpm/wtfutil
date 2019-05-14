%define debug_package %{nil}

%global gh_user     wtfutil
%global gh_commit   9160d1fb0e73889edfe66e4e78485feed16ce924
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})

Name:           wtf
Version:        0.10.0
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

