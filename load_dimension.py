from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_query="",
                 append_only=False, # <--- Updated to match DAG
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_query = sql_query
        self.append_only = append_only

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        # If append_only is False, it means we want to clear the table first
        if not self.append_only:
            self.log.info(f"Truncating dimension table {self.table}")
            redshift.run(f"TRUNCATE TABLE {self.table}")
        
        self.log.info(f"Loading dimension table {self.table}")
        sql = f"INSERT INTO {self.table} {self.sql_query}"
        redshift.run(sql)