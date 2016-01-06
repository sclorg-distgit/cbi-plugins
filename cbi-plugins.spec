%{?scl:%scl_package cbi-plugins}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}cbi-plugins
Version:        1.1.2
Release:        3.1%{?dist}
Summary:        A set of helpers for Eclipse CBI

Group:          Development/Libraries
License:        EPL
URL:            http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/
Source0:        http://git.eclipse.org/c/cbi/org.eclipse.cbi.maven.plugins.git/snapshot/%{pkg_name}-%{version}.tar.bz2
Patch0:         maven-3.0.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}tycho
BuildRequires:  %{?scl_prefix}tycho-extras
BuildRequires:  %{?scl_prefix_java_common}maven-local
Requires:       %{?scl_prefix}tycho
Requires:       %{?scl_prefix}tycho-extras

%description
A set of helpers for Eclipse CBI.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -n %{pkg_name}-%{version} -q
%patch0 -p1 -R
%pom_disable_module eclipse-macsigner-plugin
%pom_disable_module eclipse-winsigner-plugin
%pom_remove_plugin :maven-enforcer-plugin
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 1.1.2-3.1
- Import latest from Fedora

* Mon Jun 22 2015 Mat Booth <mat.booth@redhat.com> - 1.1.2-3
- Drop unnecessary requires

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Alexander Kurtakov <akurtako@redhat.com> 1.1.2-1
- Update to upstream 1.1.2 release.

* Mon Jul 28 2014 Roland Grunberg <rgrunber@redhat.com> - 1.1.1-2
- Update to 1.1.1 Release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-2
- Disable win/mac signers.

* Wed Nov 13 2013 Alexander Kurtakov <akurtako@redhat.com> 1.0.5-1
- Update to latest upstream.

* Mon Sep 30 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.4-1
- Update to latest upstream.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.3-1
- Update to latest upstream.

* Thu Mar 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.4.git734d40
- Update to latest upstream.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.3.git120561
- Delete empty line from sources.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.2.git120561
- Review remarks fixed.

* Thu Feb 21 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.0.1-0.1.git120561
- Initial contribution.
