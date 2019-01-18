# A Cloud Foundry Compatible Micro Framework

A [Cloud Foundry] compatible framework built from low footpring components with the purpose of being used on systems with lower CPU/RAM requirements.

[Cloud Foundry]: https://www.cloudfoundry.org/

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
- A Linux 64 bits system with:
    - 4 GB RAM
    - HAProxy 1.8+
    - Python3.7+ with "pip"
    - wget


## Setup

```sh
# Add the example hostnames to your /etc/hosts file:
echo 'api.example.com 127.0.0.80' |sudo tee -a /etc/hosts

# Clone the repository
git clone https://github.com/CCSGroupInternational/micro-cf
cd micro-cf

# Setup micro-cf environment variables setup
source setup/env.sh     

# Download binaries for the Golang based components
setup/download_bins.sh

# Generate SSL self signed certificates for HAProxy
setup/generate_ssl_self_signed.sh

# Generate the API file to be served for api_url/info
setup/generate_api_info.sh

# Start the haproxy
haproxy -D -f haproxy/api.cfg
```


## Testing

```sh

# Remove old config
rm -rf ~/.cf

# Setup environment variables
source setup/env.sh

# Get local api info
cf api https://$API_ENDPOINT
```