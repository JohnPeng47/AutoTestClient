#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class TargetDomain:
    hostname: str
    parts: List[str] = field(init=False)

    def __post_init__(self) -> None:
        cleaned = self.hostname.strip()
        if not cleaned:
            raise ValueError("TargetDomain requires a non-empty hostname")
        parts = [part for part in cleaned.split(".") if part]
        if not parts:
            raise ValueError("TargetDomain requires at least one part")
        object.__setattr__(self, "hostname", cleaned)
        object.__setattr__(self, "parts", parts)

    @property
    def part_count(self) -> int:
        return len(self.parts)


@dataclass
class TargetDomainList:
    domains: List[TargetDomain]

    def _analysis(self) -> str:
        grouped: Dict[int, List[str]] = {}
        for domain in self.domains:
            grouped.setdefault(domain.part_count, []).append(domain.hostname)
        lines = ["TargetDomain analysis grouped by part count:"]
        for part_count in sorted(grouped):
            hostnames = sorted(grouped[part_count])
            lines.append(f"- {part_count} parts ({len(hostnames)} hostnames)")
            for hostname in hostnames:
                lines.append(f"    - {hostname}")
        return "\n".join(lines)


def build_targets() -> TargetDomainList:
    raw_domains = [
        "www.cibc.com",
        "cibconline.cibc.com",
        "www.cibconline.cibc.com",
        "analytics.cibc.com",
        "ebanking.cibc.com",
        "api.ebanking.cibc.com",
        "w-profiling.cibc.com",
        "digital.cibc.com",
        "1.digital.cibc.com",
        "experiences.cibc.com",
        "click.mail.us.cibc.com",
        "webmail.cibc.com",
        "mail.cibc.com",
        "login2-pte.cibc.com",
    ]
    domains = [TargetDomain(hostname=domain) for domain in raw_domains]
    return TargetDomainList(domains=domains)


def main() -> None:
    domain_list = build_targets()
    report = domain_list._analysis()
    print(report)


if __name__ == "__main__":
    main()
