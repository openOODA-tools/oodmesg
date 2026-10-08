# oodmesg: Sovereign KERNEL LOG RING

<div align="center">

```
================================================================================
                                oodmesg
               Sovereign openOODA KERNEL LOG RING
================================================================================
```

**Sovereign KERNEL LOG RING**  
*Prints and monitors kernel ring buffer events with timestamp conversions.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openOODA-tools.github.io/oodmesg/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oodmesg-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openOODA-tools.github.io/oodmesg/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openOODA-tools.github.io/oodmesg/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oodmesg-uninstall
# or: curl -fsSL https://openOODA-tools.github.io/oodmesg/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oodmesg [options]

Prints and filters the Linux kernel ring buffer with streaming MCP surface.

Options:
  -l, --level <list>   filter output by comma-separated severity levels:
                       emerg, alert, crit, err, warn, notice, info, debug
  -k, --kernel         display kernel messages only (facility kern)
  -u, --userspace      display userspace messages only (facility user)
  -n, --limit <num>    limit output to maximum number of messages
  -H, --human          human-readable output with readable timestamps
  -j, --json           output formatted as JSON Lines
  -D, --demo           synthetic Linux kernel boot sequence demonstration
      --color <WHEN>   colorize output: auto, always, never [default: auto]
      --theme <NAME>   override active oote palette
      --mcp            run as Model Context Protocol stdio server
      --test           run internal verification anchor suite
  -h, --help           display this help and exit
  -v, --version        output version information and exit
```

---

## 3. Theming Integration (`oote`)

`oodmesg` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oodmesg` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

* `dmesg_read`: Read kernel ring buffer log messages with optional severity filter and limit.
* `dmesg_search`: Search kernel ring buffer messages matching a substring query.
* `dmesg_filter_level`: Filter kernel messages by severity level string (emerg, alert, crit, err, warn, notice, info, debug).
* `dmesg_stats`: Summarize total counts of kernel messages grouped by severity level.
* `dmesg_demo`: Run synthetic demonstration of Linux kernel boot sequence.

```bash
oodmesg --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&ProcCap, &SysInfoCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
