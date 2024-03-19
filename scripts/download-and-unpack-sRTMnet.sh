#!/bin/bash


# Download and unpack sRTM net.


set -x
set -o errexit
set -o pipefail
set -o nounset


SRTMNET_DIR="sRTMnet_v100"
SRTMNET_PATH="${SRTMNET_DIR}/sRTMnet_v100.h5"
SRTMNET_FILENAME="sRTMnet_v100.h5"

# If the desired sRTM net file already exists just assume it is correct and do
# nothing.
if [ -f "${SRTMNET_PATH}" ]; then
  echo "sRTM net already exists - nothing to do: ${SRTMNET_PATH}"
  exit 0
fi

mkdir -p "${SRTMNET_DIR}"

# Download sRTMnet file
wget \
  --no-verbose \
  --directory-prefix "${SRTMNET_DIR}" \
  "https://avng.jpl.nasa.gov/pub/PBrodrick/isofit/${SRTMNET_FILENAME}"
