# Ruby specific macro definitions.

%__ruby			/usr/bin/ruby

# helpers to get rbconfig parameter
%__ruby_rbconfig()	%(%{__ruby} -r rbconfig -e 'print RbConfig::CONFIG["%1"]' 2>/dev/null || echo ERROR)
%__ruby_rbconfig_path()	%(%{__ruby} -r rbconfig -r pathname -e 'print Pathname(RbConfig::CONFIG["%1"]).cleanpath' 2>/dev/null || echo ERROR)

# Ruby ABI version
# NOTE: %ruby_version may be empty, depending how Ruby was built
%ruby_abi		%{expand:%%global ruby_abi %(%{__ruby} -r rbconfig -e 'print [RbConfig::CONFIG["MAJOR"], RbConfig::CONFIG["MINOR"]].join(".")' 2>/dev/null || echo ERROR)}%ruby_abi
# Ruby arch combo (CPU-OS, e.g. i686-linux)
%ruby_arch		%{expand:%%global ruby_arch %{__ruby_rbconfig arch}}%ruby_arch

%ruby_archdir		%{expand:%%global ruby_archdir %{__ruby_rbconfig_path archdir}}%ruby_archdir
%ruby_libdir		%{expand:%%global ruby_libdir %{__ruby_rbconfig rubylibdir}}%ruby_libdir
%ruby_ridir		%{expand:%%global ruby_ridir %(%{__ruby} -r rbconfig -e 'print File.join(RbConfig::CONFIG["datadir"], "ri", "system")' 2>/dev/null || echo ERROR)}%ruby_ridir
%ruby_rubylibdir	%{expand:%%global ruby_rubylibdir %{__ruby_rbconfig_path rubylibdir}}%ruby_rubylibdir
%ruby_rubyhdrdir	%{expand:%%global ruby_rubyhdrdir %{__ruby_rbconfig_path rubyhdrdir}}%ruby_rubyhdrdir
%ruby_vendorarchdir	%{expand:%%global ruby_vendorarchdir %{__ruby_rbconfig vendorarchdir}}%ruby_vendorarchdir
%ruby_vendorlibdir	%{expand:%%global ruby_vendorlibdir %{__ruby_rbconfig_path vendorlibdir}}%ruby_vendorlibdir
%ruby_sitearchdir	%{expand:%%global ruby_sitearchdir %{__ruby_rbconfig sitearchdir}}%ruby_sitearchdir
%ruby_sitedir		%{expand:%%global ruby_sitedir %{__ruby_rbconfig sitedir}}%ruby_sitedir
%ruby_sitelibdir	%{expand:%%global ruby_sitelibdir %{__ruby_rbconfig_path sitelibdir}}%ruby_sitelibdir
%ruby_rdocdir		/usr/share/rdoc
%ruby_vendordir		%{expand:%%global ruby_vendordir %{__ruby_rbconfig vendordir}}%ruby_vendordir
%ruby_version		%{expand:%%global ruby_version %(r=%{__ruby_rbconfig ruby_version}; echo ${r:-%%nil})}%ruby_version

%ruby_gemdir		%{expand:%%global ruby_gemdir %(%{__ruby} -r rubygems -e 'puts Gem.respond_to?(:default_dirs) ? Gem.default_dirs[:system][:gem_dir] : Gem.path.first' 2>/dev/null || echo ERROR)}%{ruby_gemdir}
%ruby_specdir		%{ruby_gemdir}/specifications

# deprecated, ruby 2.0 noarch packages are versionless and extension dependency is generated by rpm5
%ruby_ver_requires_eq		%{nil}
%ruby_mod_ver_requires_eq	%{nil}

%__gem_helper %{_rpmconfigdir}/gem_helper.rb

%gem_build(f:j:) \
	%__gem_helper build \\\
	%{-f:-f%{-f*}} \\\
	%{!-j:%{_smp_mflags}}%{-j:-j%{-j*}}

%gem_install(i:n:C) \
	DESTDIR=${DESTDIR:-%{buildroot}} \\\
	%__gem_helper install \\\
	--env-shebang --rdoc --ri --force --ignore-dependencies \\\
	%{!-i:--install-dir %{buildroot}%{ruby_gemdir}}%{-i:--install-dir %{-i*}} \\\
	%{!-n:--bindir %{buildroot}%{_bindir}}%{-n:--bindir%{-n*}} \\\
	%{!-C:--fix-permissions}
