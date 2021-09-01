%define version 20210831
%define release 1

%define name        nagios-bash-plugins
%define summary     Nagios plugin written in bash

%define packager    R Urrutia <Rafael.Urrutia.S@gmail.com

%define INSTALLBASE    /usr/local/nagios/libexec


Summary:        %{summary}
Name:           %{name}
Version:        %{version}
Release:        %{release}
Packager:       %{packager}
Group:          Applications/System
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
All plugins here are writen i bash script. They are tested in CentOS, Suse, RHEL and Photon OS.

%prep
rm -rf $RPM_BUILD_ROOT

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{INSTALLBASE}

cp $RPM_SOURCE_DIR/Readme	$RPM_BUILD_ROOT/%{INSTALLBASE}/

[[ -d $RPM_SOURCE_DIR/crl ]] && cp -r $RPM_SOURCE_DIR/crl       $RPM_BUILD_ROOT/%{SWAPHOME}/

%post

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(0755,root,root,-)

%changelog
* Tue Aug 31 2021 R Urrutia
- Create first version
