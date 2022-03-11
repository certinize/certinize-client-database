"""
This type stub file was generated by pyright.
"""

_system = ...
if _system == 'Windows':
    def platform_exe(name):
        ...
    
else:
    def platform_exe(name):
        ...
    
def find_available_port(): # -> _RetAddress | None:
    ...

class ClusterError(Exception):
    ...


class Cluster:
    def __init__(self, data_dir, *, pg_config_path=...) -> None:
        ...
    
    def get_pg_version(self):
        ...
    
    def is_managed(self): # -> Literal[True]:
        ...
    
    def get_data_dir(self):
        ...
    
    def get_status(self): # -> Literal['not-initialized', 'stopped']:
        ...
    
    async def connect(self, loop=..., **kwargs):
        ...
    
    def init(self, **settings):
        """Initialize cluster."""
        ...
    
    def start(self, wait=..., *, server_settings=..., **opts):
        """Start the cluster."""
        ...
    
    def reload(self): # -> None:
        """Reload server configuration."""
        ...
    
    def stop(self, wait=...): # -> None:
        ...
    
    def destroy(self): # -> None:
        ...
    
    def get_connection_spec(self): # -> dict[str, str] | None:
        ...
    
    def override_connection_spec(self, **kwargs): # -> None:
        ...
    
    def reset_wal(self, *, oid=..., xid=...): # -> None:
        ...
    
    def reset_hba(self): # -> None:
        """Remove all records from pg_hba.conf."""
        ...
    
    def add_hba_entry(self, *, type=..., database, user, address=..., auth_method, auth_options=...): # -> None:
        """Add a record to pg_hba.conf."""
        ...
    
    def trust_local_connections(self): # -> None:
        ...
    
    def trust_local_replication_by(self, user): # -> None:
        ...
    


class TempCluster(Cluster):
    def __init__(self, *, data_dir_suffix=..., data_dir_prefix=..., data_dir_parent=..., pg_config_path=...) -> None:
        ...
    


class HotStandbyCluster(TempCluster):
    def __init__(self, *, master, replication_user, data_dir_suffix=..., data_dir_prefix=..., data_dir_parent=..., pg_config_path=...) -> None:
        ...
    
    def init(self, **settings): # -> str:
        """Initialize cluster."""
        ...
    
    def start(self, wait=..., *, server_settings=..., **opts): # -> None:
        ...
    


class RunningCluster(Cluster):
    def __init__(self, **kwargs) -> None:
        ...
    
    def is_managed(self): # -> Literal[False]:
        ...
    
    def get_connection_spec(self): # -> dict[str, Unknown]:
        ...
    
    def get_status(self): # -> Literal['running']:
        ...
    
    def init(self, **settings): # -> None:
        ...
    
    def start(self, wait=..., **settings): # -> None:
        ...
    
    def stop(self, wait=...): # -> None:
        ...
    
    def destroy(self): # -> None:
        ...
    
    def reset_hba(self):
        ...
    
    def add_hba_entry(self, *, type=..., database, user, address=..., auth_method, auth_options=...):
        ...
    


