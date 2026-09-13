<div align="center">

<img src="assets/profile-banner.svg" alt="Sahan Chathumina — Cybersecurity Portfolio Banner" width="100%"/>

</div>

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" width="700" height="300">
  <defs>
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0B1117;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#05070A;stop-opacity:1"/>
    </linearGradient>
    <linearGradient id="term-border" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.5"/>
      <stop offset="100%" style="stop-color:#1479FF;stop-opacity:0.2"/>
    </linearGradient>
    <linearGradient id="term-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF"/>
      <stop offset="100%" style="stop-color:#1479FF"/>
    </linearGradient>
    <filter id="term-glow">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="term-clip">
      <rect x="0" y="0" width="700" height="300" rx="12"/>
    </clipPath>
  </defs>

  <g clip-path="url(#term-clip)">
    <rect width="700" height="300" rx="12" fill="url(#term-bg)"/>
    <rect width="700" height="300" rx="12" fill="none" stroke="url(#term-border)" stroke-width="1"/>

    <!-- Title bar -->
    <rect x="0" y="0" width="700" height="32" fill="#111820" opacity="0.8"/>
    <circle cx="18" cy="16" r="5" fill="#FF5F56"/>
    <circle cx="36" cy="16" r="5" fill="#FFBD2E"/>
    <circle cx="54" cy="16" r="5" fill="#27C93F"/>
    <text x="350" y="20" text-anchor="middle" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="11" fill="#7F95A5">terminal — cyberlab</text>

    <!-- Scanline effect -->
    <rect x="0" y="0" width="700" height="2" fill="#00D9FF" opacity="0.08">
      <animate attributeName="y" values="0;300;0" dur="4s" repeatCount="indefinite"/>
    </rect>

    <!-- whoami command -->
    <g>
      <text x="20" y="50" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="13" fill="#00D9FF" opacity="0">
        $ whoami
        <animate attributeName="opacity" values="0;1" dur="0.3s" fill="freeze"/>
      </text>
      <text x="20" y="70" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="13" fill="#EAF7FF" opacity="0">
        sahan.chathumina@cyberlab
        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.3s" fill="freeze"/>
      </text>
    </g>

    <!-- focus command -->
    <g>
      <text x="20" y="110" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="13" fill="#00D9FF" opacity="0">
        $ focus
        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.6s" fill="freeze"/>
      </text>

      
      <text x="32" y="130" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#7F95A5" opacity="0">
        <tspan fill="#00D9FF" opacity="0.6">▸</tspan> Cybersecurity
        <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.8s" fill="freeze"/>
      </text>

      <text x="32" y="150" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#7F95A5" opacity="0">
        <tspan fill="#00D9FF" opacity="0.6">▸</tspan> Network Engineering
        <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.1s" fill="freeze"/>
      </text>

      <text x="32" y="170" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#7F95A5" opacity="0">
        <tspan fill="#00D9FF" opacity="0.6">▸</tspan> Linux
        <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.4s" fill="freeze"/>
      </text>

      <text x="32" y="190" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#7F95A5" opacity="0">
        <tspan fill="#00D9FF" opacity="0.6">▸</tspan> Ethical Hacking
        <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.7s" fill="freeze"/>
      </text>

      <!-- Colored reveal line under focus -->
      <rect x="20" y="214" width="0" height="1" rx="0.5" fill="url(#term-accent)">
        <animate attributeName="width" from="0" to="400" dur="0.8s" begin="2s" fill="freeze"/>
      </rect>
    </g>

    <!-- status command -->
    <g>
      <text x="20" y="250" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="13" fill="#00D9FF" opacity="0">
        $ status
        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="2.7s" fill="freeze"/>
      </text>

      <g opacity="0">
        <circle cx="28" cy="266" r="4" fill="#00FF88" filter="url(#term-glow)"/>
        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="3s" fill="freeze"/>
        <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite" begin="3.3s"/>
      </g>

      <text x="40" y="270" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#EAF7FF" opacity="0">
        ONLINE  •  LEARNING  •  BUILDING
        <animate attributeName="opacity" values="0;1" dur="0.3s" begin="3s" fill="freeze"/>
      </text>
    </g>

    <!-- Blinking cursor -->
    <rect x="20" y="310" width="7" height="14" fill="#00D9FF" opacity="0">
      <animate attributeName="opacity" values="0;0.7;0" dur="1.2s" repeatCount="indefinite" begin="3.4000000000000004s"/>
    </rect>
  </g>
</svg>

</div>

<div align="center">

## About Me

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 340" width="800" height="340">
  <defs>
    <linearGradient id="ab-card" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0B1117;stop-opacity:0.95"/>
      <stop offset="100%" style="stop-color:#111820;stop-opacity:0.9"/>
    </linearGradient>
    <linearGradient id="ab-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.2"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0.1"/>
    </linearGradient>
    <linearGradient id="ab-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#1479FF;stop-opacity:1"/>
    </linearGradient>
    <filter id="ab-glow">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="ab-soft">
      <feGaussianBlur stdDeviation="1.5"/>
    </filter>
    <clipPath id="ab-clip">
      <rect x="40" y="40" width="720" height="260" rx="16"/>
    </clipPath>
  </defs>

  <!-- Background glow -->
  <ellipse cx="400" cy="170" rx="300" ry="150" fill="#00D9FF" opacity="0.03" filter="url(#ab-soft)"/>

  <!-- Card background -->
  <rect x="40" y="40" width="720" height="260" rx="16" fill="url(#ab-card)"/>
  <rect x="40" y="40" width="720" height="260" rx="16" fill="none" stroke="url(#ab-border)" stroke-width="1"/>

  <!-- Top accent line -->
  <rect x="60" y="40" width="80" height="2" rx="1" fill="url(#ab-accent)" opacity="0.8"/>

  <!-- Section label -->
  <text x="64" y="72" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="10" fill="#00D9FF" letter-spacing="2" opacity="0.7">PROFILE</text>

  <!-- Vertical accent bar -->
  <rect x="64" y="90" width="2" height="50" rx="1" fill="url(#ab-accent)" opacity="0.6"/>

  <!-- Name -->
  <text x="80" y="108" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="22" font-weight="700" fill="#EAF7FF">Sahan Chathumina</text>

  <!-- Tagline -->
  <text x="80" y="130" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="12" fill="#00D9FF" letter-spacing="0.5">Cybersecurity | Network Engineering | Linux | Ethical Hacking</text>

  <!-- Animated cursor -->
  <rect x="519.2" y="119" width="8" height="14" fill="#00D9FF" opacity="0.7">
    <animate attributeName="opacity" values="0.7;0;0.7" dur="1.2s" repeatCount="indefinite"/>
  </rect>

  <!-- Divider line -->
  <line x1="64" y1="150" x2="736" y2="150" stroke="#1A2736" stroke-width="0.5" opacity="0.5"/>

  <!-- Description text -->
  <foreignObject x="64" y="160" width="672" height="80">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family:'Segoe UI',Arial,sans-serif;font-size:13px;line-height:1.6;color:#7F95A5;">
      Building secure systems. Exploring networks. Learning cybersecurity through hands-on projects.
    </div>
  </foreignObject>

  <!-- Focus areas -->
  
  <rect x="64" y="250" width="165" height="36" rx="8" fill="#111820" stroke="#1A2736" stroke-width="0.5" opacity="0.8"/>
  <circle cx="78" cy="268" r="3" fill="#00D9FF" opacity="0.8">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="88" y="272" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="11" fill="#EAF7FF">Cybersecurity</text>

  <rect x="244" y="250" width="165" height="36" rx="8" fill="#111820" stroke="#1A2736" stroke-width="0.5" opacity="0.8"/>
  <circle cx="258" cy="268" r="3" fill="#00D9FF" opacity="0.8">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <text x="268" y="272" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="11" fill="#EAF7FF">Network Engineering</text>

  <rect x="424" y="250" width="165" height="36" rx="8" fill="#111820" stroke="#1A2736" stroke-width="0.5" opacity="0.8"/>
  <circle cx="438" cy="268" r="3" fill="#00D9FF" opacity="0.8">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
  </circle>
  <text x="448" y="272" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="11" fill="#EAF7FF">Linux</text>

  <rect x="604" y="250" width="165" height="36" rx="8" fill="#111820" stroke="#1A2736" stroke-width="0.5" opacity="0.8"/>
  <circle cx="618" cy="268" r="3" fill="#00D9FF" opacity="0.8">
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3.5s" repeatCount="indefinite"/>
  </circle>
  <text x="628" y="272" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="11" fill="#EAF7FF">Ethical Hacking</text>

  <!-- Stats row -->
  <line x1="64" y1="300" x2="736" y2="300" stroke="#1A2736" stroke-width="0.5" opacity="0.3"/>

  
  <text x="64" y="322" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="10" fill="#7F95A5" letter-spacing="1">FOCUS</text>
  <text x="64" y="344" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="16" font-weight="700" fill="#EAF7FF">Security &amp; Networks</text>

  <text x="288" y="322" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="10" fill="#7F95A5" letter-spacing="1">STATUS</text>
  <text x="288" y="344" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="16" font-weight="700" fill="#EAF7FF">Learning &amp; Building</text>

  <text x="512" y="322" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="10" fill="#7F95A5" letter-spacing="1">STACK</text>
  <text x="512" y="344" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="16" font-weight="700" fill="#EAF7FF">Linux • Python • Bash</text>

  <!-- Bottom accent -->
  <rect x="660" y="298" width="80" height="2" rx="1" fill="url(#ab-accent)" opacity="0.4"/>

  <!-- Corner decorations -->
  <path d="M 56 44 L 52 44 L 44 52 L 44 56" fill="none" stroke="#00D9FF" stroke-width="0.5" opacity="0.3"/>
  <path d="M 744 296 L 748 296 L 756 288 L 756 284" fill="none" stroke="#00D9FF" stroke-width="0.5" opacity="0.3"/>
</svg>

</div>

<div align="center">

## Skill Overview

<img src="assets/skill-circles.svg" alt="Skill proficiency percentages" width="620"/>

</div>

## Skills & Technologies

### Cybersecurity

![Ethical Hacking](https://img.shields.io/badge/Ethical%20Hacking-Learning-blue) ![Network Security](https://img.shields.io/badge/Network%20Security-Learning-blue) ![Vulnerability Assessment](https://img.shields.io/badge/Vulnerability%20Assessment-Learning-blue) ![Security Hardening](https://img.shields.io/badge/Security%20Hardening-Practicing-cyan) ![OSINT](https://img.shields.io/badge/OSINT-Learning-blue) ![CTF](https://img.shields.io/badge/CTF-Practicing-cyan) ![Web Security](https://img.shields.io/badge/Web%20Security-Learning-blue) ![Digital Forensics](https://img.shields.io/badge/Digital%20Forensics-Learning-blue)

### Networking

![TCP/IP](https://img.shields.io/badge/TCP%2FIP-Practicing-cyan) ![DNS](https://img.shields.io/badge/DNS-Practicing-cyan) ![DHCP](https://img.shields.io/badge/DHCP-Practicing-cyan) ![HTTP/HTTPS](https://img.shields.io/badge/HTTP%2FHTTPS-Practicing-cyan) ![Routing & Switching](https://img.shields.io/badge/Routing%20%26%20Switching-Learning-blue) ![VLAN](https://img.shields.io/badge/VLAN-Learning-blue) ![Subnetting](https://img.shields.io/badge/Subnetting-Practicing-cyan) ![Firewalls](https://img.shields.io/badge/Firewalls-Learning-blue) ![VPN](https://img.shields.io/badge/VPN-Learning-blue) ![Cisco Networking](https://img.shields.io/badge/Cisco%20Networking-Learning-blue)

### Linux & Systems

![Linux](https://img.shields.io/badge/Linux-Practicing-cyan) ![CentOS](https://img.shields.io/badge/CentOS-Practicing-cyan) ![Rocky Linux](https://img.shields.io/badge/Rocky%20Linux-Learning-blue) ![SSH](https://img.shields.io/badge/SSH-Practicing-cyan) ![Apache](https://img.shields.io/badge/Apache-Practicing-cyan) ![BIND DNS](https://img.shields.io/badge/BIND%20DNS-Practicing-cyan) ![firewalld](https://img.shields.io/badge/firewalld-Practicing-cyan) ![systemd](https://img.shields.io/badge/systemd-Practicing-cyan) ![Bash](https://img.shields.io/badge/Bash-Practicing-cyan) ![Server Hardening](https://img.shields.io/badge/Server%20Hardening-Learning-blue) ![SELinux](https://img.shields.io/badge/SELinux-Learning-blue) ![Auditd](https://img.shields.io/badge/Auditd-Learning-blue)

### Development

![Python](https://img.shields.io/badge/Python-Practicing-cyan) ![Bash](https://img.shields.io/badge/Bash-Practicing-cyan) ![JavaScript](https://img.shields.io/badge/JavaScript-Learning-blue) ![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-Practicing-cyan) ![PHP](https://img.shields.io/badge/PHP-Learning-blue) ![MySQL](https://img.shields.io/badge/MySQL-Learning-blue) ![Full Stack Development](https://img.shields.io/badge/Full%20Stack%20Development-Learning-blue)

### Tools

![Git](https://img.shields.io/badge/Git-Practicing-cyan) ![GitHub](https://img.shields.io/badge/GitHub-Practicing-cyan) ![Wireshark](https://img.shields.io/badge/Wireshark-Learning-blue) ![Nmap](https://img.shields.io/badge/Nmap-Learning-blue) ![Metasploit](https://img.shields.io/badge/Metasploit-Learning-blue) ![Burp Suite](https://img.shields.io/badge/Burp%20Suite-Learning-blue) ![VMware](https://img.shields.io/badge/VMware-Practicing-cyan)





<div align="center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 20" width="800" height="20">
  <defs>
    <linearGradient id="sd-g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0"/>
      <stop offset="45%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.6"/>
      <stop offset="55%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="10" x2="800" y2="10" stroke="url(#sd-g)" stroke-width="1"/>
  <circle cx="400" cy="10" r="2.5" fill="#00D9FF" opacity="0.5"/>
</svg></div>



<div align="center">

## Network Architecture

<img src="assets/network-topology.svg" alt="Network topology diagram" width="600"/>

</div>

## Featured Projects

<table>
<tr>
<td width="33%" valign="top">

> **PROJECT 01**

### Network Security Lab

Hands-on environment for practicing network security, Linux administration, DNS, DHCP, and server hardening.

<sub>Linux • Networking • DNS • DHCP • Bash</sub>

![In Progress](https://img.shields.io/badge/In%20Progress-yellow)

</td>
<td width="33%" valign="top">

> **PROJECT 02**

### Linux Server Hardening

Server hardening lab covering SSH security, firewall rules, SELinux, audit logging, and system monitoring.

<sub>Linux • SSH • firewalld • SELinux • Auditd</sub>

![In Progress](https://img.shields.io/badge/In%20Progress-yellow)

</td>
<td width="33%" valign="top">

> **PROJECT 03**

### DNS & DHCP Lab

Configured BIND DNS and ISC DHCP servers on CentOS with zone transfers and dynamic updates.

<sub>Linux • BIND • DHCP • CentOS • Networking</sub>

![Completed](https://img.shields.io/badge/Completed-brightgreen)

</td>
</tr>
<tr>
<td width="33%" valign="top">

> **PROJECT 04**

### Python Security Scripts

Collection of Python scripts for network scanning, port detection, and security automation tasks.

<sub>Python • Networking • Security</sub>

![In Progress](https://img.shields.io/badge/In%20Progress-yellow)

</td>
<td width="33%" valign="top">

> **PROJECT 05**

### Firewall Configuration Lab

Practicing firewall rules with firewalld, iptables, and network segmentation scenarios.

<sub>Linux • firewalld • Networking • Security</sub>

![Learning](https://img.shields.io/badge/Learning-blue)

</td>
<td width="33%" valign="top">

> **PROJECT 06**

### Web Application Security Lab

Hands-on practice with common web vulnerabilities in a controlled lab environment.

<sub>Web Security • HTTP • Burp Suite</sub>

![Learning](https://img.shields.io/badge/Learning-blue)

</td>
</tr>
</table>




<div align="center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 20" width="800" height="20">
  <defs>
    <linearGradient id="sd-g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0"/>
      <stop offset="45%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.6"/>
      <stop offset="55%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="10" x2="800" y2="10" stroke="url(#sd-g)" stroke-width="1"/>
  <circle cx="400" cy="10" r="2.5" fill="#00D9FF" opacity="0.5"/>
</svg></div>



<div align="center">

## Cybersecurity Lab

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 252" width="800" height="252">
  
  <g opacity="0" transform="translate(0, 6)">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 6;0 0" dur="0.4s" begin="0s" fill="freeze"/>

    <rect x="24" y="24" width="752" height="60" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="24" width="752" height="60" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <rect x="24" y="32" width="3" height="44" rx="1.5" fill="#1479FF" opacity="0.6"/>

    <text x="40" y="46" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#1479FF" letter-spacing="1" opacity="0.7">CTF 01</text>
    <text x="40" y="62" font-family="'Segoe UI',Arial,sans-serif" font-size="13" font-weight="600" fill="#EAF7FF">Web Exploitation</text>
    <text x="40" y="76" font-family="'Segoe UI',Arial,sans-serif" font-size="10" fill="#7F95A5">TryHackMe  •  Easy - Medium</text>

    <text x="760" y="62" text-anchor="end" font-family="'SF Mono',monospace" font-size="9" fill="#00D9FF" opacity="0.7">3 skills</text>
  </g>
  <g opacity="0" transform="translate(0, 6)">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.12s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 6;0 0" dur="0.4s" begin="0.12s" fill="freeze"/>

    <rect x="24" y="92" width="752" height="60" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="92" width="752" height="60" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <rect x="24" y="100" width="3" height="44" rx="1.5" fill="#1479FF" opacity="0.6"/>

    <text x="40" y="114" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#1479FF" letter-spacing="1" opacity="0.7">CTF 02</text>
    <text x="40" y="130" font-family="'Segoe UI',Arial,sans-serif" font-size="13" font-weight="600" fill="#EAF7FF">Forensics</text>
    <text x="40" y="144" font-family="'Segoe UI',Arial,sans-serif" font-size="10" fill="#7F95A5">TryHackMe  •  Easy</text>

    <text x="760" y="130" text-anchor="end" font-family="'SF Mono',monospace" font-size="9" fill="#00D9FF" opacity="0.7">3 skills</text>
  </g>
  <g opacity="0" transform="translate(0, 6)">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.24s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 6;0 0" dur="0.4s" begin="0.24s" fill="freeze"/>

    <rect x="24" y="160" width="752" height="60" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="160" width="752" height="60" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <rect x="24" y="168" width="3" height="44" rx="1.5" fill="#1479FF" opacity="0.6"/>

    <text x="40" y="182" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#1479FF" letter-spacing="1" opacity="0.7">CTF 03</text>
    <text x="40" y="198" font-family="'Segoe UI',Arial,sans-serif" font-size="13" font-weight="600" fill="#EAF7FF">Cryptography</text>
    <text x="40" y="212" font-family="'Segoe UI',Arial,sans-serif" font-size="10" fill="#7F95A5">PicoCTF  •  Easy - Medium</text>

    <text x="760" y="198" text-anchor="end" font-family="'SF Mono',monospace" font-size="9" fill="#00D9FF" opacity="0.7">3 skills</text>
  </g>
</svg>

</div>

<div align="center">

## Linux Labs

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 528" width="800" height="528">
  <defs>
    <filter id="lc-glow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <!-- Card 1 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0s" fill="freeze"/>

    <rect x="24" y="24" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="24" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="34" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="46" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 01</text>

    <!-- Lab name -->
    <text x="40" y="64" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">SSH Security Lab</text>

    <!-- Objective -->
    <text x="40" y="82" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure SSH key-based auth, disable root login, impleme...</text>

    <!-- Technology pills -->
    
    <rect x="785" y="36" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="50" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="719" y="36" width="37" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="737.5" y="50" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">SSH</text>

    <!-- Status dot -->
    <circle cx="760" cy="59" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.5s"/>
    </circle>
  </g>
  <!-- Card 2 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.15s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.15s" fill="freeze"/>

    <rect x="24" y="104" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="104" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="114" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="126" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 02</text>

    <!-- Lab name -->
    <text x="40" y="144" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">DNS Server Lab</text>

    <!-- Objective -->
    <text x="40" y="162" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Set up BIND DNS master/slave with zone transfers</text>

    <!-- Technology pills -->
    
    <rect x="785" y="116" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="130" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="712" y="116" width="44" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="734" y="130" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">BIND</text>
    <rect x="639" y="116" width="37" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="657.5" y="130" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">DNS</text>

    <!-- Status dot -->
    <circle cx="760" cy="139" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.65s"/>
    </circle>
  </g>
  <!-- Card 3 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.3s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.3s" fill="freeze"/>

    <rect x="24" y="184" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="184" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="194" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="206" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 03</text>

    <!-- Lab name -->
    <text x="40" y="224" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">DHCP Server Lab</text>

    <!-- Objective -->
    <text x="40" y="242" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure ISC DHCP with reservations and relay agents</text>

    <!-- Technology pills -->
    
    <rect x="785" y="196" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="210" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="712" y="196" width="44" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="734" y="210" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">DHCP</text>

    <!-- Status dot -->
    <circle cx="760" cy="219" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.8s"/>
    </circle>
  </g>
  <!-- Card 4 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.44999999999999996s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.44999999999999996s" fill="freeze"/>

    <rect x="24" y="264" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="264" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="274" width="3" height="50" rx="1.5" fill="#00D9FF" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="286" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00D9FF" letter-spacing="1.5" opacity="0.7">LAB 04</text>

    <!-- Lab name -->
    <text x="40" y="304" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">Firewall Rules Lab</text>

    <!-- Objective -->
    <text x="40" y="322" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Implement zone-based firewall rules and NAT</text>

    <!-- Technology pills -->
    
    <rect x="785" y="276" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="290" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="677" y="276" width="79" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="716.5" y="290" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">firewalld</text>
    <rect x="590" y="276" width="86" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="633" y="290" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Networking</text>

    <!-- Status dot -->
    <circle cx="760" cy="299" r="4" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.95s"/>
    </circle>
  </g>
  <!-- Card 5 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.6s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.6s" fill="freeze"/>

    <rect x="24" y="344" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="344" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="354" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="366" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 05</text>

    <!-- Lab name -->
    <text x="40" y="384" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">Apache Web Server Lab</text>

    <!-- Objective -->
    <text x="40" y="402" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure virtual hosts, SSL/TLS, and access controls</text>

    <!-- Technology pills -->
    
    <rect x="785" y="356" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="370" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="698" y="356" width="58" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="727" y="370" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Apache</text>

    <!-- Status dot -->
    <circle cx="760" cy="379" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="1.1s"/>
    </circle>
  </g>
  <!-- Card 6 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.75s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.75s" fill="freeze"/>

    <rect x="24" y="424" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="424" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="434" width="3" height="50" rx="1.5" fill="#1479FF" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="446" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#1479FF" letter-spacing="1.5" opacity="0.7">LAB 06</text>

    <!-- Lab name -->
    <text x="40" y="464" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">SELinux Lab</text>

    <!-- Objective -->
    <text x="40" y="482" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure SELinux policies and troubleshoot denials</text>

    <!-- Technology pills -->
    
    <rect x="785" y="436" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="450" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="691" y="436" width="65" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="723.5" y="450" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">SELinux</text>

    <!-- Status dot -->
    <circle cx="760" cy="459" r="4" fill="#1479FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="1.25s"/>
    </circle>
  </g>
</svg>

</div>

<div align="center">

## Networking Labs

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 448" width="800" height="448">
  <defs>
    <filter id="lc-glow">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  
  <!-- Card 1 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0s" fill="freeze"/>

    <rect x="24" y="24" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="24" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="34" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="46" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 01</text>

    <!-- Lab name -->
    <text x="40" y="64" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">DNS Server Lab</text>

    <!-- Objective -->
    <text x="40" y="82" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Set up BIND DNS master/slave with zone transfers</text>

    <!-- Technology pills -->
    
    <rect x="785" y="36" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="50" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="712" y="36" width="44" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="734" y="50" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">BIND</text>
    <rect x="639" y="36" width="37" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="657.5" y="50" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">DNS</text>

    <!-- Status dot -->
    <circle cx="760" cy="59" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.5s"/>
    </circle>
  </g>
  <!-- Card 2 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.15s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.15s" fill="freeze"/>

    <rect x="24" y="104" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="104" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="114" width="3" height="50" rx="1.5" fill="#00FF88" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="126" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00FF88" letter-spacing="1.5" opacity="0.7">LAB 02</text>

    <!-- Lab name -->
    <text x="40" y="144" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">DHCP Server Lab</text>

    <!-- Objective -->
    <text x="40" y="162" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure ISC DHCP with reservations and relay agents</text>

    <!-- Technology pills -->
    
    <rect x="785" y="116" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="130" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="712" y="116" width="44" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="734" y="130" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">DHCP</text>

    <!-- Status dot -->
    <circle cx="760" cy="139" r="4" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.65s"/>
    </circle>
  </g>
  <!-- Card 3 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.3s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.3s" fill="freeze"/>

    <rect x="24" y="184" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="184" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="194" width="3" height="50" rx="1.5" fill="#00D9FF" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="206" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00D9FF" letter-spacing="1.5" opacity="0.7">LAB 03</text>

    <!-- Lab name -->
    <text x="40" y="224" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">Firewall Rules Lab</text>

    <!-- Objective -->
    <text x="40" y="242" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Implement zone-based firewall rules and NAT</text>

    <!-- Technology pills -->
    
    <rect x="785" y="196" width="51" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="810.5" y="210" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Linux</text>
    <rect x="677" y="196" width="79" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="716.5" y="210" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">firewalld</text>
    <rect x="590" y="196" width="86" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="633" y="210" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Networking</text>

    <!-- Status dot -->
    <circle cx="760" cy="219" r="4" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.8s"/>
    </circle>
  </g>
  <!-- Card 4 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.44999999999999996s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.44999999999999996s" fill="freeze"/>

    <rect x="24" y="264" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="264" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="274" width="3" height="50" rx="1.5" fill="#00D9FF" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="286" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#00D9FF" letter-spacing="1.5" opacity="0.7">LAB 04</text>

    <!-- Lab name -->
    <text x="40" y="304" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">Subnetting Practice</text>

    <!-- Objective -->
    <text x="40" y="322" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Practice VLSM subnetting and IP address planning</text>

    <!-- Technology pills -->
    
    <rect x="750" y="276" width="86" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="793" y="290" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Networking</text>
    <rect x="670" y="276" width="86" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="713" y="290" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Subnetting</text>

    <!-- Status dot -->
    <circle cx="760" cy="299" r="4" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.95s"/>
    </circle>
  </g>
  <!-- Card 5 -->
  <g opacity="0" transform="translate(0, 8)">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.6s" fill="freeze"/>
    <animateTransform attributeName="transform" type="translate" values="0 8;0 0" dur="0.5s" begin="0.6s" fill="freeze"/>

    <rect x="24" y="344" width="752" height="70" rx="10" fill="#0B1117" opacity="0.8"/>
    <rect x="24" y="344" width="752" height="70" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Left accent -->
    <rect x="24" y="354" width="3" height="50" rx="1.5" fill="#7F95A5" opacity="0.7"/>

    <!-- Lab number -->
    <text x="40" y="366" font-family="'SF Mono','Cascadia Code','Consolas',monospace" font-size="9" fill="#7F95A5" letter-spacing="1.5" opacity="0.7">LAB 05</text>

    <!-- Lab name -->
    <text x="40" y="384" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF">VLAN Configuration Lab</text>

    <!-- Objective -->
    <text x="40" y="402" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="11" fill="#7F95A5">Configure VLANs, trunk ports, and inter-VLAN routing</text>

    <!-- Technology pills -->
    
    <rect x="750" y="356" width="86" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="793" y="370" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Networking</text>
    <rect x="712" y="356" width="44" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="734" y="370" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">VLAN</text>
    <rect x="597" y="356" width="79" height="20" rx="10" fill="#111820" stroke="#1A2736" stroke-width="0.5"/>
    <text x="636.5" y="370" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="9" fill="#7F95A5">Switching</text>

    <!-- Status dot -->
    <circle cx="760" cy="379" r="4" fill="#7F95A5" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="1.1s"/>
    </circle>
  </g>
</svg>

</div>



<div align="center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 20" width="800" height="20">
  <defs>
    <linearGradient id="sd-g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0"/>
      <stop offset="45%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.6"/>
      <stop offset="55%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="10" x2="800" y2="10" stroke="url(#sd-g)" stroke-width="1"/>
  <circle cx="400" cy="10" r="2.5" fill="#00D9FF" opacity="0.5"/>
</svg></div>



<div align="center">

## Certifications &amp; Courses

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 340" width="700" height="340">
  <!-- Vertical line -->
  <line x1="40" y1="10" x2="40" y2="310" stroke="#1A2736" stroke-width="1" opacity="0.2"/>
  
  <!-- Item 1 -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0s" fill="freeze"/>

    <!-- Connection line -->
    <line x1="40" y1="42" x2="40" y2="126" stroke="#1A2736" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.3"/>

    <!-- Outer glow ring -->
    <circle cx="40" cy="36" r="12" fill="none" stroke="#00FF88" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="10;14;10" dur="3s" repeatCount="indefinite" begin="0s"/>
      <animate attributeName="opacity" values="0.3;0.1;0.3" dur="3s" repeatCount="indefinite" begin="0s"/>
    </circle>

    <!-- Main node -->
    <circle cx="40" cy="36" r="7" fill="#05070A" stroke="#00FF88" stroke-width="2"/>
    <circle cx="40" cy="36" r="3" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.5s"/>
    </circle>

    <!-- Card -->
    <rect x="50" y="16" width="630" height="90" rx="10" fill="#0B1117" opacity="0.7"/>
    <rect x="50" y="16" width="630" height="90" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Accent glow on left -->
    <rect x="50" y="26" width="2" height="70" rx="1" fill="#00FF88" opacity="0.5"/>

    <!-- Year -->
    <text x="66" y="34" font-family="'SF Mono','Consolas',monospace" font-size="11" font-weight="600" fill="#00FF88">2026</text>

    <!-- Title -->
    <text x="66" y="54" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="15" font-weight="600" fill="#EAF7FF">Red Hat System Administration I</text>

    <!-- Subtitle -->
    <text x="66" y="72" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="12" fill="#7F95A5">Red Hat</text>

    <!-- Status badge -->
    <rect x="550" y="34" width="80" height="22" rx="11" fill="#111820" stroke="#00FF88" stroke-width="0.8" opacity="0.8"/>
    <text x="590" y="49" text-anchor="middle" font-family="'SF Mono',monospace" font-size="8" fill="#00FF88" letter-spacing="0.5">COMPLETED</text>
  </g>
  <!-- Item 2 -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.2s" fill="freeze"/>

    <!-- Connection line -->
    <line x1="40" y1="142" x2="40" y2="226" stroke="#1A2736" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.3"/>

    <!-- Outer glow ring -->
    <circle cx="40" cy="136" r="12" fill="none" stroke="#00D9FF" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="10;14;10" dur="3s" repeatCount="indefinite" begin="0.2s"/>
      <animate attributeName="opacity" values="0.3;0.1;0.3" dur="3s" repeatCount="indefinite" begin="0.2s"/>
    </circle>

    <!-- Main node -->
    <circle cx="40" cy="136" r="7" fill="#05070A" stroke="#00D9FF" stroke-width="2"/>
    <circle cx="40" cy="136" r="3" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.7s"/>
    </circle>

    <!-- Card -->
    <rect x="50" y="116" width="630" height="90" rx="10" fill="#0B1117" opacity="0.7"/>
    <rect x="50" y="116" width="630" height="90" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Accent glow on left -->
    <rect x="50" y="126" width="2" height="70" rx="1" fill="#00D9FF" opacity="0.5"/>

    <!-- Year -->
    <text x="66" y="134" font-family="'SF Mono','Consolas',monospace" font-size="11" font-weight="600" fill="#00D9FF">2026</text>

    <!-- Title -->
    <text x="66" y="154" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="15" font-weight="600" fill="#EAF7FF">CCNA: Introduction to Networks</text>

    <!-- Subtitle -->
    <text x="66" y="172" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="12" fill="#7F95A5">Cisco</text>

    <!-- Status badge -->
    <rect x="550" y="134" width="80" height="22" rx="11" fill="#111820" stroke="#00D9FF" stroke-width="0.8" opacity="0.8"/>
    <text x="590" y="149" text-anchor="middle" font-family="'SF Mono',monospace" font-size="8" fill="#00D9FF" letter-spacing="0.5">IN PROGRESS</text>
  </g>
  <!-- Item 3 -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.4s" fill="freeze"/>

    <!-- Connection line -->
    

    <!-- Outer glow ring -->
    <circle cx="40" cy="236" r="12" fill="none" stroke="#00FF88" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="10;14;10" dur="3s" repeatCount="indefinite" begin="0.4s"/>
      <animate attributeName="opacity" values="0.3;0.1;0.3" dur="3s" repeatCount="indefinite" begin="0.4s"/>
    </circle>

    <!-- Main node -->
    <circle cx="40" cy="236" r="7" fill="#05070A" stroke="#00FF88" stroke-width="2"/>
    <circle cx="40" cy="236" r="3" fill="#00FF88" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.9s"/>
    </circle>

    <!-- Card -->
    <rect x="50" y="216" width="630" height="90" rx="10" fill="#0B1117" opacity="0.7"/>
    <rect x="50" y="216" width="630" height="90" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Accent glow on left -->
    <rect x="50" y="226" width="2" height="70" rx="1" fill="#00FF88" opacity="0.5"/>

    <!-- Year -->
    <text x="66" y="234" font-family="'SF Mono','Consolas',monospace" font-size="11" font-weight="600" fill="#00FF88">2025</text>

    <!-- Title -->
    <text x="66" y="254" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="15" font-weight="600" fill="#EAF7FF">Diploma in English</text>

    <!-- Subtitle -->
    <text x="66" y="272" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="12" fill="#7F95A5">Academy - English in Seven Boxes</text>

    <!-- Status badge -->
    <rect x="550" y="234" width="80" height="22" rx="11" fill="#111820" stroke="#00FF88" stroke-width="0.8" opacity="0.8"/>
    <text x="590" y="249" text-anchor="middle" font-family="'SF Mono',monospace" font-size="8" fill="#00FF88" letter-spacing="0.5">COMPLETED</text>
  </g>
</svg>

</div>

<div align="center">

## Education

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 240" width="700" height="240">
  <!-- Vertical line -->
  <line x1="40" y1="10" x2="40" y2="210" stroke="#1A2736" stroke-width="1" opacity="0.2"/>
  
  <!-- Item 1 -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0s" fill="freeze"/>

    <!-- Connection line -->
    <line x1="40" y1="42" x2="40" y2="126" stroke="#1A2736" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.3"/>

    <!-- Outer glow ring -->
    <circle cx="40" cy="36" r="12" fill="none" stroke="#00D9FF" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="10;14;10" dur="3s" repeatCount="indefinite" begin="0s"/>
      <animate attributeName="opacity" values="0.3;0.1;0.3" dur="3s" repeatCount="indefinite" begin="0s"/>
    </circle>

    <!-- Main node -->
    <circle cx="40" cy="36" r="7" fill="#05070A" stroke="#00D9FF" stroke-width="2"/>
    <circle cx="40" cy="36" r="3" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.5s"/>
    </circle>

    <!-- Card -->
    <rect x="50" y="16" width="630" height="90" rx="10" fill="#0B1117" opacity="0.7"/>
    <rect x="50" y="16" width="630" height="90" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Accent glow on left -->
    <rect x="50" y="26" width="2" height="70" rx="1" fill="#00D9FF" opacity="0.5"/>

    <!-- Year -->
    <text x="66" y="34" font-family="'SF Mono','Consolas',monospace" font-size="11" font-weight="600" fill="#00D9FF">2024 - Present</text>

    <!-- Title -->
    <text x="66" y="54" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="15" font-weight="600" fill="#EAF7FF">BSc (Hons) in Ethical Hacking &amp; Network Security</text>

    <!-- Subtitle -->
    <text x="66" y="72" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="12" fill="#7F95A5">University</text>

    <!-- Status badge -->
    <rect x="550" y="34" width="80" height="22" rx="11" fill="#111820" stroke="#00D9FF" stroke-width="0.8" opacity="0.8"/>
    <text x="590" y="49" text-anchor="middle" font-family="'SF Mono',monospace" font-size="8" fill="#00D9FF" letter-spacing="0.5">IN PROGRESS</text>
  </g>
  <!-- Item 2 -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="0.2s" fill="freeze"/>

    <!-- Connection line -->
    

    <!-- Outer glow ring -->
    <circle cx="40" cy="136" r="12" fill="none" stroke="#00D9FF" stroke-width="0.5" opacity="0.3">
      <animate attributeName="r" values="10;14;10" dur="3s" repeatCount="indefinite" begin="0.2s"/>
      <animate attributeName="opacity" values="0.3;0.1;0.3" dur="3s" repeatCount="indefinite" begin="0.2s"/>
    </circle>

    <!-- Main node -->
    <circle cx="40" cy="136" r="7" fill="#05070A" stroke="#00D9FF" stroke-width="2"/>
    <circle cx="40" cy="136" r="3" fill="#00D9FF" opacity="0.8">
      <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="0.7s"/>
    </circle>

    <!-- Card -->
    <rect x="50" y="116" width="630" height="90" rx="10" fill="#0B1117" opacity="0.7"/>
    <rect x="50" y="116" width="630" height="90" rx="10" fill="none" stroke="#1A2736" stroke-width="0.5"/>

    <!-- Accent glow on left -->
    <rect x="50" y="126" width="2" height="70" rx="1" fill="#00D9FF" opacity="0.5"/>

    <!-- Year -->
    <text x="66" y="134" font-family="'SF Mono','Consolas',monospace" font-size="11" font-weight="600" fill="#00D9FF">2023 - Present</text>

    <!-- Title -->
    <text x="66" y="154" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="15" font-weight="600" fill="#EAF7FF">Higher National Diploma in Network Engineering</text>

    <!-- Subtitle -->
    <text x="66" y="172" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="12" fill="#7F95A5">Institute of Network Engineering</text>

    <!-- Status badge -->
    <rect x="550" y="134" width="80" height="22" rx="11" fill="#111820" stroke="#00D9FF" stroke-width="0.8" opacity="0.8"/>
    <text x="590" y="149" text-anchor="middle" font-family="'SF Mono',monospace" font-size="8" fill="#00D9FF" letter-spacing="0.5">IN PROGRESS</text>
  </g>
</svg>

</div>

## Currently Learning

> ● **ACTIVE**

- Cybersecurity Fundamentals
- Network Security
- Linux System Administration
- Ethical Hacking
- CTF Challenges
- Python for Security Automation
- Cloud & Infrastructure Security



<div align="center"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 20" width="800" height="20">
  <defs>
    <linearGradient id="sd-g" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0"/>
      <stop offset="45%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.6"/>
      <stop offset="55%" style="stop-color:#00D9FF;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0"/>
    </linearGradient>
  </defs>
  <line x1="0" y1="10" x2="800" y2="10" stroke="url(#sd-g)" stroke-width="1"/>
  <circle cx="400" cy="10" r="2.5" fill="#00D9FF" opacity="0.5"/>
</svg></div>



## GitHub Statistics

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Sahan-Chathumina-25&show_icons=true&theme=dark&hide_border=true&bg_color=%230B1117&title_color=%2300D9FF&text_color=%23EAF7FF&icon_color=%2300D9FF" alt="GitHub Stats" height="165"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sahan-Chathumina-25&layout=compact&theme=dark&hide_border=true&bg_color=%230B1117&title_color=%2300D9FF&text_color=%23EAF7FF&lang_count=6" alt="Top Languages" height="165"/>

</div>


<div align="center">

## Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/Sahan-Chathumina-25)

</div>

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="600" height="120">
  <defs>
    <linearGradient id="ft-accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00D9FF;stop-opacity:0.8"/>
      <stop offset="50%" style="stop-color:#1479FF;stop-opacity:0.8"/>
      <stop offset="100%" style="stop-color:#00D9FF;stop-opacity:0.8"/>
    </linearGradient>
    <filter id="ft-glow">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- Top divider line -->
  <line x1="50" y1="15" x2="550" y2="15" stroke="#1A2736" stroke-width="0.5" opacity="0.3"/>

  <!-- Animated accent line -->
  <line x1="50" y1="15" x2="50" y2="15" stroke="url(#ft-accent)" stroke-width="1.5" filter="url(#ft-glow)">
    <animate attributeName="x2" values="50;550" dur="1.5s" fill="freeze"/>
  </line>

  <!-- Center pulse dot -->
  <circle cx="300" cy="15" r="0" fill="#00D9FF" filter="url(#ft-glow)">
    <animate attributeName="r" values="0;4;2" dur="1.5s" fill="freeze"/>
    <animate attributeName="opacity" values="0;0.8;0.6" dur="1.5s" fill="freeze"/>
  </circle>

  <!-- Status text -->
  <text x="300" y="45" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="10" fill="#7F95A5" letter-spacing="2" opacity="0">
    SYSTEM STATUS
    <animate attributeName="opacity" values="0;0.5" dur="0.5s" begin="0.8s" fill="freeze"/>
  </text>

  <text x="300" y="62" text-anchor="middle" font-family="'SF Mono','Consolas',monospace" font-size="13" fill="#00D9FF" letter-spacing="1" opacity="0">
    ● ONLINE
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1s" fill="freeze"/>
  </text>

  <circle cx="252" cy="58" r="3" fill="#00FF88" opacity="0">
    <animate attributeName="opacity" values="0;0.7" dur="0.3s" begin="1s" fill="freeze"/>
    <animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite" begin="1.3s"/>
  </circle>

  <!-- Tagline -->
  <text x="300" y="88" text-anchor="middle" font-family="'Segoe UI','Inter',Arial,sans-serif" font-size="14" font-weight="600" fill="#EAF7FF" letter-spacing="4" opacity="0">
    BUILD  •  LEARN  •  SECURE
    <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.3s" fill="freeze"/>
  </text>

  <!-- Bottom decorative dots -->
  <circle cx="270" cy="105" r="1.5" fill="#00D9FF" opacity="0">
    <animate attributeName="opacity" values="0;0.4" dur="0.3s" begin="1.5s" fill="freeze"/>
  </circle>
  <circle cx="300" cy="105" r="1.5" fill="#1479FF" opacity="0">
    <animate attributeName="opacity" values="0;0.4" dur="0.3s" begin="1.6s" fill="freeze"/>
  </circle>
  <circle cx="330" cy="105" r="1.5" fill="#00D9FF" opacity="0">
    <animate attributeName="opacity" values="0;0.4" dur="0.3s" begin="1.7s" fill="freeze"/>
  </circle>

  <!-- Bottom line reveal -->
  <line x1="300" y1="115" x2="300" y2="115" stroke="url(#ft-accent)" stroke-width="0.8" opacity="0.3">
    <animate attributeName="x1" values="300;50" dur="1s" begin="1.8s" fill="freeze"/>
    <animate attributeName="x2" values="300;550" dur="1s" begin="1.8s" fill="freeze"/>
  </line>
</svg>

</div>