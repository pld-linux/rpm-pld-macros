%define		rpm_macros_rev	2.049
%define		find_lang_rev	1.42
# split into individual X_prov_ver if there is a reason to desync
%define		prov_ver	4.15
Summary:	PLD Linux RPM macros
Summary(pl.UTF-8):	Makra RPM dla Linuksa PLD
Name:		rpm-pld-macros
Version:	%{rpm_macros_rev}
Release:	1
License:	GPL v2+
Group:		Development/Building
Source0:	macros.pld
Source1:	service_generator.sh
Source3:	find-lang.sh
Source4:	dokuwiki-find-lang.sh
Source5:	macros.kernel
Source6:	attr.kernel
Source7:	rpmrc
Source8:	rpm-compress-doc
Source9:	rpm-find-spec-bcond

Source10:	macros.ruby
Source11:	attr.ruby
Source12:	rubygems.rb
Source13:	gem_helper.rb

Source20:	macros.java
Source21:	attr.java
Source22:	rpm-java-requires
Source23:	eclipse-feature.xslt

Source30:	macros.php
Source31:	attr.php
Source32:	rpm-php-provides
Source33:	rpm-php-requires
Source34:	rpm-php-requires.php

Source40:	macros.browser-plugins
Source41:	macros.cacti
Source42:	macros.emacs
Source43:	macros.ghc
Source44:	macros.nagios
Source45:	macros.openldap
Source46:	macros.perl
Source47:	macros.python
Source49:	macros.tcl
Source50:	macros.upstart
Source51:	macros.webapp
Source52:	macros.xmms
Source53:	macros.xorg
Source54:	macros.selinux
Source55:	macros.rust
Source56:	macros.arch
Source57:	macros.go
Source58:	macros.qt
Source59:	macros.erlang
Source60:	macros.gstreamer
Source61:	attr.gstreamer
Source62:	kmod-deps.sh
Source63:	attr.mono
Source64:	macros.vpath
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	sed >= 4.0
Obsoletes:	rpm-macros < 1.254
# rm: option `--interactive' doesn't allow an argument
Conflicts:	coreutils < 6.9
# tmpdir/_tmppath macros problems; optcppflags missing
Conflicts:	rpm < 4.4.9-72
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# redefine to bootstrap
%define		_usrlibrpm %{_prefix}/lib/rpm

# don't generate pear reqs for optional deps
%define		_noautoreq_pear		.*

%description
This package contains rpm macros for PLD Linux.

%description -l pl.UTF-8
Ten pakiet zawiera makra rpm-a dla Linuksa PLD.

%package build
Summary:	PLD Linux RPM build macros
Summary(pl.UTF-8):	Makra do budowania pakietów RPM dla Linuksa PLD
Requires:	%{name} = %{version}-%{release}
Requires:	findutils >= 1:4.2.26
Provides:	rpmbuild(find_lang) = %{find_lang_rev}
Provides:	rpmbuild(macros) = %{rpm_macros_rev}
Requires:	rpm-macros-systemd
Obsoletes:	rpm-build-macros < 1.745
# ensure cargo with install --no-track support
Conflicts:	cargo < 1.41.0
Conflicts:	gettext-devel < 0.11
# ensure not using meson without meson-related macros in package
Conflicts:	meson < 1.6.1-3
# ensure not using ninja without ninja-related macros in package
Conflicts:	ninja < 1.12.1-2
# macros.d/*
Conflicts:	rpm-build < 5.4.15-52
# php-config --sysconfdir
Conflicts:	php-devel < 4:5.2.0-3
Conflicts:	php4-devel < 3:4.4.4-10
# sysconfig module with proper 'purelib' path
Conflicts:	python3 < 1:3.2.1-3
%if "%{pld_release}" != "ac"
# libtool --install
Conflicts:	libtool < 2:2.2
%endif

%description build
This package contains rpm build macros for PLD Linux.

%description build -l pl.UTF-8
Ten pakiet zawiera makra rpm-a do budowania pakietów dla Linuksa PLD.

%package rubyprov
Summary:	Ruby tools, which simplify creation of RPM packages with Ruby software
Summary(pl.UTF-8):	Makra ułatwiające tworzenie pakietów RPM z programami napisanymi w Ruby
Group:		Applications/File
Requires:	%{name}-build = %{version}-%{release}
Requires:	ruby
Requires:	ruby-modules
Requires:	ruby-rubygems
Provides:	rpm-rubyprov = %{prov_ver}
Obsoletes:	rpm-rubyprov
# < 5.4.15-52 (use Epoch in Provides to be lower than Provides?)

%description rubyprov
Ruby tools, which simplifies creation of RPM packages with Ruby
software.

%description rubyprov -l pl.UTF-8
Makra ułatwiające tworzenie pakietów RPM z programami napisanymi w
Ruby.

%package javaprov
Summary:	Additional utilities for checking Java provides/requires in RPM packages
Summary(pl.UTF-8):	Dodatkowe narzędzia do sprawdzania zależności kodu w Javie w pakietach RPM
Group:		Applications/File
Requires:	%{name}-build = %{version}-%{release}
Requires:	jar
Requires:	jre
Requires:	file
Requires:	findutils >= 1:4.2.26
Requires:	mktemp
Requires:	unzip
Provides:	rpm-javaprov = %{prov_ver}
Obsoletes:	rpm-javaprov
# < 5.4.15-52 (use Epoch in Provides to be lower than Provides?)

%description javaprov
Additional utilities for checking Java provides/requires in RPM
packages.

%description javaprov -l pl.UTF-8
Dodatkowe narzędzia do sprawdzania zależności kodu w Javie w pakietach
RPM.

%package php-pearprov
Summary:	Additional utilities for checking PHP PEAR provides/requires in RPM packages
Summary(pl.UTF-8):	Dodatkowe narzędzia do sprawdzania zależności skryptów php w RPM
Group:		Applications/File
# The scripts are in perl
Requires:	perl-base
Requires:	%{name}-build = %{version}-%{release}
Requires:	sed >= 4.0
# Alternate req script in PHP
Suggests:	/usr/bin/php
Suggests:	php-pear-PHP_CompatInfo
Provides:	rpm-php-pearprov = %{prov_ver}
Obsoletes:	rpm-php-pearprov
# < 5.4.15-52 (use Epoch in Provides to be lower than Provides?)

%description php-pearprov
Additional utilities for checking PHP PEAR provides/requires in RPM
packages.

%description php-pearprov -l pl.UTF-8
Dodatkowe narzędzia do sprawdzenia zależności skryptów PHP PEAR w
pakietach RPM.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%build
%{__sed} -i -e 's,{Revision},%{rpm_macros_rev},' macros.pld

rev=$(awk '/^%%rpm_build_macros/{print $2}' macros.pld)
if [ "$rev" != "%rpm_macros_rev" ]; then
	: Update rpm_macros_rev define to $rev, and retry
	exit 1
fi
rev=$(awk -F= '/^VERSION/{print $2}' %{SOURCE3})
if [ "$rev" != "%find_lang_rev" ]; then
	: Update find_lang_rev define to $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_usrlibrpm}/{fileattrs,macros.d,pld}

cp -p macros.pld $RPM_BUILD_ROOT%{_usrlibrpm}/pld/macros
cp -p %{SOURCE7} $RPM_BUILD_ROOT%{_usrlibrpm}/pld/rpmrc

cp -p %{SOURCE8} $RPM_BUILD_ROOT%{_usrlibrpm}/compress-doc
cp -p %{SOURCE9} $RPM_BUILD_ROOT%{_usrlibrpm}/find-spec-bcond

cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.kernel
cp -p %{SOURCE6} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/kernel.attr
cp -p %{SOURCE62} $RPM_BUILD_ROOT%{_usrlibrpm}/kmod-deps.sh

cp -p service_generator.sh $RPM_BUILD_ROOT%{_usrlibrpm}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_usrlibrpm}/find-lang.sh
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_usrlibrpm}/dokuwiki-find-lang.sh

cp -p %{SOURCE10} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.ruby
cp -p %{SOURCE11} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/ruby.attr
cp -p %{SOURCE12} $RPM_BUILD_ROOT%{_usrlibrpm}/rubygems.rb
cp -p %{SOURCE13} $RPM_BUILD_ROOT%{_usrlibrpm}/gem_helper.rb

cp -p %{SOURCE20} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.java
cp -p %{SOURCE21} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/java.attr
cp -p %{SOURCE22} $RPM_BUILD_ROOT%{_usrlibrpm}/java-find-requires
cp -p %{SOURCE23} $RPM_BUILD_ROOT%{_usrlibrpm}/eclipse-feature.xslt

cp -p %{SOURCE30} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.php
cp -p %{SOURCE31} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/php.attr
cp -p %{SOURCE32} $RPM_BUILD_ROOT%{_usrlibrpm}/php.prov
cp -p %{SOURCE33} $RPM_BUILD_ROOT%{_usrlibrpm}/php.req
cp -p %{SOURCE34} $RPM_BUILD_ROOT%{_usrlibrpm}/php.req.php

cp -p %{SOURCE40} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.browser-plugins
cp -p %{SOURCE41} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.cacti
cp -p %{SOURCE42} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.emacs
cp -p %{SOURCE43} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.ghc
cp -p %{SOURCE44} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.nagios
cp -p %{SOURCE45} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.openldap
cp -p %{SOURCE46} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.perl
cp -p %{SOURCE47} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.python
cp -p %{SOURCE49} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.tcl
cp -p %{SOURCE50} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.upstart
cp -p %{SOURCE51} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.webapp
cp -p %{SOURCE52} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.xmms
cp -p %{SOURCE53} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.xorg
cp -p %{SOURCE54} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.selinux
cp -p %{SOURCE55} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.rust
cp -p %{SOURCE56} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.arch
cp -p %{SOURCE57} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.go
cp -p %{SOURCE58} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.qt
cp -p %{SOURCE59} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.erlang
cp -p %{SOURCE60} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.gstreamer
cp -p %{SOURCE61} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/gstreamer.attr
cp -p %{SOURCE63} $RPM_BUILD_ROOT%{_usrlibrpm}/fileattrs/mono.attr
cp -p %{SOURCE64} $RPM_BUILD_ROOT%{_usrlibrpm}/macros.d/macros.vpath

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_usrlibrpm}/pld/macros
%{_usrlibrpm}/pld/rpmrc

%files build
%defattr(644,root,root,755)
%{_usrlibrpm}/fileattrs/java.attr
%{_usrlibrpm}/fileattrs/gstreamer.attr
%{_usrlibrpm}/fileattrs/kernel.attr
%{_usrlibrpm}/fileattrs/mono.attr
%{_usrlibrpm}/fileattrs/php.attr
%{_usrlibrpm}/fileattrs/ruby.attr

%{_usrlibrpm}/macros.d/macros.arch
%{_usrlibrpm}/macros.d/macros.browser-plugins
%{_usrlibrpm}/macros.d/macros.cacti
%{_usrlibrpm}/macros.d/macros.emacs
%{_usrlibrpm}/macros.d/macros.erlang
%{_usrlibrpm}/macros.d/macros.ghc
%{_usrlibrpm}/macros.d/macros.go
%{_usrlibrpm}/macros.d/macros.gstreamer
%{_usrlibrpm}/macros.d/macros.java
%{_usrlibrpm}/macros.d/macros.kernel
%{_usrlibrpm}/macros.d/macros.nagios
%{_usrlibrpm}/macros.d/macros.openldap
%{_usrlibrpm}/macros.d/macros.perl
%{_usrlibrpm}/macros.d/macros.php
%{_usrlibrpm}/macros.d/macros.python
%{_usrlibrpm}/macros.d/macros.qt
%{_usrlibrpm}/macros.d/macros.ruby
%{_usrlibrpm}/macros.d/macros.rust
%{_usrlibrpm}/macros.d/macros.selinux
%{_usrlibrpm}/macros.d/macros.tcl
%{_usrlibrpm}/macros.d/macros.upstart
%{_usrlibrpm}/macros.d/macros.vpath
%{_usrlibrpm}/macros.d/macros.webapp
%{_usrlibrpm}/macros.d/macros.xmms
%{_usrlibrpm}/macros.d/macros.xorg

%attr(755,root,root) %{_usrlibrpm}/compress-doc
%attr(755,root,root) %{_usrlibrpm}/dokuwiki-find-lang.sh
%attr(755,root,root) %{_usrlibrpm}/find-lang.sh
%attr(755,root,root) %{_usrlibrpm}/find-spec-bcond
%attr(755,root,root) %{_usrlibrpm}/kmod-deps.sh
%attr(755,root,root) %{_usrlibrpm}/service_generator.sh

%files rubyprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_usrlibrpm}/gem_helper.rb
%attr(755,root,root) %{_usrlibrpm}/rubygems.rb

%files javaprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_usrlibrpm}/java-find-requires
%{_usrlibrpm}/eclipse-feature.xslt

%files php-pearprov
%defattr(644,root,root,755)
%attr(755,root,root) %{_usrlibrpm}/php.prov
%attr(755,root,root) %{_usrlibrpm}/php.req
%attr(755,root,root) %{_usrlibrpm}/php.req.php
