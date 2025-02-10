# Steps

1. Load project in dev container

2. run : dagster dev \
Expeted: start with no error \
Actual: start with no error

3. Reproduce Error \
    3.1 uncomment lines 26-30 in definitions.py \
    3.2 run : dagster dev 

Expeted: start with no error \
Actual: failed with error: DagsterInvalidDefinitionError(f"Duplicate asset check key: {key}")


Question: 
We would expect to create multiple asset checks for the same asset with different severities
however function `build_last_update_freshness_checks` uses asset_key as a unique key to create asset_check key.
