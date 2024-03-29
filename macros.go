%go_arches	%{ix86} %{x8664} %{armv5} %{armv6} %{armv7} aarch64 mips mipsel mips64 mips64le ppc64 ppc64le riscv64 s390x
%go_cachedir		%{?buildsubdir:%{_builddir}/%{buildsubdir}/}.go-cache

%__go	\\\
%ifarch aarch64 \
	GOARCH=${GOARCH-arm64} \\\
%endif \
%ifarch %{armv5} \
	GOARCH=${GOARCH-arm} \\\
	GOARM=${GOARM-5} \\\
%endif \
%ifarch %{armv6} \
	GOARCH=${GOARCH-arm} \\\
	GOARM=${GOARM-6} \\\
%endif \
%ifarch %{armv7} \
	GOARCH=${GOARCH-arm} \\\
	GOARM=${GOARM-7} \\\
%endif \
%ifarch mipsel \
	GOARCH=${GOARCH-mipsle} \\\
%endif \
%ifarch mips64el \
	GOARCH=${GOARCH-mips64le} \\\
%endif \
%ifarch %{ix86} \
	GOARCH=${GOARCH-386} \\\
%ifarch %{x86_with_sse2} \
	GO386=${GO386-sse2} \\\
%else \
	GO386=${GO386-softfloat} \\\
%endif \
%endif \
%ifarch %{x8664} \
	GOARCH=${GOARCH-amd64} \\\
%endif \
%ifarch mips mips64 ppc64 ppc64le riscv64 s390x \
	GOARCH=${GOARCH-%{_arch}} \\\
%endif \
	%{?go_cachedir:GOCACHE="${GOCACHE-%{go_cachedir}}"} \\\
	%{?__jobs:GOMAXPROCS=%{__jobs}} \\\
	GOOS=${GOOS-linux} \\\
	/usr/bin/go
