from datetime import timedelta

from dagster import Definitions, build_last_update_freshness_checks, AssetCheckSeverity, asset

all_checks = []

@asset
def my_asset_1():
    return 1

@asset
def my_asset_2():
    return 2

all_checks.extend(build_last_update_freshness_checks(
        assets=[my_asset_1, my_asset_2],
        lower_bound_delta=timedelta(days=1),
        severity=AssetCheckSeverity.WARN
    )
)

# Uncomment to add an additional set of checks with a different severity 
# code fails with the following error:
# DagsterInvalidDefinitionError(f"Duplicate asset check key: {key}")
#all_checks.extend(build_last_update_freshness_checks(
#        assets=[my_asset_1, my_asset_2],
#        lower_bound_delta=timedelta(days=2),
#        severity=AssetCheckSeverity.ERROR
#    )
#)

defs = Definitions(
    assets=[my_asset_1, my_asset_2],
    asset_checks=all_checks,
)
