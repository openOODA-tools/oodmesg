Name:           oodmesg
Version:        0.1.0
Release:        1%{?dist}
Summary:        Prints and monitors kernel ring buffer events with timestamp conversions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oodmesg
Source0:        oodmesg-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oodmesg is a sovereign, capability-bounded KERNEL LOG RING written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oodmesg
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oodmesg-uninstall

%files
/usr/bin/oodmesg
/usr/bin/oodmesg-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
