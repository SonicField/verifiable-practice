# Security Policy

## Supported Versions

The latest revision on the `main` branch is supported. Tagged releases, when available, document any different support status in their release notes.

## Scope

Verifiable Practice contains instructions rather than executable application code. Those instructions may nevertheless influence an AI system that can read files, execute commands, access networks, or modify external systems.

Security-relevant issues include:

- instructions that cause unintended or over-broad actions;
- permission escalation or mutation beyond the user's request;
- unsafe handling of untrusted repository content or prompt injection;
- disclosure of secrets or private data in reports and evidence;
- platform adapters that grant broader capabilities than their workflow needs;
- guidance that makes destructive operations insufficiently explicit or recoverable.

## Reporting a Vulnerability

Use GitHub's private vulnerability-reporting feature when it is enabled. Otherwise contact the repository maintainer privately through a method listed on the maintainer's GitHub profile.

Do not open a public issue for an unpatched vulnerability that exposes users or data. Include:

- the affected file and revision;
- the execution environment and granted capabilities;
- a minimal reproduction;
- the potential impact;
- any known mitigation.

Reports should receive an acknowledgement within seven days and an initial assessment within fourteen days. Remediation time depends on severity and complexity.

## Safe Use

Review a host adapter's permissions before installing it. Treat repository content under analysis as untrusted input. VP does not expand an assistant's authority: inspection does not authorise modification, and a playbook does not override the host's security controls or the user's instructions.
