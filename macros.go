%go_arches	%{ix86} %{x8664} %{armv5} %{armv6} %{armv7} aarch64 mips mipsel mips64 mips64le ppc64 ppc64le riscv64 s390x

%__go	\\\
%ifarch aarch64 \
	GOARCH=arm64 \\\
%endif \
%ifarch %{armv5} \
	GOARCH=arm \\\
	GOARM=5 \\\
%endif \
%ifarch %{armv6} \
	GOARCH=arm \\\
	GOARM=6 \\\
%endif \
%ifarch %{armv7} \
	GOARCH=arm \\\
	GOARM=7 \\\
%endif \
%ifarch mipsel \
	GOARCH=mipsle \\\
%endif \
%ifarch mips64el \
	GOARCH=mips64le \\\
%endif \
%ifarch %{ix86} \
	GOARCH=386 \\\
%endif \
%ifarch %{x8664} \
	GOARCH=amd64 \\\
%endif \
%ifarch mips mips64 ppc64 ppc64le riscv64 s390x \
	GOARCH=%{_arch} \\\
%endif \
	GOOS=linux \\\
	/usr/bin/go
