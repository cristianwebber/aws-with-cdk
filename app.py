from aws_cdk import core

from base_data_plataform.airflow_stack.stack import AirflowStack
from base_data_plataform.athena.stack import AthenaStack
from base_data_plataform.common_stack import CommonStack
from base_data_plataform.data_lake.stack import DataLakeStack
from base_data_plataform.databricks.stack import DatabricksStack
from base_data_plataform.dms.stack import DmsStack
from base_data_plataform.glue_catalog.stack import GlueCatalogStack
from base_data_plataform.kinesis.stack import KinesisStack
from base_data_plataform.redshift.stack import RedshiftStack

app = core.App()
data_lake_stack = DataLakeStack(app)
common_stack = CommonStack(app)
kinesis_stack = KinesisStack(
    app, data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket
)
dms_stack = DmsStack(
    app,
    common_stack=common_stack,
    data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket,
)
athena_stack = AthenaStack(app)
glue_catalog_stack = GlueCatalogStack(
    app,
    raw_data_lake_bucket=data_lake_stack.data_lake_raw_bucket,
    processed_data_lake_bucket=data_lake_stack.data_lake_raw_processed,
)
databricks_stack = DatabricksStack(app)
airflow_stack = AirflowStack(
    app,
    common_stack=common_stack,
    data_lake_raw_bucket=data_lake_stack.data_lake_raw_bucket,
)
redshift_stack = RedshiftStack(
    app,
    common_stack=common_stack,
    data_lake_raw=data_lake_stack.data_lake_raw_bucket,
    data_lake_processed=data_lake_stack.data_lake_raw_processed,
)

app.synth()
