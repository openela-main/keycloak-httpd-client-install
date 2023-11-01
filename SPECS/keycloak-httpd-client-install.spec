%global srcname keycloak-httpd-client-install
%global summary Tools to configure Apache HTTPD as Keycloak client

%bcond_without python2
%bcond_with python3

Name:           %{srcname}
Version:        1.0
Release:        2%{?dist}
Summary:        %{summary}

%global git_tag RELEASE_%(r=%{version}; echo $r | tr '.' '_')

License:        GPLv3
URL:            https://github.com/jdennis/keycloak-httpd-client-install
Source0:        https://github.com/jdennis/keycloak-httpd-client-install/archive/%{git_tag}.tar.gz

Patch0001:      0001-doc-Fix-a-typo-in-oidc-redirect-uri-description.patch
Patch0002:      0002-Add-a-new-oidc-logout-uri-command-line-option.patch

BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       %{_bindir}/keycloak-httpd-client-install

%description
Keycloak is a federated Identity Provider (IdP). Apache HTTPD supports
a variety of authentication modules which can be configured to utilize
a Keycloak IdP to perform authentication. This package contains
libraries and tools which can automate and simplify configuring an
Apache HTTPD authentication module and registering as a client of a
Keycloak IdP.

%package -n python3-%{srcname}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{srcname}}

Requires:       %{name} = %{version}-%{release}
Requires:       python3-requests
Requires:       python3-requests-oauthlib
Requires:       python3-jinja2

%description -n python3-%{srcname}
Keycloak is an authentication server. This package contains libraries and
programs which can invoke the Keycloak REST API and configure clients
of a Keycloak server.

%prep
%autosetup -n %{srcname}-%{git_tag} -p1

%build
%py3_build

%install
%py3_install

install -d -m 755 %{buildroot}/%{_mandir}/man8
install -c -m 644 doc/keycloak-httpd-client-install.8 %{buildroot}/%{_mandir}/man8

%files
%license LICENSE.txt
%doc README.md doc/ChangeLog
%{_datadir}/%{srcname}/

%files -n python3-%{srcname}
%{python3_sitelib}/*
%{_bindir}/keycloak-httpd-client-install
%{_bindir}/keycloak-rest
%{_mandir}/man8/*

%changelog
* Wed Jul  3 2019 Jakub Hrozek <jhrozek@redhat.com> - 1.0-2
- Backport upstream patches to adds the --oidc-logout-uri option
  and fix OIDC-related man page issues
- Related: rhbz#1553890 - [RFE] Add mod_auth_openidc support

* Fri Jun 14 2019 Jakub Hrozek <jhrozek@redhat.com> - 1.0-1
- New upstream release
- Resolves: rhbz#1553890 - [RFE] Add mod_auth_openidc support

* Fri Jul 27 2018  <jdennis@redhat.com> - 0.8-7
- fix SOURCE0, it was pointing to github repo archive instead of release tarball

* Tue Jul 10 2018  <jdennis@redhat.com> - 0.8-6
- Restore use of bcond for python conditionals

* Mon Jul  9 2018  <jdennis@redhat.com> - 0.8-5
- Share same spec file with Fedora

* Mon Jun 11 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.8-4
- Conditionalize the python2 subpackage

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jan 10 2018 John Dennis <jdennis@redhat.com> - 0.8-1
- Upgrade to upstream 0,8, includes:
- CVE-2017-15112 unsafe use of -p/--admin-password on command line
- CVE-2017-15111 unsafe /tmp log file in --log-file option in keycloak_cli.py

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 John Dennis <jdennis@redhat.com> - 0.6-1
- Resolves: rhbz#1427720, if --mellon-root is not supplied and defaults to /
  you end up with double slashes in entityId and endpoints
- add --tls-verify option to control python-requests behavor when
  using tls to connect. With this option you can use a self-signed
  cert or point to a CA bundle.
- Fix warnings and checks when using client originate method
  'registration' with 'anonymous' authentication.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan  6 2017 John Dennis <jdennis@redhat.com> - 0.5-1
- Fix default port bug
  Strip the port from the URL if it matches the scheme (e.g. 80 for
  http and 443 for https)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 27 2016 John Dennis <jdennis@redhat.com> - 0.4-1
- new upstream
  See ChangeLog for details

* Fri May 20 2016 John Dennis <jdennis@redhat.com> - 0.3-1
- new upstream
  See ChangeLog for details

* Tue May 17 2016 John Dennis <jdennis@redhat.com> - 0.2-1
- new upstream
- Add keycloak-httpd-client-install.8 man page

* Fri May 13 2016 John Dennis <jdennis@redhat.com> - 0.1-1
- Initial version
