# A Cloud Foundry Compatible Micro Framework

A [Cloud Foundry] compatible framework built from low footpring components with the purpose of being used on systems with lower CPU/RAM requirements.

[Cloud Foundry]: https://www.cloudfoundry.org/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- A Linux 64 bits system with:
    - 4 GB RAM
    - HAProxy 1.8+
    - Python3.7+ with "pip"
    - wget

### Installing

```sh
git clone https://github.com/CCSGroupInternational/micro-cf
cd micro-cf
source setup/download_bins.sh  # Download required binaries to ~/micro-cf/bin
```

## Testing
```sh
scripts/start_all.sh
tests/run_all.sh
```
