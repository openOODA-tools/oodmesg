Name:           oodmesg
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign Linux kernel ring buffer reader and monitor in pure openOODA.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodmesg
Source0:        oodmesg-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodmesg is a sovereign, capability-bounded Linux kernel ring buffer reader
and monitor written in pure openOODA, featuring zero ambient authority,
systemd-journald alignment, severity filtering, synthetic boot showcases,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodmesg
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodmesg-uninstall

%files
/usr/bin/oodmesg
/usr/bin/oodmesg-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Sovereign pure openOODA elevation with dual-surface CLI and MCP
