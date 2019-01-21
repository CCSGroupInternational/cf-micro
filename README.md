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
# Add the example host names to your /etc/hosts file:
cat << _EOF_ |sudo tee -a /etc/hosts
127.0.0.80 api.example.com
127.0.0.81 uaa.example.com
127.0.0.82 rqlite.example.com
_EOF_

# Clone the repository
git clone https://github.com/CCSGroupInternational/micro-cf
cd micro-cf

# Setup micro-cf environment variables setup
source setup/env.sh     

# Download binaries for the Golang based components
setup/download_bins.sh

# Install python requirements
pip install --user -r requirements.txt 

# Generate SSL self signed certificates for HAProxy
setup/generate_ssl_self_signed.sh

# Generate the API file to be served for api_url/info
setup/generate_api_info.sh

# Start the RQLITE DB service
nohup rqlited \
    -http-addr ${RQLITE_BACKEND_FIRST_IP}:${RQLITE_BACKEND_PORT} \
    -raft-addr ${RQLITE_CLUSTER_FIRST_IP}:${RQLITE_CLUSTER_PORT} \
    ~/rqlite_node1 &

# Start the haproxy
haproxy -f haproxy/

# If you are running for the first time, bootstrap the UAA database, using:
setup/uaa_db_bootstrap.py

# Start the UAA server
PORT=${UAA_BACKEND_PORT} quickweb run uaa-server -l ${UAA_BACKEND_FIRST_IP} 
```

## Testing

```sh

# Remove old config
rm -rf ~/.cf

# Setup environment variables
source setup/env.sh

# Get local api info
cf api https://$API_ENDPOINT --skip-ssl-validation
```
