#!/usr/bin/env bash
set -euxo pipefail

endpoint="api.fortress.com.hk/api/v2/ftrhk/products/search"

# https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
declare -A categories=( 
    ["vacuum"]=56
    ["aircon"]=51
    ["refrigerator"]=61
)

for category in "${!categories[@]}"; do
    xhs $endpoint \
        fields==FTR_FULL \
        curr==HKD \
        lang==en \
        pageSize==1000 \
        sort==bestSeller \
        ignoreSort==false \
        query==:bestSeller:category:${categories[$category]} | \
    jq "{\"type\": \"$category\", \"products\": [.products[] | {\"price\": .price.formattedValue, \"name\": .name, \"description\": .description, \"url\": (\"https://www.fortress.com.hk/en\" + .url), \"releaseDate\": .releaseDate}] | unique}" \
        > src/kb/fortress_$category.txt

done