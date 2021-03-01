# TCL specific macro definitions.

%__tclsh	/usr/bin/tclsh

%tcl_version	%{expand:%%global tcl_version %(V=$(echo 'puts $tcl_version' | %{__tclsh}); echo ${V:-0})}%tcl_version
%tcl_sitearch	%{_libdir}/tcl%{tcl_version}
%tcl_sitelib	%{_datadir}/tcl%{tcl_version}
